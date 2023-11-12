import requests
from bs4 import BeautifulSoup 
from io import StringIO
import pandas as pd

url = 'https://www.alertablu.sc.gov.br/d/'
colunas = ['Estação', 'Hora da Leitura', '24h', '168h']
arquivo = 'alertablu.csv'

def main():
    try:
        response = requests.get(url, verify=False)
        response.rause_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        table = StringIO(str(table))

        df = pd.read_html(table, thousands='.', decimal=',')[0]
        df = df[colunas]
        df.to_csv(arquivo, header=False, index=False, mode='a')

    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    main()