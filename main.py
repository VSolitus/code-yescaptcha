import requests
import json
from flask import Flask, request

global global_key

def index_n():
    url = "http://cn.yescaptcha.com/getBalance"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "clientKey": global_key,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    H1 = '------------------------------------------------------------------\n'
    H2 = '     作者 V_Solitus https://github.com/VSolitus/code-yescaptcha   \n'
    H3 = f'     当前余额：{response.json()["balance"]   }                \n'
    H4 = '------------------------------------------------------------------\n'
    title=H1 + H2 + H3 + H4
    return title
def createTask(data,clas):
    url = "http://cn.yescaptcha.com/createTask"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "clientKey": global_key,
        "task": {
            "type": "ImageToTextTaskTest",
            "case": clas,
            "body": data
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['solution']['text']
app = Flask(__name__)
#接收ImageToTextTask : 图片不定长英文数字
@app.route('/ImageToTextTask', methods=['POST'])
def handle_create_task():
    data = request.json
    return createTask(data.get('data'),data.get('class'))
if __name__ == '__main__':
    global_key="3e51e*****************3337" #此处填入你的key
    print(index_n())
    app.run(host='127.0.0.1', port=5200)
