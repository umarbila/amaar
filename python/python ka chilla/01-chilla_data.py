# import pandas as pd
# umar = pd.read_csv("Chilla_data2_for_plots.csv")
# print(umar)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
umar = sns.load_dataset("Chilla_data2_for_plots.csv")
p = sns.countplot(x="Light kitni der band hti hy?", hue="Gender", data=umar)
print.show()