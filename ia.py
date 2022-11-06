from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib
from sklearn.ensemble import RandomForestClassifier # Algoritmo Random Forest
from sklearn.metrics import r2_score # Utilizado para medir a acuracia do modelo preditivo
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder # Utilizado para fazer o OneHotEncoding

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
        array = [0.5       , 0.82608696, 0.        , 0.        , 1.        ,
        1.        , 0.        , 0.        , 0.        , 0.09859155,
        0.        , 0.1039604 , 0.        , 0.        , 0.93023256]
        ia = joblib.load('emprestimo.pkl')
        #resultado = ia.predict([])
        return request.json
if __name__ == '__main__': 
  app.run()