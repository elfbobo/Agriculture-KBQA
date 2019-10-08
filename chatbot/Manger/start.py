from bulid_model import KBQA
from py2neo import Graph
import os
import json

SETTING_PATH = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]) + os.sep + "config.json"
config = json.load(open(SETTING_PATH, encoding="utf8"))
graph = Graph(host=config["host"], http_port=config["host"], user=config["host"], password=config["host"])
core = KBQA()


def run(ques):
    info = core.nlu(ques)
    answers = core.nlg(info, graph)
    return answers


if __name__ == "__main__":
    while 1:
        question = input("user(请输入你的问题)：")
        # question = "花棒属于什么科"
        answer = run(question)
        print("bot：", answer)
        if question == "break":
            print("再见！欢迎下次光临")
            break
