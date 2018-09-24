from flask import Flask, url_for, redirect
from flask import render_template
from flask import request
import os
from flask import json
from flask import jsonify
from flask import Response
import urllib2
import sqlite3 as sql
from flask import g
from cgi import parse_qs, escape

import tmdbsimple as tmdb

tmdb.API_KEY = '30dae1d722bd468f31399114d91007bc'


GenreList = {'Comedy': 35, 
'Action': 28, 
'Thriller': 53, 
'Science Fiction': 878,
'Drama':18,
'Horror':30,
'Fantasy':30,
'Animation':16,
'Family':10751}



app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    user = {'nickname': 'dannySky10'}
    return render_template('index.html',title='ChillTime',user = user)


# http requests from The Movie Database, returning JSON data

@app.route("/findTitle/<string:data>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def echo_title(data):
    if request.method == 'GET':
        movies = search_movie(data)
        return jsonify({"data": movies})

@app.route("/findTvTitle/<string:data>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def echo_TVTitle(data):
    if request.method == 'GET':
        tv = search_tv(data)
        return jsonify({"data": tv})


@app.route("/findGenre/<int:page>/<string:data>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def echo_genre(page, data):
    if request.method == 'GET':
        movies = search_genre(page, data)
        return jsonify({"data": movies})


@app.route("/findTvGenre/<int:page>/<string:data>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def echo_TvGenre(page, data):
    if request.method == 'GET':
        tv = search_TvGenre(page, data)
        return jsonify({"data": tv})
     



def search_genre(page, data):
    movieList = []
    genre = tmdb.Genres(id=GenreList[data])
    movies = genre.movies(page= page+1)
    for s in movies["results"]:
        movieList.append(s)
        
    return movieList

def search_movie(data):
    search = tmdb.Search()
    response = search.movie(query= data)
    movieList = []
    totalPages = 2

    for s in search.results:
        movieList.append(s)

        
    return movieList

def search_tv(data):
    search = tmdb.Search()
    response = search.tv(query=data)
    tvList = []
    totalPages = 2

    for s in search.results:
        tvList.append(s) 

    return tvList

def search_TvGenre(page,data):
    tvList = []
    genre = tmdb.Genres(id=GenreList[data])
    tv = genre.tv(page= page+1)

    for s in tv["results"]:
        tvList.append(s)

        return tvList



with app.test_request_context():
    print url_for('static', filename='style.css')
    print url_for('static', filename='cover.css')
    print url_for('index')



if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)