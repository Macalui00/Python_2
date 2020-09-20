import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
"""seaborn.set_color_codes
seaborn.set_color_codes(palette='deep')
Change how matplotlib color shorthands are interpreted.

Calling this will change how shorthand codes like “b” or “g” are interpreted by matplotlib in subsequent plots.

Parameters
palette{deep, muted, pastel, dark, bright, colorblind}
Named seaborn palette to use as the source of colors.
"""

# divide las diferentes barras del histograma
# sn.set(style='dark',)

#con esto podemos generar grilla y la escala de la fuente es de 1.5
# sn.set(style="whitegrid", font_scale=1.5)

#otro uso del set
# sn.set(color_codes=True)

data = np.random.randn(500)
 
plot = sn.distplot(data)
 
plt.show()

"""
Set aesthetic parameters in one step.

Each set of parameters can be set directly or temporarily, see the referenced functions below for more information.

Parameters
context : string or dict
Plotting context parameters, see plotting_context
style : string or dict
Axes style parameters, see axes_style
palette : string or sequence
Color palette, see color_palette
font : string
Font family, see matplotlib font manager.
font_scale : float, optional
Separate scaling factor to independently scale the size of the font elements.
color_codes : bool
If True and palette is a seaborn palette, remap the shorthand color codes (e.g. "b", "g", "r", etc.) to the colors from this palette.
rc : dict or None
Dictionary of rc parameter mappings to override the above.

link: https://www.kite.com/python/docs/seaborn.set"""