# Librerías
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
 
# Datos
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
 
# Temas: darkgrid, whitegrid, dark, white, and ticks
plt.figure(figsize=(5,5))
sns.set_style("whitegrid")
sns.boxplot(data=data)
plt.title("whitegrid")

plt.figure(figsize=(5,5)) 
sns.set_style("darkgrid")
sns.boxplot(data=data)
plt.title("darkgrid")

plt.figure(figsize=(5,5))
sns.set_style("white")
sns.boxplot(data=data)
plt.title("white")

plt.figure(figsize=(5,5))
sns.set_style("dark")
sns.boxplot(data=data)
plt.title("dark")

plt.figure(figsize=(5,5))
sns.set_style("ticks")
sns.boxplot(data=data)
plt.title("ticks")

plt.show()
#https://python-graph-gallery.com/104-seaborn-themes/