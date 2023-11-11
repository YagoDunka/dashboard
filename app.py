from flask import Flask
import numpy as np

app = Flask(__name__)

lista = np.array([1, 4, 7, 10, 34, 23, 4, 6, 2])

idx = np.where(lista < 7)

@app.route('/')

def home():
    return str(lista[idx])

if __name__ == '__main__':
    app.run()