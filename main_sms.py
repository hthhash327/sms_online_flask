from flask import Flask, request, jsonify
import requests
import threading
import resource_1

app = Flask(__name__)

# 存储轮询任务的状态
tasks = {}

def send(keys, url, payload, headers):
    try:
        if keys in resource_1.Get:
            response = requests.get(url, json=payload, headers=headers)
        else:
            response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"{keys} 请求成功,返回结果：{response.text}")
        else:
            print(f"{keys} 请求失败,返回结果：{response.text}")
    except requests.RequestException as e:
        print(f"{keys} 请求异常,返回结果：", e)

def polling_task(number):
    dicts = resource_1.preparingnumber(number)
    import time
    while tasks.get(number, {}).get("running", False):
        for key, items in dicts.items():
            if not tasks.get(number, {}).get("running", False):
                break
            send(key, items[0], items[1], items[2])
            time.sleep(3)

@app.route("/send", methods=["GET"])
def start_send():
    number = request.args.get("number", "").strip()
    if not number.isdigit() or len(number) != 11:
        return jsonify({"code": 400, "msg": "手机号格式不正确"}), 400

    if number in tasks and tasks[number]["running"]:
        return jsonify({"code": 200, "msg": "该手机号任务已在运行中"})

    tasks[number] = {"running": True}
    t = threading.Thread(target=polling_task, args=(number,), daemon=True)
    t.start()
    return jsonify({"code": 200, "msg": f"手机号 {number} 轮询任务已启动"})

@app.route("/stop", methods=["GET"])
def stop_send():
    number = request.args.get("number", "").strip()
    if number in tasks:
        tasks[number]["running"] = False
        return jsonify({"code": 200, "msg": f"手机号 {number} 任务已停止"})
    return jsonify({"code": 404, "msg": "未找到该手机号的任务"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)