import re

tags = ['chuva',
       'enchente',
       'alagou',
       'alaga',
       'temporal',
       'chov',
       'rio cheio',
       'diluvio',
       'inund',
       'enxurrada']

def text_cleaning(text):
    """
    Função para apliação de diferentes filtros para a limpeza de um texto

    Parâmetros:
        text (str): texto para aplicação dos filtros

    Retorna:
        str: texto filtrado
    """
    text = re.sub(r'@[A-Za-z0-9$-_@.&+]+', ' ', str(text)) # usernames
    text = re.sub(r'https?://[A-Za-z0-9./]+', ' ', text) # urls
    text = text.replace('RT', ' ') # marcas de retweet
    text = text.replace('\n', ' ') # marcas de line-feed

    return text

def conta_palavras(group, tags=tags):
    counts = 0
    for tag in tags:
        counts += sum(group.str.lower().str.contains(tag))
    return counts