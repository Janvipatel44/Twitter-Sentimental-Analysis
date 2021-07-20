import io
import boto3
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import json

# References:    #https://towardsdatascience.com/finding-and-removing-duplicate-rows-in-pandas-dataframe-c6117668631f
# https://towardsdatascience.com/categorical-encoding-using-label-encoding-and-one-hot-encoder-911ef77fb5bd
# https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html
# https://stackoverflow.com/questions/55291667/getting-typeerror-slicenone-none-none-0-is-an-invalid-key
# https://dzone.com/articles/kmeans-silhouette-score-explained-with-python-exam
# https://matplotlib.org/stable/tutorials/colors/colors.html


def clean_data(X):
    # record columns to delete
    X.dropna()

    # duplicate rows removal
    X.drop_duplicates(inplace=True)
    return X


def label_encoder(X):
    # creating instance of label encoder
    labelencoder = LabelEncoder()
    # Assigning numerical values and storing in another column
    X['Current_Word'] = labelencoder.fit_transform(X['Current_Word'])
    X['Next_Word'] = labelencoder.fit_transform(X['Next_Word'])
    return X


def model_train(train_data):
    # https://towardsdatascience.com/machine-learning-algorithms-part-9-k-means-example-in-python-f2ad05ed5203#:~:text=K%2DMeans%20Clustering%20is%20an,been%20trained%20with%20labeled%20data.&text=The%20real%20world%20applications%20of,market%20segmentation
    wcss = []
    for i in range(2, 10):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(train_data)
        wcss.append(kmeans.inertia_)
    return kmeans


def cluster_prediction(data, kmeans):
    # Y label
    clusterNo = kmeans.predict(data)
    data = pd.DataFrame(data)
    data['clusterNo'] = pd.DataFrame(clusterNo)
    data = data.replace(np.nan, 0)
    return data


def cluster_evaluation(data, kmeans):
    # Silhouette Score calculation
    score = silhouette_score(data, kmeans.labels_, metric='euclidean')
    print('Silhouette Score: %.3f' % score)

    # Centroid cluster
    cent = kmeans.cluster_centers_
    print('Centroid of Cluster', cent)


def display_clusters(data, train):
    # Plotting the cluster
    clusterCount = data['clusterNo'].nunique()
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22',
              '#FFFF00', '#4B0082']
    for i in range(0, clusterCount):
        plt.scatter(data[data['clusterNo'] == i].iloc[:, 0], data[data['clusterNo'] == i].iloc[:, 1], color=colors[i])
    plt.xlabel('PC 1')
    plt.ylabel('PC 2')
    if (train == True):
        plt.title('Cluster plot on training data')
    else:
        plt.title('Cluster plot on testing data')
    plt.show()


def lambda_handler(event, context):

    s3_bucket_name = "traindatab00863421"
    filename = "trainVector.csv"
    s3 = boto3.client('s3')
    train_data = s3.get_object(Bucket=s3_bucket_name, Key=filename)
    train_data = train_data['Body'].read()
    train_data = pd.read_csv(io.BytesIO(train_data), header=0, delimiter=",", low_memory=False)
    train_data = clean_data(train_data)
    train_data = label_encoder(train_data)
    pca = PCA(2)
    train_data = pca.fit_transform(train_data)
    kmeans = model_train(train_data)
    train_data = cluster_prediction(train_data, kmeans)
    print(train_data)
    cluster_evaluation(train_data, kmeans)
    display_clusters(train_data, True)

    s3_bucket_name = "testdatab00863421"
    filename = "testVector.csv"
    test_data = s3.get_object(Bucket=s3_bucket_name, Key=filename)
    test_data = test_data['Body'].read()
    test_data = pd.read_csv(io.BytesIO(test_data), header=0, delimiter=",", low_memory=False)
    test_data = clean_data(test_data)
    test_data = label_encoder(test_data)
    pca = PCA(2)
    test_data = pca.fit_transform(test_data)
    test_data = cluster_prediction(test_data, kmeans)
    print(test_data)
    display_clusters(test_data, False)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }