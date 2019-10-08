import os
from py2neo import Graph
from 知识图谱.Agriculture_KBQA.chatbot.NLU import bulid_corpus
from 知识图谱.Agriculture_KBQA.chatbot.NLG import template
from 知识图谱.Agriculture_KBQA.chatbot.NLG import generate


class KBQA(object):

    def nlu(self, question):
        """
        parse user input question
        :param question: User input
        :return: json data : extract question entity and intention
        """
        key_list, key_word_dict = bulid_corpus.bulid_key_word()
        action_tree = bulid_corpus.build_action_tree(key_list)
        final_dict = bulid_corpus.check_wd_type(question, action_tree, key_word_dict)
        question_type = bulid_corpus.check_intention(question)
        # 假设无实体类型，无意图实现自动跳转
        #####################################
        if final_dict and question_type:
            info = {"entity": final_dict, "intents": question_type}
        elif final_dict and not question_type:
            info = {"entity": final_dict, "intents": {"not_intents"}}
        elif not final_dict and question_type:
            info = {"entity": {}, "intents": {"not_entity"}}
        else:
            info = {"entity": {}, "intents": {"not_match"}}
        print("nlu part rturn data:",info)
        return info

    def nlg(self, info, graph):
        """
        generation bot answer
        :param info:  json data contains question entity and intention
        :return: natural statement
        """
        slq_list = generate.info_tans(info)
        print("nlg part generation sql:", slq_list)
        final_answers = template.match_answer(slq_list, graph)
        return final_answers


