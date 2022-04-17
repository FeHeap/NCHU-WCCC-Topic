from flask import Flask,render_template,request
import os
import psycopg2

import random

from base64 import b64encode, b64decode
from binascii import unhexlify

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(iv, passwd, msg):
    # Convert Hex String to Binary
    iv = unhexlify(iv)
    passwd = unhexlify(passwd)

    # Pad to AES Block Size
    msg = pad(msg.encode(), AES.block_size)
    # Encipher Text
    cipher = AES.new(passwd, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(msg)

    # Encode Cipher_text as Base 64 and decode to String
    out = b64encode(cipher_text).decode('utf-8')

    return out

app = Flask(__name__)


@app.route('/getCipherUID', methods=['POST'])
def getCipherUID():
    phone = request.values['phone']

    # Heroku works
    DATABASE_URL = os.environ['DATABASE_URL']

    # connect with database
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # create cursor
    cursor = conn.cursor()

    SQL_select_command = """
           SELECT * FROM UIDTable
           WHERE phone={phone};
       """
    # execute SQL
    cursor.execute(SQL_select_command)
    data = cursor.fetchall()

    if len(data) != 0:
        return ''
    else:
        hexArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        UID = ''
        for j in range(64):
            UID += hexArray[random.randint(0, 15)]
        SQL_insert_command = """
                   INSERT INTO ivPasswdTable
                    (phone, UID)
                    VALUES (%s, %s);
               """
        # execute SQL
        cursor.execute(SQL_insert_command, phone, UID)


        SQL_select_command = """
                   SELECT * FROM ivPasswdTable;
               """
        cursor.execute(SQL_select_command)
        ivPasswds = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

        random.shuffle(ivPasswds)

        cipherIDs = ''
        for ivPasswd in ivPasswds[:96]:
            cipherIDs += ',' + ivPasswd[0] + encrypt(ivPasswd[1], ivPasswd[2], UID)

        return cipherIDs[1:]

@app.route('/sendPointAndLinks', methods=['POST'])
def sendPointAndLinks():
    pointAndLinks = request.values['pointAndLinks']

    # Heroku works
    DATABASE_URL = os.environ['DATABASE_URL']

    # connect with database
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # create cursor
    cursor = conn.cursor()

    SQL_insert_command = """
                       INSERT INTO pointAndLinks
                        (key_UID, links_UID)
                        VALUES (%s, %s);
                   """
    # execute SQL
    cursor.execute(SQL_insert_command, pointAndLinks[:67], pointAndLinks[68:])

    conn.commit()
    cursor.close()
    conn.close()

    return ''

@app.route('/sendCovid', methods=['POST'])
def sendCovid():
    UID = request.values['UID']

    # Heroku works
    DATABASE_URL = os.environ['DATABASE_URL']

    # connect with database
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # create cursor
    cursor = conn.cursor()

    SQL_insert_command = """
                       INSERT INTO covid
                        (UID)
                        VALUES (%s);
                   """
    # execute SQL
    cursor.execute(SQL_insert_command, UID)

    conn.commit()
    cursor.close()
    conn.close()

    return ''

if __name__ == '__main__':
    app.run()
