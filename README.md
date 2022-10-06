# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #2 выполнил(а):
- Ли Александр Альбертович
- Х21IT_AI-01BL
Отметка о выполнении заданий (заполняется студентом):

| Задание | Выполнение | Баллы |
| ------ | ------ | ------ |
| Задание 1 | * | 60 |
| Задание 2 | * | 20 |
| Задание 3 | * | 20 |

знак "*" - задание выполнено; знак "#" - задание не выполнено;

Работу проверили:
- к.т.н., доцент Денисов Д.В.
- к.э.н., доцент Панов М.А.
- ст. преп., Фадеев В.О.

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Структура отчета

- Данные о работе: название работы, фио, группа, выполненные задания.
- Цель работы.
- Задание 1.
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Задание 2.
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Задание 3.
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Выводы.
- ✨Magic ✨

## Цель работы
познакомиться с программными средствами для организции передачи данных между инструментами google, Python и Unity

## Задание 1
### Пошагово выполнить каждый пункт раздела "ход работы" с описанием и примерами реализации задач

Следуя видео-инструкции, удалось настроить гугл-таблицы с Unity и вводом записей с PyCharm.

![image](https://user-images.githubusercontent.com/78469125/194118299-c0e25d43-83bb-408f-af85-996a9e0f4854.png)


## Задание 2
### Реализовать запись в Google-таблицу набора данных, полученных с помощью линейной регрессии из лабораторной работы № 1

![image](https://user-images.githubusercontent.com/78469125/194115734-ba400617-4e5c-47bf-a3cc-9353e550eae2.png)

Следующий скрипт возвращает в гугл-таблицу фиксированные данные с первой лабораторной работы, рассчитывая параметр loss при разном количестве итераций.

```py
import gspread
import numpy as np


def loss_function(a, b, x, y):
    num = len(x)
    prediction = model(a, b, x)
    return (0.5 / num) * (np.square(prediction - y)).sum()

def model(a, b, x):
    return a * x + b

def optimize(a, b, x, y):
    num = len(x)
    prediction = model(a, b, x)
    # Update the values of A and B by finding the partial derivatives of the loss function on a and b
    da = (1.0 / num) * ((prediction - y) * x).sum()
    db = (1.0 / num) * ((prediction - y).sum())
    a = a - Lr * da
    b = b - Lr * db
    return a, b

def iterate(a,b,x,y,times):
    for i in range(times):
        a,b = optimize(a,b,x,y)
    return a,b

gc = gspread.service_account(filename='unityproject-364614-db2360b977ac.json')
sh = gc.open('UnitySheet')
x = [3, 21, 22, 34, 54, 34, 55, 67, 89, 99]
x = np.array(x)
y = [2, 22, 24, 65, 79, 82, 55, 130, 150, 199]
y = np.array(y)
a = np.random.rand(1)
b = np.random.rand(1)
Lr = 0.0001
print(a,b,loss)
i = 0
while i <= len(x+1):
    i += 1
    if i == 0:
        continue
    else:
        iter = np.random.randint(1, 15)
        print(iter)
        a,b = iterate(a,b,x,y,iter)
        loss = loss_function(a, b, x, y)
        tempInf = loss
        tempInf = str(tempInf)
        tempInf = tempInf.replace('.', ',')
        sh.sheet1.update(('A' + str(i)), str(x[i-1]))
        sh.sheet1.update(('B' + str(i)), str(y[i-1]))
        sh.sheet1.update(('C' + str(i)), str(tempInf))
        print(tempInf)

```

## Задание 3
### Самостоятельно разработать сценарий воспроизведения звукового сопровождения в Unity в зависимости от изменения считанных данных в задании 2

Параметр loss менялся сильно от малого количества итераций (1-4) к среднему (5-9), который, в своб очередь, близился к фиксированному значению при 10-15 итерациях. Таким образом, звуковое сопровождение будет комментировать высокий, средний и низкий уровни потерь.

![image](https://user-images.githubusercontent.com/78469125/194116771-f01b56c2-7c50-4c4d-92e4-17066e3ae775.png)


## Выводы

Удалось настроить API к гугл-таблицам от PyCharm, было интересно разобрать изначально данный код на последующие задачи. Один из выводов состоит в том, что Unity, а точнее С#, очень привередлив к коду, ввиду чего требовалась постоянная модификация скрипта, сравнения с дефолтными данными, дебаг, и нервы. 

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Powered by

**BigDigital Team: Denisov | Fadeev | Panov**
