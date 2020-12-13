import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


gamma1 = 0.1
gamma2 = -0.1
omega_0 = 1
beta = 2


def f(y, t):   # отсутствие колебаний
                y1, y2 = y
                return [y2, (-gamma1-(y1**2) * beta)*y2 - omega_0 * y1]


def f_1(y, t):   # автоколебания
                y1, y2 = y
                return [y2, (-gamma2-(y1**2) * beta)*y2 - omega_0 * y1]


t = np.linspace(0, 200, 1000)
y0 = [0.0001, 0.0001]
[y1, y2] = odeint(f, y0, t).T

plt.subplot(221)
plt.plot(y1, y2, linewidth=2)
plt.grid(True)

plt.subplot(222)
plt.plot(t, y1, linewidth=2, label='Автоколебания  \n квазигармонические')
plt.legend(loc='best')
plt.grid(True)


t = np.linspace(0, 200, 1000)
y0 = [0.0001, 0.0001]
[y1, y2] = odeint(f_1, y0, t).T

plt.subplot(223)
plt.plot(y1, y2, linewidth=2)
plt.grid(True)

plt.subplot(224)
plt.plot(t, y1, linewidth=2, label='Автоколебания \n затухающие')
plt.legend(loc='best')
plt.grid(True)
plt.show()
