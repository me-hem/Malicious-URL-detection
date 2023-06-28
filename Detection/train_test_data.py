# Consider this file for Using data set so that we all are working on same training and test data.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

random_seed = 42

data = pd.read_csv("MaliciousURLDataset\MaliciousURL.csv")

df = pd.DataFrame(data)
X = df.iloc[:,0]
y = df.iloc[:,1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed, stratify=y)
