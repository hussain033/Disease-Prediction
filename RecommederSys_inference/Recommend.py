import pandas as pd
import sklearn
import pickle as pk

with open('diseaseClass.pickle', 'rb') as f:
    model = pk.load(f)

df = pd.read_csv("../Datasets/RecommenderSys_Training.csv")

def Recommender(symptom):
    index = df.index.get_loc(symptom)
    distances, indices = knn.kneighbors(df.iloc[index,:].values.reshape(1,-1), n_neighbors=15)
    movie = []
    distance = []

    for i in range(0, len(distances.flatten())):
        if i != 0:
            movie.append(df.index[indices.flatten()[i]])
            distance.append(distances.flatten()[i])    

    m=pd.Series(movie,name='symptom')
    d=pd.Series(distance,name='distance')
    recommend = pd.concat([m,d], axis=1)
    recommend = recommend.sort_values('distance',ascending=True)

    print('Recommendations for {0}:\n'.format(df.index[index]))
    for i in range(0,recommend.shape[0]):
        print('{0}: {1}, with distance of {2}'.format(i+1, recommend["symptom"].iloc[i], recommend["distance"].iloc[i]))
    
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage: python3 Recommend.py 'input'")
    else:
        symptom = sys.argv[1]
        Recommender(symptom)
