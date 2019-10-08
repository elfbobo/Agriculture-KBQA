# 查询知识图谱返回相关数据
def match_answer(slq_list, graph):
    final_answers = []
    for sql in slq_list:
        question_type = sql['question_type']
        queries = sql['sql']
        answers = []
        for query in queries:
            rsp = graph.run(query).data()
            answers += rsp
        _answer = answer_prettify(question_type, answers)
        if _answer:
            final_answers.append(_answer)
    return final_answers


# 美化生成的句子
def answer_prettify(question_type, answers):
    final_answer = []
    if question_type == 'classify_qwds':
        if answers:
            subject = answers[0]['p.name']
            desc = list(set([i['b.name'] for i in answers]))
            if len(desc) == 2:
                final_answer = '{}不仅属于{}品种，而且属于{}品种'.format(subject, desc[0], desc[1])
            elif len(desc) == 1:
                final_answer = '{0}是属于：{1}品种'.format(subject, desc[0])
            else:
                desc.insert(-1, "以及")
                final_answer = '{0}是属于：{1}品种'.format(subject, '；'.join(desc))
        else:
            final_answer = "未找到该农场品的品种类信息，换个试试？"


    elif question_type == 'person_qwds' and answers:
        if answers:
            subject = answers[0]['p.name']
            desc = list(set([i['b.name'] for i in answers]))
            if len(desc) == 1:
                final_answer = '{0}的命名者是：{1}'.format(subject, desc[0])
            else:
                desc.insert(-1, "以及")
                final_answer = '{0}的命名者是：{1}'.format(subject, '；'.join(desc))
        else:
            final_answer = "未找到该农场品的命名信息，换个试试？"

    elif question_type == 'belong_qwds':
        if answers:
            subject = answers[0]['p.name']
            desc = list(set([i['b.name'] for i in answers]))
            if len(desc) == 2:
                final_answer = '{}不仅属于:{}，而且属于:{}'.format(subject, desc[0], desc[1])
            elif len(desc) == 1:
                final_answer = '{0}是属于：{1}'.format(subject, desc[0])
            else:
                desc.insert(-1, "以及")
                final_answer = '{0}是属于：{1}'.format(subject, '；'.join(desc))
        else:
            final_answer = "未找到该农场品的门类信息，换个试试？"

    elif question_type == 'outline_qwds':
        if answers:
            subject = answers[0]['p.name']
            desc = list(set([i['b.name'] for i in answers]))
            if len(desc) == 2:
                final_answer = '{}不仅属于{}，而且属于{}'.format(subject, desc[0], desc[1])
            elif len(desc) == 1:
                final_answer = '{0}是属于：{1}'.format(subject, desc[0])
            else:
                desc.insert(-1, "以及")
                final_answer = '{0}是属于：{1}'.format(subject, '；'.join(desc))
        else:
            final_answer = "未找到该农场品的纲类信息，换个试试？"


    elif question_type == 'location_qwds':
        if answers:
            subject = answers[0]['p.name']
            desc = list(set([i['b.name'] for i in answers]))
            if len(desc) == 2:
                final_answer = '{}不仅分布于：{}，而且分布于：{}'.format(subject, desc[0], desc[1])
            elif len(desc) == 1:
                final_answer = '{0}分布于：{1}'.format(subject, desc[0])
            else:
                desc.insert(-1, "以及")
                final_answer = '{0}常分布于：{1}等地方'.format(subject, '；'.join(desc))
        else:
            final_answer = "未找到该农场品的分布信息，换个试试？"

    elif question_type == 'catalogue_qwds':
        if answers:
            subject = answers[0]['p.name']
            desc = list(set([i['b.name'] for i in answers]))
            if len(desc) == 2:
                final_answer = '{}不仅属于{}目，而且属于{}目'.format(subject, desc[0], desc[1])
            elif len(desc) == 1:
                final_answer = '{0}是属于：{1}目'.format(subject, desc[0])
            else:
                desc.insert(-1, "以及")
                final_answer = '{0}是属于：{1}目'.format(subject, '；'.join(desc))
        else:
            final_answer = "未找到该农场品的目信息，换个试试？"

    elif question_type == 'family_qwds':
        if answers:
            subject = answers[0]['p.name']
            desc = list(set([i['b.name'] for i in answers]))
            if len(desc) == 2:
                final_answer = '{}不仅属于{}，而且属于{}'.format(subject, desc[0], desc[1])
            elif len(desc) == 1:
                final_answer = '{0}是属于：{1}'.format(subject, desc[0])
            else:
                desc.insert(-1, "以及")
                final_answer = '{0}是属于：{1}'.format(subject, '；'.join(desc))
        else:
            final_answer = "未找到该农场品的科信息，换个试试？"

    elif question_type == 'not_intents':
        final_answer = '该数据没有，要不试试别的属性或者关系查询'

    elif question_type == 'not_entity':
        final_answer = '没有该农产品！'

    elif question_type == 'not_match':
        final_answer = '是不是有点超纲啦！'

    return final_answer
