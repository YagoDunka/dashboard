import asyncio
from twscrape import API
import pandas as pd
from datetime import datetime, timedelta

string_procura = ''
data = datetime.today() - timedelta(days=1)
data = data.strftime('%Y-%m-%d')
geo = '-26.9208247,-49.0666268,10km'
string_query = f'{string_procura} since:{data} geocode:{geo}'

colunas = ['id', 'date', 'place', 'rawContent']
arquivo = 'tweets.csv'

async def main():
    try:
        api = API()
        await api.pool.add_account('@SenacTeste', 'senac@123', '_', '_')
        await api.pool.login_all()

        tweets = []
        async for tweet in api.search(string_query):
            tweets.append([tweet.id, tweet.date, tweet.place, tweet.rawContent])

        df = pd.DataFrame(tweets, columns=colunas)
        df.to_csv(arquivo, header=False, index=False, mode='a')

    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    asyncio.run(main())