import os
import psycopg2

def ivPasswdTable():
    herokuCLI_command = 'heroku config:get DATABASE_URL -a nchu-cse-wccc-topic-final'
    DATABASE_URL = os.popen(herokuCLI_command).read()[:-1]

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cursor = conn.cursor()

    SQL_command = '''
            CREATE TABLE IF NOT EXISTS ivPasswdTable (
                index VARCHAR(3),
                iv VARCHAR(32),
                passwd VARCHAR(32)
            );
    '''
    cursor.execute(SQL_command)

    f = open('ivPasswdTable.txt', 'r')
    ivPasswds = [x.strip('\n').split(',') for x in f.readlines()]
    f.close()

    for ivPasswd in ivPasswds:
        print(ivPasswd)
        SQL_command = '''
                INSERT INTO ivPasswdTable
                    (index, iv, passwd)
                    VALUES (%s, %s, %s);
        '''
        cursor.execute(SQL_command, ivPasswd)

    conn.commit()

    cursor.close()
    conn.close()


def UIDTable():
    herokuCLI_command = 'heroku config:get DATABASE_URL -a nchu-cse-wccc-topic-final'
    DATABASE_URL = os.popen(herokuCLI_command).read()[:-1]

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cursor = conn.cursor()

    SQL_command = '''
            CREATE TABLE IF NOT EXISTS UIDTable (
                phone VARCHAR(15),
                UID VARCHAR(64)
            );
    '''
    cursor.execute(SQL_command)

    conn.commit()

    cursor.close()
    conn.close()


def pointAndLinks():
    herokuCLI_command = 'heroku config:get DATABASE_URL -a nchu-cse-wccc-topic-final'
    DATABASE_URL = os.popen(herokuCLI_command).read()[:-1]

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cursor = conn.cursor()

    SQL_command = '''
                CREATE TABLE IF NOT EXISTS pointAndLinks (
                    key_UID VARCHAR(67),
                    links_UID VARCHAR(6800)
                );
        '''
    cursor.execute(SQL_command)

    conn.commit()

    cursor.close()
    conn.close()

def covidTable():
    herokuCLI_command = 'heroku config:get DATABASE_URL -a nchu-cse-wccc-topic-final'
    DATABASE_URL = os.popen(herokuCLI_command).read()[:-1]

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cursor = conn.cursor()

    SQL_command = '''
                CREATE TABLE IF NOT EXISTS covid (
                    key_UID VARCHAR(67)
                );
        '''
    cursor.execute(SQL_command)

    conn.commit()

    cursor.close()
    conn.close()


def getPointAndLinks():
    herokuCLI_command = 'heroku config:get DATABASE_URL -a nchu-cse-wccc-topic-final'
    DATABASE_URL = os.popen(herokuCLI_command).read()[:-1]

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cursor = conn.cursor()

    SQL_select_command = """
                       SELECT * FROM pointAndLinks;
                   """
    cursor.execute(SQL_select_command)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    f = open("pointAndLinks.txt", "w")
    for subdata in data:
        f.write(f'{subdata[0]},{subdata[1]}\n')
    f.close()

def getCovid():
    herokuCLI_command = 'heroku config:get DATABASE_URL -a nchu-cse-wccc-topic-final'
    DATABASE_URL = os.popen(herokuCLI_command).read()[:-1]

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cursor = conn.cursor()

    SQL_select_command = """
                       SELECT * FROM covid;
                   """
    cursor.execute(SQL_select_command)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    f = open("covid.txt", "w")
    for subdata in data:
        f.write(f'{subdata}\n')
    f.close()



if __name__ == '__main__':
    # ivPasswdTable()
    # UIDTable()
    # pointAndLinks()
    # covidTable()
    getPointAndLinks()
    getCovid()