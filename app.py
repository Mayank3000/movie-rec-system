from flask import Flask,render_template,request,redirect,jsonify
import pickle
import requests
import pandas as pd
from patsy import dmatrices
app = Flask(__name__)

movie_list=pickle.load(open('movies_list.pkl','rb'))  
same=pickle.load(open('same.pkl','rb'))
genre_dict = pickle.load(open('genre_dict.pkl','rb'))

def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=39764d950fcb8ecbce507dd5239640b7&language=en-US".format(movie_id)
    data = requests.get(url) 
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movie_list[movie_list['title']==movie].index[0]
    dis=sorted(list(enumerate(same[index])),reverse=True,key= lambda x:x[1] )
    recommend_movie_name=[]
    recommend_movie_poster=[]
    for i in dis[1:6]:
        movie_id=movie_list.iloc[i[0]].movie_id
        recommend_movie_poster.append(get_poster(movie_id))
        recommend_movie_name.append(movie_list.iloc[i[0]].title)
    return recommend_movie_name,recommend_movie_poster

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/',methods=['GET','POST'])
def recommendation():
    movies=movie_list['title'].values
    status=False
    if request.method == 'POST':
        try: 
            if request.form:
                movie_name = request.form['movie_search']
                print(movie_name)
                recommend_movie_name,recommend_movie_poster = recommend(movie_name)
                status=True
                return render_template('recommend.html',movie_name=recommend_movie_name,poster=recommend_movie_poster,movies=movies,status=status)
        except Exception as e:
            error = {'error':str(e)}
            return render_template('recommend.html',error=error,movies=movies,status=status)    
        
    else:
        return render_template('recommend.html',movies=movies,status=status)

@app.route('/genres', methods=['GET', 'POST'])
def genre_page():
    if request.method == 'POST':
        genre_name = request.form['genre']
        movies = genre_dict.get(genre_name, [])
        return render_template('genres.html', genre=genre_name, movies=movies)
    else:
        genres = genre_dict.keys()
        return render_template('select_genre.html', genres=genres)


if __name__ == '__main__':
    app.run(debug=True,port=8000)