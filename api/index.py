from flask import Flask, jsonify, request
from flask_cors import CORS
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd
import numpy as np

import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def sem_uso():
    return "não usamos essa rota"
@app.route('/', methods=['POST'])
def ia():
    if request.json == None or request.json == False:
        return 'Não há nehum parâmetro. Por favor envie a descriçaõ da imagem'
    else:
        dados = np.array([request.json['dados']])
        dados_array = pd.DataFrame(dados, columns=["UF","IDADE","ESCOLARIDADE","ESTADO_CIVIL","QT_FILHOS",
        "CASA_PROPRIA","QT_IMOVEIS","VL_IMOVEIS","OUTRA_RENDA_VALOR",
        "TEMPO_ULTIMO_EMPREGO_MESES","TRABALHANDO_ATUALMENTE","ULTIMO_SALARIO",
        "QT_CARROS","VALOR_TABELA_CARROS","SCORE_CREDITO",])
        ia = joblib.load(os.path.join(os.getcwd(),"api/emprestimo.pkl"))
        resultado = ia.predict(dados_array)
        print(resultado[0])
        return resultado[0]
if __name__ == '__main__': 
  app.run()
