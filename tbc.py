#-*-coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
x = np.linspace(0,1000000,1000)
y = 0.3*x

plt.plot(x,y,color = "red")
plt.xlabel("xiaoshoue")
plt.ylabel("jinglirun")

plt.show()
