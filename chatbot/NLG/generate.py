# 实体和实体类型转置
def entity_type_func(entity_list):
    entity_type_dict = {}
    for entity, types in entity_list.items():
        for t in types:
            if t not in entity_type_dict:
                entity_type_dict[t] = [entity]
            else:
                entity_type_dict[t].append(entity)
    return entity_type_dict


# sql语句转换
def info_tans(info):
    entity_type_dict = entity_type_func(info["entity"])
    sql_list = []
    for intention in info["intents"]:
        sql, sql_dict = [], dict()
        sql_dict['question_type'] = intention
        if intention == "classify_qwds" and "produce" in entity_type_dict:
            sql = [
                "match(p:Produce),(b:Classify) where p.name='{0}' match n =((p)-[:part_of]-(b)) return p.name,b.name".format(
                    i) for i in entity_type_dict.get("produce")
            ]
        elif intention == "person_qwds" and "produce" in entity_type_dict:
            sql = [
                "match(p:Produce),(b:Person) where p.name='{0}' match n =((p)-[:give_name]-(b)) return p.name,b.name".format(
                    i) for i in entity_type_dict.get("produce")
            ]
        elif intention == "belong_qwds" and "produce" in entity_type_dict:
            sql = [
                "match(p:Produce),(b:Belong) where p.name='{0}' match n =((p)-[:part_of]-(b)) return p.name,b.name".format(
                    i) for i in entity_type_dict.get("produce")
            ]
        elif intention == "outline_qwds" and "produce" in entity_type_dict:
            sql = [
                "match(p:Produce),(b:Outline) where p.name='{0}' match n =((p)-[:part_of]-(b)) return p.name,b.name".format(
                    i) for i in entity_type_dict.get("produce")
            ]
        elif intention == "location_qwds" and "produce" in entity_type_dict:
            sql = [
                "match(p:Produce),(b:Location) where p.name='{0}' match n =((p)-[:distribute]-(b)) return p.name,b.name".format(
                    i) for i in entity_type_dict.get("produce")
            ]
        elif intention == "catalogue_qwds" and "produce" in entity_type_dict:
            sql = [
                "match(p:Produce),(b:Catalogue) where p.name='{0}' match n =((p)-[:part_of]-(b)) return p.name,b.name".format(
                    i) for i in entity_type_dict.get("produce")
            ]
        elif intention == "family_qwds" and "produce" in entity_type_dict:
            sql = [
                "match(p:Produce),(b:Family) where p.name='{0}' match n =((p)-[:part_of]-(b)) return p.name,b.name".format(
                    i) for i in entity_type_dict.get("produce")
            ]
        sql_dict['sql'] = sql
        sql_list.append(sql_dict)
    return sql_list
