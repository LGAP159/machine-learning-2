from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import kagglehub

path = kagglehub.dataset_download("mysarahmadbhat/lung-cancer")
print("Path to dataset files:", path)
