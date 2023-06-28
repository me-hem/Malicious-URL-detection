import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

random_seed = 42

data = pd.read_csv("MaliciousURLDataset\MaliciousURL.csv")

print(data.head)

X = data[0]
y = data[1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed, stratify=y)
