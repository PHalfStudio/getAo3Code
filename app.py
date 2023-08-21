from flask import Flask, request
from module.code import get_key

app = Flask(__name__)
app.json.ensure_ascii = False


@app.route('/ao3web/authentication', methods=['POST'])
def check_key():
    if int(request.form['key']) == int(get_key()):
        return {
            "message": "success",
            "code": "200"
        }
    else:
        return {
            "message": "fail",
            "code": "404"
        }


@app.route('/test/wechat', methods=['POST'])
def test():
    print(request.form['Content'])


if __name__ == '__main__':
    app.run()
