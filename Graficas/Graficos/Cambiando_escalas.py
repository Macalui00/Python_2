import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import kdeplot
from seaborn import load_dataset

titanic = sns.load_dataset("titanic")

sns.set(rc={'axes.facecolor':'white', 'axes.labelcolor':'.15', 'figure.facecolor':'black', 'patch.edgecolor':'k'})

"""Figure "context" changes the scale ofthe plot elements and labels
sns.set_context()
Smallest to largest:"paper","notebook","talk",'poster'"""

sns.set_context("paper")
sns.catplot(x="alive",
                col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=2.5, aspect=.8)

sns.set_context("notebook")
sns.catplot(x="alive",
                col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=2.5, aspect=.8)

sns.set_context("talk")
sns.catplot(x="alive",
                col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=2.5, aspect=.8)

sns.set_context("poster")
sns.catplot(x="alive",
                col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=2.5, aspect=.8)

#Ajustar el tamaño de la ventana al grafico
plt.figure(1).tight_layout()
plt.figure(2).tight_layout()
plt.figure(3).tight_layout()
plt.figure(4).tight_layout()

plt.show()

#https://s3.amazonaws.com/assets.datacamp.com/production/course_15192/slides/chapter4.pdf