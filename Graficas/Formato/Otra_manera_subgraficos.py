import numpy as np
import matplotlib.pyplot as plt

for k in [1,2,3,4] :
    plt.subplot(2,2,k)

x = np.arange(1, 11)
y = np.random.randint(10, size=10)

plt.subplot(2,2,3)
plt.plot(x,y)
plt.title('Tercer Subplot')
plt.tight_layout() 

plt.show()