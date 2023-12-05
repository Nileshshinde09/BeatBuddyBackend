from recommendSongs import *
from flask import Flask,request,jsonify
from apiHandler import *
from getInfo import *
from trending import *
import mongodb

app= Flask(__name__)

# mongodb.connect()


@app.route('/',methods=['GET'])
def home():
    return 'hello world'

@app.route('/api/v1/availableName',methods=['GET'])
def songAvailable():
    if request.method == 'GET':
        response = jsonify(nameforRecommendation())
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

@app.route('/api/v1/recommendSongs',methods=['GET'])
def recommendSongs():
    songname = request.args.get('songname')
    if request.method == 'GET':
        if songname:
            response = jsonify(recommend_song(songname.strip()))
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response

@app.route('/api/v1/ArtistTopTracks',methods=['GET'])
def topTracks():
    name=request.args.get('name')
    if request.method == 'GET':
        response = jsonify(ArtistTopTracks(name))
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
@app.route('/api/v1/ArtistImage',methods=['GET'])
def artistImage():
    artistname = request.args.get('artistname')
    if request.method == 'GET':
        if artistname:
            response = jsonify(ArtistImage(artistname))
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response
@app.route('/api/v1/AlbumImage',methods=['GET'])
def getAlbumImage():
    albumname = request.args.get('albumname')
    if request.method == 'GET':
        if albumname:
            response = jsonify(AlbumImage(albumname))
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response
@app.route('/api/v1/ArtistNameToId',methods=['GET'])
def getID():
    artistname = request.args.get('artistname')
    if request.method == 'GET':
        if artistname:
            response = jsonify(NameToId(artistname))
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response
        
@app.route('/api/v1/getSocialMedia',methods=['GET'])
def socialMedia():
    artistname = request.args.get('artistname')
    if request.method == 'GET':
        if artistname:
            response = jsonify(getSocialMedia(artistname))
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response
        
@app.route('/api/v1/getDesc',methods=['GET'])
def Desc():
    name = request.args.get('name')
    if request.method == 'GET':
        if name:
            response = jsonify(getDesc(name))
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response

@app.route('/api/v1/getUrl',methods=['GET'])
def Url():
    name = request.args.get('name')
    if request.method == 'GET':
        if name:
            response = jsonify(getUrl(name))
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response
        
@app.route('/api/v1/getTrendingArtist',methods=['GET'])
def trendingArtist():
    if request.method == 'GET':
        response = jsonify(TrendingArtist())
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

@app.route('/api/v1/getTopArtist',methods=['GET'])
def topArtist():
    if request.method == 'GET':
        response = jsonify(TopArtist())
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
    

@app.route('/api/v1/getTrendingAlbum',methods=['GET'])
def trendingAlbum():
    if request.method == 'GET':
        response = jsonify(TrendingAlbum())
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
    
@app.route('/api/v1/getTopAlbum',methods=['GET'])
def topAlbum():
    if request.method == 'GET':
        response = jsonify(TopAlbum())
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
                             
#if __name__=="__main__":
#    app.run(debug=True)
