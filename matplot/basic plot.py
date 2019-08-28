import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(np.pi , -np.pi , 256 , endpoint = True)
x

s , c , z = np.sin(x) , np.cos(x) , np.tan(x)


plt.plot(x , s)


plt.plot(x , c)


plt.plot(x , z)

plt.plot(x , s)
plt.plot(x , z)
plt.show()


plt.plot(x , c)
plt.plot(x , z)
plt.show()


plt.plot(x , s)
plt.plot(x , c)
plt.plot(x , z)
plt.show()

