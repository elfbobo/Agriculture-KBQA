import os
from py2neo import Graph
import ahocorasick
import json
import os

SETTING_PATH = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2])+os.sep+"config.json"
config = json.load(open(SETTING_PATH))

