import pandas as pd
from sklearn import datasets
import seaborn as sns

import matplotlib.pyplot as plt
iris = datasets.load_iris()
iris_df=pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df.loc[:, "species_label"] = iris.target
sns.lmplot('sepal length (cm)','petal width (cm)',data=iris_df,fit_reg=True,hue='species_label')
plt.show()
