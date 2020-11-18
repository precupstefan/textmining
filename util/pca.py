import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np


def determine_best_number_of_components(dataframe: pd.DataFrame):
    pca = PCA(n_components=0.95, svd_solver="full").fit(dataframe)
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.plot(pca.explained_variance_ratio_)
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance');
    plt.show()
    1 == 1


def apply_PCA(dataframe: pd.DataFrame):
    pca = PCA(n_components=0.99, svd_solver="full").fit_transform(dataframe)
    return pca


def build_pca_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    # TODO: should we scale data?
    pca_array = apply_PCA(dataframe)
    columns = ['component' + str(i) for i in range(pca_array.shape[1])]
    return pd.DataFrame(pca_array, columns=columns)
