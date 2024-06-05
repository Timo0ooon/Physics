import math
import matplotlib.pyplot as plt


def xt(m, u, k, t):
    return (m*u/k)*(1-math.exp(-k*t/m))


def yt(r, g, v, m, k, t, H):
    return (((r*g*v-m*g)/k) * (t + m/k * (math.exp(-k*t/m) - 1))) - H


def main():
    r = 1000
    u = 100
    g = 9.8
    v = 20_000
    m = 18_700_000
    k = 10
    H = 300

    t0 = 0
    delta_t = 0.1
    y = []
    x = []

    while yt(r, g, v, m, k, t0, H) <= 0:
        y.append(yt(r, g, v, m, k, t0, H))
        x.append(xt(m, u, k, t0))
        t0 += delta_t

    plt.plot(x, y)
    plt.xlabel('l')
    plt.ylabel('h')
    plt.title('Траектория движения подводной лодки')
    plt.grid(True)
    plt.show()

    t0 = 0
    delta_t = 0.1
    y = []
    x = []

    while yt(r, g, v, m, k, t0, H) <= 0:
        y.append(yt(r, g, v, m, k, t0, H))
        x.append(t0)
        t0 += delta_t

    plt.plot(x, y)
    plt.xlabel('t')
    plt.ylabel('h')
    plt.title('Зависимость глубины от времени')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
