from imports import *
from apiHandler import AlbumImage
# settings
pd.set_option(
    'display.max_columns',None
    ,'display.max_colwidth', None
)
# load data
CSV = 'data/cleaned_dataset.csv'
df = pd.read_csv(CSV)

# change column name to lowercase
df.columns = ['_'.join(c.split(' ')).lower() for c in df.columns]


# filtering on 
# album_type = single & 
# licensed = True 
# most_playedon = Spotify
# (save memory consumption)
df = df[(df['album_type'] == 'single') & (df['licensed'] == 'True') & (df['most_playedon'] == 'Spotify')]


# filtering columns
wanted = ['title','danceability','energy','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_min','stream', 'energyliveness']
df = df[wanted]



# reset index
df.reset_index(drop=True, inplace=True)


# customer class to extract numerical features only
class ExtractFeatures(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        df_feat = X.select_dtypes(np.float64)
        return df_feat
    
    
# build a pipeline
pipe = Pipeline (steps=[
                        ("extract_feat", ExtractFeatures()),    # extract numerical features
                        ("scale", MinMaxScaler()),              # scale the data
                        ])

# params
# name = np.random.choice(df.title)
indices = pd.Series(df.index, index=df['title']).drop_duplicates()
df_scaled = pipe.fit_transform(df)
n = 200
recom_songs = []


def generate_recommendation(song_title, model_type=None, num=None, model_name=None):
    """
    Purpose: Function for song recommendations 
    Inputs: random song title, type of similarity model & n recommendations
    Output: list of top n recommended songs
    """
    # Create a list with model name
    top_songs_list = [model_name, song_title]
    
    # Get song indices
    index = indices[song_title]
    
    # Get list of songs for given song
    score = model_type[index, :].tolist()
        
    # Sort the most similar songs
    similarity_score = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

    # score=list(enumerate(model_type[indices[song_title]]))
    
    # # Sort the most similar songs
    # similarity_score = sorted(score,key = lambda x:x[1],reverse = True)

    
    # Select the top-n recommend songs
    similarity_score = similarity_score[:num]
    top_songs_index = [i[0] for i in similarity_score]
    
    # Top n recommended songs
    top_songs = df['title'].iloc[top_songs_index]
    top_songs_list.extend(top_songs.to_list())
    top_songs_list = top_songs_list[1:]

    return top_songs_list


def recommend_song(name):
    # df = df[(df['album_type'] == 'single') & (df['licensed'] == 'True') & (df['most_playedon'] == 'Spotify')]

    # Model Type: Cosine Similarity 
    try:
        cosine = cosine_similarity(df_scaled)
        q_name = cosine_similarity.__qualname__
        recom_songs.append(generate_recommendation(name, model_type=cosine, num=n, model_name=q_name))
    
        # Model Type: Sigmoid Kernel
        # sig_kernel = sigmoid_kernel(df_scaled)
        # q_name = sigmoid_kernel.__qualname__
        # recom_songs.append(generate_recommendation(name, model_type=sig_kernel, num=n, model_name=q_name))

        # # Model Type: Manhattan Distance
        # man_dist = manhattan_distances(df_scaled)
        # q_name = manhattan_distances.__qualname__
        # recom_songs.append(generate_recommendation(name, model_type=man_dist, num=n, model_name=q_name))


    
        # # Model Type: Additive Chi2 kernel
        # ack = additive_chi2_kernel(df_scaled)
        # q_name = additive_chi2_kernel.__qualname__
        # recom_songs.append(generate_recommendation(name, model_type=ack, num=n, model_name=q_name))


        # # Model Type: Chi2 Kernel
        # c2 = chi2_kernel(df_scaled)
        # q_name = chi2_kernel.__qualname__
        # recom_songs.append(generate_recommendation(name, model_type=c2, num=n, model_name=q_name))


        # # Model Type: Euclidean Distance
        # ed = euclidean_distances(df_scaled)
        # q_name = euclidean_distances.__qualname__
        # recom_songs.append(generate_recommendation(name, model_type=ed, num=n, model_name=q_name))

        # # Model Type: Laplacian Kernel
        # lk = laplacian_kernel(df_scaled)
        # q_name = laplacian_kernel.__qualname__
        # recom_songs.append(generate_recommendation(name, model_type=lk, num=n, model_name=q_name))

        # # Model Type: Linear Kernel
        # lin_k = linear_kernel(df_scaled)
        # q_name = linear_kernel.__qualname__
        # recom_songs.append(generate_recommendation(name, model_type=lin_k, num=n, model_name=q_name))
   
        # # Model Type: Polynomial Kernel
        # pk = polynomial_kernel(df_scaled)
        # q_name = polynomial_kernel.__qualname__
        # recom_songs.append(generate_recommendation(name, model_type=pk, num=n, model_name=q_name))

        # # Model Type: RBF Kernel
        # rk = rbf_kernel(df_scaled)
        # q_name = rbf_kernel.__qualname__
        # recom_songs.append(generate_recommendation(name, model_type=rk, num=n, model_name=q_name))
    except Exception :
        return []

    final_list=set()
    original=pd.read_csv('data/cleaned_dataset.csv')
    final_dict={}
    for songs in recom_songs:
        for i in songs:
            final_list.add(i)
    print(final_list) 
    for i in list(final_list):
        Artist=original[original['Title']==i]['Artist'].values[0]
        Album=original[original['Title']==i]['Album'].values[0]
        Views=original[original['Title']==i]['Views'].values[0]
        Likes=original[original['Title']==i]['Likes'].values[0]
        Comments=original[original['Title']==i]['Comments'].values[0]
        Licensed=original[original['Title']==i]['Licensed'].values[0]
        Url=AlbumImage(Album)
        final_dict[i]=[i,Artist,Album,Views,Likes,Comments,Licensed,Url]
    return final_dict

def nameforRecommendation():
    df= pd.read_csv('data/cleaned_dataset.csv')
    df.columns = ['_'.join(c.split(' ')).lower() for c in df.columns]
    df = df[(df['album_type'] == 'single') & (df['licensed'] == 'True') & (df['most_playedon'] == 'Spotify')]
    return list(df.title)


if __name__=="__main__":
    # print(len(recommend_song('Gorillaz - New Gold ft. Tame Impala & Bootie Brown (Official Visualiser)')))
    nameforRecommendation()
    recommend_song()
# {'Gorillaz - New Gold ft. Tame Impala & Bootie Brown (Official Visualiser)': ['Gorillaz', 'New Gold (feat. Tame Impala and Bootie Brown)', 8435055.0, 282142.0, 7399.0, 'True', 'https://i.scdn.co/image/ab67616d0000b273fda889bb57058a4a1b88edcd'], 'Tiësto & Charli XCX - Hot In It [Official Music Video]': ['Tiësto', 'Hot In It', 5891427.0, 96134.0, 2236.0, 'True', 'https://i.scdn.co/image/ab67616d0000b273029756c183a335434b7fd449'], 'Sean Paul, J Balvin - Contra La Pared': ['Sean Paul', 'Contra La Pared', 256405663.0, 1928933.0, 20224.0, 'True', 'https://i.scdn.co/image/ab67616d0000b27335a8918b4f284fed70a8e423'], 'Gorillaz - Cracker Island ft. Thundercat (Official Video)': ['Gorillaz', 'Cracker Island (feat. Thundercat)', 24459820.0, 739527.0, 20296.0, 'True', 'https://i.scdn.co/image/ab67616d0000b273efbba3463588a325949874d5']}
