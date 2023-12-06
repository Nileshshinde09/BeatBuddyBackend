from csv import DictReader
import random
from imports import *
import pandas as pd
from apiHandler import ArtistImage,AlbumImage
original=pd.read_csv('data/cleaned_dataset.csv')
df= pd.read_csv('data/cleaned_dataset.csv')
def showTrending(df,w1=0.6, w2=0.3, w3=0.1):
    # df=df[df['Album']=='single']
    trendingdf=df[['Artist','Track','Album','Views','Likes','Comments']]
    # Define the function to calculate the trend score for each row
    def calculate_trend_score(row):
        return int(w1 * row['Views'] + w2 * row['Likes'] + w3 * row['Comments'])

    # Apply the function to create a new column 'Trend Score'
    trendingdf['Trend_Score'] = trendingdf.apply(calculate_trend_score, axis=1)
    newdf= trendingdf.sort_values(by='Trend_Score', ascending=False)
    return newdf

def showTopEntities(df,w1=0.6, w2=0.3, w3=0.1):
    # df=df[df['Album']=='single']
    trendingdf=df[['Artist','Track','Album','Views','Likes','Comments']]
    # Define the function to calculate the trend score for each row
    def calculate_trend_score(row):
        return int(w1 * row['Views'] + w2 * row['Likes'] + w3 * row['Comments'])

    # Apply the function to create a new column 'Trend Score'
    trendingdf['Trend_Score'] = trendingdf.apply(calculate_trend_score, axis=1)
    return trendingdf.sort_values(by='Trend_Score', ascending=False)

    
def TopArtist(changesoccurs=False):
    if changesoccurs:
        artist_dict=dict()
        newdf=showTrending(df)
        for i in newdf['Artist'].drop_duplicates().to_list()[:150]:
            if ArtistImage(i):
                artist_dict[i]=[str(ArtistImage(i))]
        resdf=pd.DataFrame(artist_dict)
        resdf.to_csv('data/trending_artist.csv') 
    else:
        with open("data/trending_artist.csv",encoding="utf8") as f:
            artists=list(DictReader(f))
            random.shuffle(artists)
            return artists
     
def TrendingArtist(changesoccurs=False):
    if changesoccurs:
        artist_dict=dict()
        newdf=showTrending(df)
        for i in newdf['Artist'].drop_duplicates().to_list()[:150]:
            if ArtistImage(i):
                artist_dict[i]=[str(ArtistImage(i))]
        resdf=pd.DataFrame(artist_dict)
        resdf.to_csv('data/trending_artist.csv') 
    else:
        with open("data/trending_artist.csv",encoding="utf8") as f:
            return list(DictReader(f))
     

def TrendingAlbum(changesoccurs=False):
    if changesoccurs:
        album_dict=dict()
        newdf=showTrending(df)
        for i in newdf['Album'].drop_duplicates().to_list()[:150]:
            if AlbumImage(i):
                album_dict[i]=[str(AlbumImage(i))]
        resdf=pd.DataFrame(album_dict)
        resdf.to_csv('data/trending_album.csv') 
    else:
        with open("data/trending_album.csv",encoding="utf8") as f:
            file=pd.read_csv(f)
            albums=file['Album'].to_list()
            original=pd.read_csv('data/cleaned_dataset.csv')
            final_dict={}
            for i,val in enumerate(albums):
                try:
                    Artist=original[original['Album']==val]['Artist'].values[0]
                    Album=val
                    Views=original[original['Album']==val]['Views'].values[0]
                    Likes=original[original['Album']==val]['Likes'].values[0]
                    Comments=original[original['Album']==val]['Comments'].values[0]
                    Licensed=original[original['Album']==val]['Licensed'].values[0]
                    Url=file[file['Album']==val]['url'].values[0]
                    Index=i
                except Exception:
                    continue
                final_dict[str(i)+"_"+val]=[val,Artist,Album,Views,Likes,Comments,Licensed,Url,Index]
            return final_dict
        
def TopAlbum(changesoccurs=False):
    if changesoccurs:
        album_dict=dict()
        newdf=showTrending(df)
        for i in newdf['Album'].drop_duplicates().to_list()[:150]:
            if AlbumImage(i):
                album_dict[i]=[str(AlbumImage(i))]
        resdf=pd.DataFrame(album_dict)
        resdf.to_csv('data/trending_album.csv') 
    else:
        with open("data/trending_album.csv",encoding="utf8") as f:
            print("Hello world")
            file=pd.read_csv(f)
            print(file)
            albums=file['Album'].to_list()
            random.shuffle(albums)
            original=pd.read_csv('data/cleaned_dataset.csv')
            final_dict={}
            for i,val in enumerate(albums):
                try:
                    Artist=original[original['Album']==val]['Artist'].values[0]
                    Album=val
                    Views=original[original['Album']==val]['Views'].values[0]
                    Likes=original[original['Album']==val]['Likes'].values[0]
                    Comments=original[original['Album']==val]['Comments'].values[0]
                    Licensed=original[original['Album']==val]['Licensed'].values[0]
                    Url=file[file['Album']==val]['url'].values[0]
                    Index=i
                except Exception:
                    continue
                final_dict[str(i)+"_"+val]=[val,Artist,Album,Views,Likes,Comments,Licensed,Url,Index]
            return final_dict

if __name__=="__main__":
    
    TrendingArtist()
    TrendingAlbum()
    TopArtist()
    TopAlbum()
