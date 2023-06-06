from newsapi import NewsApiClient
import datetime as dt


newsapi = NewsApiClient(api_key='2d3163c6a3f2476c8faab0cd5d21b8ad')

all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='globo, info-money',
                                      domains='globo.com,infomoney.com.br',
                                      from_param='2023-05-01',
                                      to='2023-05-22',
                                      language='pt',
                                      sort_by='relevancy',
                                      page_size=20,
                                      page=2)

articles = all_articles['articles']

print(articles)
