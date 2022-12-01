# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #2 выполнил(а):
- Мокроносов Александр Сергеевич
- РИ210950
Отметка о выполнении заданий (заполняется студентом):

| Задание | Выполнение | Баллы |
| ------ | ------ | ------ |
| Задание 1 | * | 60 |
| Задание 2 | * | 20 |
| Задание 3 | # | 20 |

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
Познакомиться с программными средствами для организции передачи данных между инструментами google, Python и Unity

## Задание 1
### Реализовать совместную работу и передачу данных в связке Python - Google-Sheets – Unity. 

Ход работы:

1. В облачном сервисе google console подключить API для работы с google sheets и google drive.

![Снимок экрана (415)](https://user-images.githubusercontent.com/113508468/204993447-897ddfe7-7b77-42cc-9c7d-c6e8a9c4ca70.jpg)

2. Реализовать запись данных из скрипта на python в google-таблицу. Данные описывают изменение темпа инфляции на протяжении 11 отсчётных периодов, с учётом стоимости игрового объекта в каждый период.

![image](https://user-images.githubusercontent.com/113508468/204994108-2788caec-3016-44f4-9d9e-d16d8bee8519.png)

3. Создать новый проект на Unity, который будет получать данные из google-таблицы, в которую были записаны данные в предыдущем пункте.

4. Написать функционал на Unity, в котором будет воспризводиться аудио-файл в зависимости от значения данных из таблицы.

![image](https://user-images.githubusercontent.com/113508468/205001961-2018f6a3-7047-4444-877d-f4a493406543.png)


## Задание 2
### Передадим значение loss в гугл-таблицу.

```
import gspread
import numpy as np
import matplotlib.pyplot as plt

gc = gspread.service_account(filename='unitydatascience-365207-b1a58de370e3.json')
sh = gc.open("UnitySheets")
priceX = np.random.randint(2000, 10000, 11)
priceX = np.array(priceX)
priceY = np.random.randint(2000, 10000, 11)
priceY = np.array(priceY)
mon = list(range(1, 11))


def model(a, b, x):
  return a * x + b


def loss_function(a, b, x, y):
  num = len(x)
  prediction = model(a, b, x)
  return (0.5 / num) * (np.square(prediction - y)).sum()


def optimize(a, b, x, y):
  num = len(x)
  prediction = model(a, b, x)
  da = (1.0 / num) * ((prediction - y) * x).sum()
  db = (1.0 / num) * (prediction - y).sum()
  a = a - Lr * da
  b = b - Lr * db
  return a, b


def iterate (a, b, x, y, times):
  for i in range(times):
    a, b = optimize(a, b, x, y)
  return a, b


x = [2, 11, 13, 16, 25, 36, 49, 56, 76, 84, 99]
x = np.array(x)
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = np.array(y)

a = np.random.rand(1)
b = np.random.rand(1)
Lr = 0.000001

a, b = iterate(a, b, priceX, priceY, 1)
prediction = model(a, b, priceX)
loss = loss_function(a, b, priceX, priceY)
print(a, b, loss)
plt.scatter(x, y)
plt.plot(x, prediction)


i = 0
while i <= len(mon):
    i += 1
    if i == 0:
        continue
    else:
        tempInf = ((prediction[i-1]-prediction[i-2])/prediction[i-2])*100
        tempInf = str(tempInf)
        tempInf = tempInf.replace('.', ',')
        sh.sheet1.update(('A' + str(i)), str(i))
        sh.sheet1.update(('B' + str(i)), str(prediction[i-1]//1))
        sh.sheet1.update(('C' + str(i)), str(tempInf))
        print(prediction)


```

![image](https://user-images.githubusercontent.com/113508468/205005329-743b073c-9bfd-4a7a-b137-6122bbf6bbd8.png)

## Выводы

В результате проделанной лабораторной работы узнал, как реализовать совместную работу и передачу данных в связке Python - Google-Sheets – Unity: писать скрипт на Python для заполнения Google-таблиц, получать, обрабатывать данные из Google-Sheets в Unity через скрипт на C#. 

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
