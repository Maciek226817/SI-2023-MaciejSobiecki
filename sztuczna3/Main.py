import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.linear_model import LinearRegression

# Zadanie 1 i Zadanie 2

lata = np.array([2000, 2002, 2005, 2007, 2010]).reshape((-1, 1))
procenty = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

model = LinearRegression()
model.fit(lata, procenty)

# zmieniając rok  możemy zobaczyć jak procent bezrobotnych bedzie
# w danym roku w 2023 jest to 12.118 w przyblizeniu 12
# a np. w 2020 jest to 11.376

rok = np.array([2023]).reshape((-1, 1))
przewidywany_procent = model.predict(rok)
print(f"Przewidywany procent bezrobotnych w 2023 roku: {przewidywany_procent[0]:.3f}")

a = model.coef_[0]
b = model.intercept_
print(f"Procent bezrobotnych = {a:.3f} * {rok.mean():.0f} + {b:.3f}")

# Zadanie 3
# regresja przedstawiona z a pomocą animacji

fig, ax = plt.subplots()
ax.scatter(lata, procenty)

line, = ax.plot([], [], color='r')


def update(i):
    x = lata[:i + 1]
    y = procenty[:i + 1]
    model = LinearRegression()
    model.fit(x, y)
    line.set_data(x, model.predict(x))
    ax.set_title(f"Regresja liniowa ")
    return line,


ani = FuncAnimation(fig, update, frames=range(len(lata)), blit=True, interval=500)
plt.show()
