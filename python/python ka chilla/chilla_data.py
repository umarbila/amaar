import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

umar = sns.load_dataset("Chilla_data2_for_plots.csv")
sns.barplot(x="Age", y="Gender", hue="Duration", data=umar)
plt.show()
# import pandas as pd
# df = pd.read_csv("data_viz.csv")
# print(df) 
# import seaborn as sns
# import matplotlib.pyplot as plt 
# phool = sns.load_dataset("titanic")
# sns.boxplot(x="sex", y="age", hue="class", data=phool)
# plt.show()






