# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #1 выполнил(а):
- Пичугин Михаил Сергеевич 
- РИ-210932
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
Ознакомиться с основными операторами зыка Python на примере реализации линейной регрессии.

## Задание 1
### Написать программы Hello world на Python и Unity
Для взаимодейстия с Python использовался Google Colab.

![Collab1](https://user-images.githubusercontent.com/114404329/192327326-840f89c6-cc97-4229-a8d7-715299bfccec.png)
![Collab2](https://user-images.githubusercontent.com/114404329/192327333-7403293f-4219-4474-9582-f259ebdad788.png)

Ход действий для выполнение задания, связанного с Unity:
Сначала был создан новый Unity проект. В проект были добавлены куб и плоскость. К сцене был привязан скрип с выводом "Hello World!" на консоль. После выполнения скрипта было выведено сообщение в консоль "Hello World!".

![Unity1](https://user-images.githubusercontent.com/114404329/192327283-4ab47208-b650-46a1-8307-b0a186da2d63.PNG)
![unity2](https://user-images.githubusercontent.com/114404329/192327289-48009be2-0a74-4f02-a8ab-8efa992ec9e1.PNG)
![Unity screan3](https://user-images.githubusercontent.com/114404329/192327291-a7857204-5caf-4927-a432-96916abfe79f.png)

## Задание 2
### Пошагово выполнить каждый пункт раздела "ход работы" с описанием и примерами реализации задач
Ход работы:
- Произвести подготовку данных для работы с алгоритмом линейной регрессии. 10 видов данных были установлены случайным образом, и данные находились в линейной зависимости. Данные преобразуются в формат массива, чтобы их можно было вычислить напрямую при использовании умножения и сложения.

```py

In [ ]:
#Import the required modules, numpy for calculation, and Matplotlib for drawing
import numpy as np
import matplotlib.pyplot as plt
#This code is for jupyter Notebook only
%matplotlib inline

# define data, and change list to array
x = [3,21,22,34,54,34,55,67,89,99]
x = np.array(x)
y = [2,22,24,65,79,82,55,130,150,199]
y = np.array(y)

#Show the effect of a scatter plot
plt.scatter(x,y)

```
Перенёс данные в Google Colab:

![0](https://user-images.githubusercontent.com/114404329/192331448-57ae7079-9b0a-48c3-969f-c786aa555b97.PNG)

- Определите связанные функции. Функция модели: определяет модель линейной регрессии wx+b. Функция потерь: функция потерь среднеквадратичной ошибки. Функция оптимизации: метод градиентного спуска для нахождения частных производных w и b.

Определил связь функций:

Функция модели:

```py

def model(a, b, x):
    return a * x + b 
    
```    

Функция потерь:

```py

def lossFunction(a, b, x, y):
    num = len(x)
    prediction = model(a, b, x)
    return (0.5 / num) * (np.square(prediction - y)).sum()

```

Функция оптимизации:

```py

def optimize(a, b, x, y, Lr):
    num = len(x)
    prediction = model(a, b, x)
    da = (1.0 / num) * ((prediction - y) * x).sum()
    db = (1.0 / num) * ((prediction - y).sum())
    a = a - Lr * da
    b = b - Lr * db
    return a, b
    
```

Шаг 1

![1](https://user-images.githubusercontent.com/114404329/192333419-77e5df15-a1aa-4d3c-997f-a3f5e8075b38.PNG)
 
Шаг 2

![2](https://user-images.githubusercontent.com/114404329/192333497-fef8fa0e-4bb3-4fe1-9d6d-fb5a6386395f.PNG)

Шаг 3

![3](https://user-images.githubusercontent.com/114404329/192333562-b807a78c-fb3d-47f8-a5aa-0ed12ab62b20.PNG)

Шаг 4

![4](https://user-images.githubusercontent.com/114404329/192333721-71abba83-bfce-402e-807f-e574c522888a.PNG)

Шаг 5

![5](https://user-images.githubusercontent.com/114404329/192333765-7fcd5556-1e3c-47e0-9e18-302e982dc966.PNG)

Шаг 6

![10000](https://user-images.githubusercontent.com/114404329/192333798-d80669b3-0482-4936-9aa7-a7ae7d840d24.PNG)

## Задание 3
### Должна ли величина loss стремиться к нулю при изменении исходных данных? Ответьте на вопрос, приведите пример выполнения кода, который подтверждает ваш ответ.

Да, должна. Если мы увеличим количества итераций, величина loss будет стремиться к нулю.

При 1 итерации, loss будет равна приблизительно 1411:

![1](https://user-images.githubusercontent.com/114404329/192337406-75337c9f-c27f-4f59-8829-f8e2ef08d6ef.PNG)

При 10000 итераций, loss будет равна приблизительно 189:

![10000](https://user-images.githubusercontent.com/114404329/192337624-42d0a4f8-84e4-465c-a345-2ddb82a19e63.PNG)

При 1000000 итераций, loss будет равна приблизительно 182:

![1000000](https://user-images.githubusercontent.com/114404329/192338193-2c9b44cb-e9b9-49dd-82fb-f8a8d7c108b6.PNG)

Эти примеры доказывают, что при увеличении колличества итераций, loss становится меньше, следовательно, стремится к нулю

### Какова роль параметра Lr? Ответьте на вопрос, приведите пример выполнения кода, который подтверждает ваш ответ. В качестве эксперимента можете изменить значение параметра.

От параметра Lr зависил угол наклона между прямой и линией горизонта. Чем больше значение Lr, тем больше угол между ними.
(Серая линия и красная кривая на скриншотах нарисованы в графическом редакторе Paint для наглядности)

При Ln = 0.00001:

![0 00001](https://user-images.githubusercontent.com/114404329/192341786-9f98e7d6-6c8c-4fc2-aa03-9b2d075ef33d.png)

При Ln = 0.0001:

![0 0001](https://user-images.githubusercontent.com/114404329/192342456-8ce7a5e4-c3db-48f1-b823-7803a895ece8.png)

При Ln = 0.001:

![0 001](https://user-images.githubusercontent.com/114404329/192342494-69731086-7cf0-4bb2-9867-7234c98c1032.png)


## Выводы

В ходе данной работы я написал две простые программы на Ubity и Python(Google colab). Также по ютуб гайдам я настроил среды разработки.
Далее, я проанализировал и реализовал код из методички, тем самым познакомившись с алгоритмом линейной регрессии и функциями модели, потерь и оптимизации. После были проведены эксперименты для выявления зависимости и закономерности.

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
