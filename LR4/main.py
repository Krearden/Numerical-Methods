#coding=utf-8
from math import *


# Лабораторная работа № 4 на тему «Интерполирование. Среднеквадратичное приближение. Равномерное приближение»
# Выполнили Запорожченко Кирилл и Педаев Михаил (ФЗ-11)
# 2023 г.


#FUNCTIONS

#значение функции в точке x
def getFx(x, variant):
    if (variant == 0):
        return pow(3, x) + 3 * pow(x, 3) + 2
    else:
        print("Not done yet")

def getH(a, b, n):
    return (b - a) / (n - 1)

def Factorial(n):
    if (n == 0):
        return 1
    else:
        return n * Factorial(n - 1)


#Таблица разделенных разностей
def createSplitDiffTable(variant, a, b, n):
    h = getH(a, b, n)
    xs = []
    differences_table = [[] for i in range(n)]
    while(a <= b):
        xs.append(a)
        differences_table[0].append(getFx(a, variant))
        a += h
        a = round(a, 2)

    for i in range(1, n):
        for j in range(n - i):
            differences_table[i].append((differences_table[i - 1][j + 1] - differences_table[i - 1][j]) / (xs[j + i] - xs[j]))

    return xs, differences_table

#Печать таблицы разделенных разностей
def printSplitDiffTable(xs, differences_table):
    print("Таблица разделенных разностей:")
    for i in range(len(xs)):
        print("{:2.1f}".format(xs[i]), end = '  ')
        for j in range(len(differences_table[i])):
            print(differences_table[j][i], end = ' ')
        print()

#Полином ньютона по таблице разделенных разностей
def getNewtonPolynom(x, xs, differences_table):
    n = len(xs)
    y = 0
    part_summ = 1
    for i in range(n):
        y += part_summ * differences_table[i][0]
        part_summ *= x - xs[i]
    return y

#Фукнция. Возвращает произведения разностей (x - xi): i = 0 ... n - 1; xi берется из таблицы разделенных разностей.
def getOmega(x, xs, n):
    result = 1
    for i in range(n):
        result *= x - xs[i]
    return abs(result)

def getFirstDerivative(variant, x):
    if (variant == 0):
        return log(3) * pow(3, x) + 9 * x * x
    else:
        print("Not implemented yet")

def getMaxDerivatire(variant, x):
    maximum_derivative = 1e-100
    for x in xs:
        first_derivative = getFirstDerivative(variant, x)
        if (first_derivative > maximum_derivative):
            maximum_derivative = first_derivative
    return maximum_derivative

def getNewtonError(variant, x, xs, n):
    return getMaxDerivatire(variant, xs) * getOmega(x, xs, n)/ Factorial(n)

def printNewtonInterpolation(a, b, n, xs, differences_table):
    h = getH(a, b, n)
    a += h / 2
    print(" x              f(x)              Pn(x)                  Delta                    Оценка (вот здесь ошибка)")
    while (a < b):
        Fx = getFx(a, variant)
        newtonPx = getNewtonPolynom(a, xs, differences_table)
        print("{:2.3f}, {}, {}, {}, {}".format(a, Fx, newtonPx, abs(newtonPx - Fx), getNewtonError(variant, a, xs, n)))
        a += h / 2


#MAIN
if __name__ == '__main__':
    variants = [0]
    for variant in variants:
        a = 1
        b = 2
        n = 6
        xs, difft = createSplitDiffTable(variant, a, b, n)
        printSplitDiffTable(xs, difft)
        print()
        printNewtonInterpolation(a, b, n, xs, difft)
        # for i in range(len(xs)):
        #     print(xs[i], difft[i])