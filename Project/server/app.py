from flask import Flask, render_template, request


app = Flask(__name__)


linkMap = {}
covidMap = {}


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/connect', methods=['POST', 'GET'])
def connect():
    if request.method == 'POST':
        link = request.form
        print("link -" + link["myPhone"] + "- and -" + link["Others"] + "-")
        if (link["myPhone"] in linkMap):
            linkMap[link["myPhone"]][link["Others"]] = None
        else:
            linkMap[link["myPhone"]] = { link["Others"]:None }

        if (link["Others"] in linkMap):
            linkMap[link["Others"]][link["myPhone"]] = None
        else:
            linkMap[link["Others"]] = { link["myPhone"]:None }

    return render_template("index.html")


@app.route('/covid', methods=['POST', 'GET'])
def covid():

    if request.method == 'POST':
        person = request.form['myPhone']
        if person not in covidMap:
            covidMap[person] = None

        print("In covidMap:", end="")
        for node in covidMap.keys():
            print(node, end=" ")
        print()

        leafToRoot = {}

        for root in covidMap.keys():
            if root in linkMap:
                for leaf in linkMap[root]:
                    if leaf in leafToRoot:
                        leafToRoot[leaf].append(root)
                    else:
                        leafToRoot[leaf] = [root]

        haveDone = {}
        hardLink = {}
        for leaf in leafToRoot.keys():
            if leaf in haveDone:
                continue
            haveDone[leaf] = None
            for outleaf in linkMap[leaf]:
                if outleaf in leafToRoot.keys() and leafToRoot[leaf] != leafToRoot[outleaf]:
                    linkBuff = []
                    for root in leafToRoot[leaf]:
                        if root not in linkBuff:
                            linkBuff.append(root)
                    for root in leafToRoot[outleaf]:
                        if root not in linkBuff:
                            linkBuff.append(root)
                    link = "-".join(linkBuff)
                    if(link in hardLink):
                        print("bad")
                    hardLink[link] = None
                    haveDone[outleaf] = None

        for link in hardLink.keys():
            print(link)

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
