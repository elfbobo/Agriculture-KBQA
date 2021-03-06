# agriculture-KBQA

## 项目介绍：
    该项目是基于知识图谱的农业智能问答系统，从0到1的去搭建一个以农场品为中心的知识图谱，面向的用户群体是：农民和普通民众。

## 项目目的：    
1. 对农民而言让他了解某些农场品的种植方式，基本属性，种植成本，经济效益等等。
2. 对普通群众而言让他了解这些农产品的作用（健康方面），以及各种植物之间的关系起到科普的作用。

## 项目结果展示：

### 操作说明
![](https://raw.githubusercontent.com/Crawler-y/Agriculture-KBQA/master/tool/guide.png)

### 图谱展示
![](https://raw.githubusercontent.com/Crawler-y/Agriculture-KBQA/master/tool/show.png)

### 对话展示部分
![](https://raw.githubusercontent.com/Crawler-y/Agriculture-KBQA/master/tool/chatbot.png)

## 项目结构：
```
.
├── hudongbaike     // scrapy爬虫项目路径
│   └── hudongbaike
│       └── spiders
│          └── bk.py  //爬取搜索词
│          └── bkc.py  //带入搜索词爬取内容
├── data   // 数据存放路径
│   └── query_list.csv //存放搜索词文件
│   └── *.txt //存放关键词文件
├── data_processing    // 数据清洗
│   └── build_kg.ipynb //数据处理入库
├── model    // 算法存放路径
├── chatbot    // 问答机器人模块
│   └── Manger//调度模块
│          └── start.py//主程序
│   └── NLG //数据生成模块
│   └── NLU //意图识别和实体识别模块
│   └── config.json //配置信息
│   └── question_processing.ipynb //历史测试文件
├── tool    // 存放图片和文档说明
```

## 项目运行方式：
    敬请期待！！！
    （pass）
  
# 技术点说明：

* 知识图谱部分说明：

### 命名实体的分类：
| 实体类型	    | 中文含义                                 | 举个例子                                  |
| ---------    | ---------------------------------------- | ---------------------------------------- |
| Produce      | 农场品名称                                |  蛇果，牛油果，雪梨，芝麻，菠萝             |
| Person       | 人物名称                                 | 袁隆平，习近平，Kotschy                     |
| Location     | 区域                                    | 福建省，三明市，云南，元江                   |
| Belong       | 门                                      | 被子植物门，绿藻门，蕨类植物门               |
| Outline      | 纲                                      | 单子叶植物纲，双子叶植物纲                   |
| Catalogue    | 目                                      | 蔷薇目，粉状胚乳目，山龙眼目                 |
| Family       | 科                                      | 蔷薇科，莲科，凤梨科                        |
| Classify     | 品种                                    | 苹果，梨，藕                               |
| Manure       | 肥料                                    | 尿素，钾肥，碳酸                            |
| Climate      | 气候                                    | 气温，水分，关照（需要分箱）                 |
| Diseases     | 病虫害                                  | 褐腐病，晚疫病，莲藕黑斑病                   |
| Nutrients    | 营养素                                  | 维生素A，蛋白质，钙                         |
| Illness      | 疾病（人类）                             | 糖尿病，宫颈癌，青光眼                      |
| Ability      | 功效                                    | 降火，化咳止痰，美容，丰胸                   |

### 实体关系的分类：
| 关系类型	    | 中文含义                                 | 举个例子                                  |
| ---------    | ---------------------------------------- | ---------------------------------------- |
| part_of         | 农产品属于                                | <蛇果> 属于 <蔷薇目>                      |
| have_ nutrition| 农村品拥有营养元素                       | <蛇果> 营养成分 <碳水化合物><维生素C><锰>  |
| distribute   | 农产品分布于                              | <蛇果> 分布区域是 <美国>                   |
| give_name    | 农产品命名                                | <“kotschy”> 是第一个命名 <牛油果> 的人      |
| fertilization| 农村品施肥                                | <蛇果> 追施 <三元复合肥>                   |
| beneficial_envi | 农村品有利生长环境                      | <莲藕> 喜 <温暖（20-30℃）>                |
| fall_ill     | 农村品易得病虫害                           | <蛇果> 病害有 <腐烂病>                     |
| prevent_disease   | 农村品疾病预防                        |  <蛇果> 具有 <抗癌>  的功效                |
| health_help   | 农村品健康助力                            | <蛇果>  具有 <帮助消化> 等功效              |

* 问答系统说明：

### 语义匹配部分：
    敬请期待！！！
    （pass）

### 信息检索部分：
    敬请期待！！！
    （pass）