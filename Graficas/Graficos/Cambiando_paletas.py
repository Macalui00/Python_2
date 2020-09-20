import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import kdeplot
from seaborn import load_dataset

titanic = sns.load_dataset("titanic")

#Ejemplo de paleta de default:

sns.catplot(x="alive",
                col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=2.5, aspect=.8)

#Ejemplo de paleta divergente:
sns.set_palette("RdBu")
#Otros ejemplos de paletas divergentes: PRGn, RdBu_r, PRGn_r

#Otras paletas divergentes
sns.catplot(x="alive",
                 col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=2.5, aspect=.8)

#Ejemplo de paletas secuenciales: Greys, Blues, PuRd, GnBu

#Paleta customizada:
custom_palette = ["red" ,"green","orange","blue","yellow","purple"]
sns.set_palette(custom_palette)

#Otro ejemplo de paleta customizada:
custom_palette = ['#FBB4AE','#B3CDE3','#CCEBC5','#DECBE4','#FED9A6','#FFFFCC','#E5D8BD','#FDDAEC','#F2F2F2']
sns.set_palette(custom_palette)

plt.show()