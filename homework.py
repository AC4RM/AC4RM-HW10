from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd


def register_student(first_name, last_name, *args, **kwargs):
    pass


sql_query_1 = '''

              '''

sql_query_2 = '''

              '''


def train_model():
    cancer = load_breast_cancer()
    df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    pca = PCA(n_components = 0.95)
    pca.fit(scaled_data)
    x_pca = pca.transform(scaled_data)

    # Your code here


regex_pattern = ""
