import re
import json
import os
import ahocorasick

SETTING_PATH = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]) + os.sep + "config.json"
config = json.load(open(SETTING_PATH, encoding="utf8"))


# 构建关键词库
def bulid_key_word():
    key_word_dict, key_words = dict(), []
    for file_path in config["keyword_corpus"]:
        key_class = re.compile("data/(.*?).txt").findall(file_path)
        key_data = [i.strip() for i in open(file_path) if i.strip()]
        key_words += key_data
        node_key_dict = dict(zip(key_data, key_class * len(key_data)))
        for key, value in node_key_dict.items():
            if key_word_dict.get(key):
                key_word_dict[key] += [value]
            else:
                key_word_dict[key] = [value]
    return set(key_words), key_word_dict


#  加速匹配树
def build_action_tree(word_list):
    tree = ahocorasick.Automaton()
    for index, word in enumerate(word_list):
        tree.add_word(word, (index, word))
    tree.make_automaton()
    return tree


# 合并实体类型
def check_wd_type(question, tree, wd_type_dict):
    region_wds = []
    for i in tree.iter(question):
        wd = i[1][1]
        region_wds.append(wd)
    stop_wds = []
    for wd1 in region_wds:
        for wd2 in region_wds:
            if wd1 in wd2 and wd1 != wd2:
                stop_wds.append(wd1)
    final_wds = [i for i in region_wds if i not in stop_wds]
    final_dict = {i: wd_type_dict.get(i) for i in final_wds}
    return final_dict


# 意图识别整合模块
def intent_parse():
    intent_dict = {}
    for node in config["quenstion_intention"]:
        key = list(node.values())[0]
        values = list(node.keys()) * len(key)
        for k, v in zip(key, values):
            if intent_dict.get(k):
                intent_dict[k] += [v]
            else:
                intent_dict[k] = [v]
    return intent_dict


# 意图识别模块
def check_intention(question):
    intent_dict = intent_parse()
    action_tree = build_action_tree(intent_dict.keys())
    iter_question = action_tree.iter(question)
    intents = set(sum(map(lambda x: intent_dict.get(x[1][1]), iter_question), []))
    return intents
