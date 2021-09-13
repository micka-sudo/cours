import os

# os.path.abspath(__file__) permet de récupérer un chemain absolue
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR= os.path.join(CUR_DIR, "data")