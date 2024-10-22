import random
import matplotlib.pyplot as plt

def check(expression, N=10000):
    """
    Функція для перевірки складної умови із
    завдання 1 лабораторної роботи №2.

    Функція нічого не повертає та будує графік області, що задовольняє
    складній умові

    Параметри:
         expression(str): рядок з умовою
            Приклад:
               '-2<=x<=0 and y>0'

         N(int): кількість точок на графіку. Необов1'язковий параметр,
                 за замовченням N=5000
    """

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    a = -3
    b = 3
    plt.xlim(a, b)
    plt.ylim(a, b)

    for _ in range(N):
        x = random.random()*(b-a)+a # щоб випадкове число було в інтервалі (a,b)
        y = random.random()*(b-a)+a
        if eval(expression):
            plt.plot(x, y, "k.", markersize=1)
    plt.show();

# Приклад виклику функції
check('-1 <= y <= 1 and -1 <= x <= 1 and x**2 + y**2 > 1 ')
