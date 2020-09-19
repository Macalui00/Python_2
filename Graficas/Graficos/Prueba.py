import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import kdeplot
from seaborn import load_dataset

tips = load_dataset("tips")
tips.head()

kdeplot(data=tips, y=tips.tip, color="orange")
plt.show()