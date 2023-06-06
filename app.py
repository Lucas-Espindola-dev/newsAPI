from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key='2d3163c6a3f2476c8faab0cd5d21b8ad')
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    news = []
    desc = []
    img = []

    articles = topheadlines['articles']

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(news, desc, img)

    return render_template('news.html', context=mylist)


@app.route('/cnn')
def cnn():
    newsapi = NewsApiClient(api_key='2d3163c6a3f2476c8faab0cd5d21b8ad')
    topheadlines = newsapi.get_top_headlines(sources='cnn')

    news = []
    desc = []
    img = []

    articles = topheadlines['articles']

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(news, desc, img)

    return render_template('cnn.html', context=mylist)


@app.route('/foxnews')
def foxnews():
    newsapi = NewsApiClient(api_key='2d3163c6a3f2476c8faab0cd5d21b8ad')
    topheadlines = newsapi.get_top_headlines(sources='fox-news')

    news = []
    desc = []
    img = []

    articles = topheadlines['articles']

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(news, desc, img)

    return render_template('foxnews.html', context=mylist)


@app.route('/abc')
def abc():
    newsapi = NewsApiClient(api_key='2d3163c6a3f2476c8faab0cd5d21b8ad')
    topheadlines = newsapi.get_top_headlines(sources='abc-news')

    news = []
    desc = []
    img = []

    articles = topheadlines['articles']

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(news, desc, img)

    return render_template('abc.html', context=mylist)


if __name__ == '__main__':
    app.run(debug=True)
