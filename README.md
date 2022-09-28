# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #1 выполнил
- Сурков Степан Васильевич
- РИ-210915
### Отметка о выполнении заданий (заполняется студентом):

| Задание | Выполнение | Баллы |
| ------ | ------ | ------ |
| Задание 1 | * |    |
| Задание 2 | * |    |
| Задание 3 | * |    |

знак "*" - задание выполнено; знак "#" - задание не выполнено;
### Работу проверили:
- к.т.н., доцент Денисов Д.В.
- к.э.н., доцент Панов М.А.
- ст. преп., Фадеев В.О.
### Структура отчета

- Данные о работе: название работы, ФИО, группа, выполненные задания
- Цель работы
- Задание 1.
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Задание 2
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Задание 3
- Код реализации выполнения задания. Визуализация результатов выполнения (если применимо).
- Выводы.
- ✨Magic ✨

## Цель работы
Ознакомиться с основными операторами зыка Python на примере реализации линейной регрессии.

## Задание 1
### *Написать программы Hello World на Python и Unity*

#### 1. Вывод фразы "Hello World" в консоли Python
```py

print('Hello World!')
```

#### 2. Вывод фразы "Hello World" в консоли Unity

```c#
 void Start() {
     Debug.Log("Hello World");
 }
```

## Задание 2
### *В разделе «ход работы» пошагово выполнить каждый пункт с описанием и примером реализации задачи по теме лабораторной работы*

Производим подготовку данных для работы с алгоритмом линейной регрессии. 10 видов данных были установлены случайным образом, и
данные находились в линейной зависимости. 

Для вычислений использвуется модуль numpy, для отрисовки – matplotlib.

```py
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

x = [3, 21, 22, 34, 54, 34, 55, 67, 89, 99]
x = np.array(x)
y = [2, 22, 24, 65, 79, 82, 55, 130, 150, 199]
y = np.array(y)

plt.scatter(x, y)
```

### Определяем связанные функции

#### Базовая модель линейной регрессии
```py

def model(a, b, x):
    return a * x + b
```
#### Функция потерь от разницы средних отклонений (среднеквадратичной ошибки)
```py
def loss_function(a, b, x, y):
    num = len(x)
    prediction = model(a, b, x)
    return (0.5 / num) * (np.square(prediction - y)).sum()
```
#### Функция оптимизации (метод градиентного спуска для нахождения частных производных w и b)
```py
def optimize(a, b, x, y):
    num = len(x)
    prediction = model(a, b, x)
    da = (1.0 / num) * ((prediction - y) * x).sum()
    db = (1.0 / num) * ((prediction - y).sum())
    a = a - Lr * da
    b = b - Lr * db
    return a, b
```
#### Повторяемая функция, возвращающая a и b
```py
def iterate(a, b, x, y, times):
    for i in range(times):
        a, b = optimize(a, b, x, y)
    return a, b
```
#### Итоговая версия программы
```py
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

x = [3, 21, 22, 34, 54, 34, 55, 67, 89, 99]
x = np.array(x)
y = [2, 22, 24, 65, 79, 82, 55, 130, 150, 199]
y = np.array(y)

plt.scatter(x, y)

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
    db = (1.0 / num) * ((prediction - y).sum())
    a = a - Lr * da
    b = b - Lr * db
    return a, b


def iterate(a, b, x, y, times):
    for i in range(times):
        a, b = optimize(a, b, x, y)
    return a, b

a = np.random.rand(1)
print(a)
b = np.random.rand(1)
print(b)
Lr = 0.000001
```

### Результаты итераций

#### 1-я итерация
![1st](https://user-images.githubusercontent.com/66885212/192842629-52036583-3005-4adc-8603-57f38986a54a.png)

[0.31110294] [0.42610981] [0.31561037] [0.42617531] 3405.1539528522794 [<matplotlib.lines.Line2D at 0x7f299ec2e7d0>]

#### 2-я итерация

![2nd](https://user-images.githubusercontent.com/66885212/192842644-5a289df9-0077-4a96-ae8a-e234ed5fad14.png)

[0.65041773] [0.64105868] [0.65727051] [0.64115666] 2042.7362975213969 [<matplotlib.lines.Line2D at 0x7f299eeea8d0>]

#### 3-я итерация

![3rd](https://user-images.githubusercontent.com/66885212/192842646-6e5666bd-abc1-40d6-8f4c-9cc1ea45e654.png)

[0.12303663] [0.40941758] [0.1382848] [0.40964038] 4252.51086408771 [<matplotlib.lines.Line2D at 0x7f299ec520d0>]

#### 4-я итерация

![4th](https://user-images.githubusercontent.com/66885212/192842648-efeea3fc-a07e-42b0-9c6e-89059c0e5c63.png)

[0.79263549] [0.19375026] [0.80460544] [0.19392028] 1593.1145591757995 [<matplotlib.lines.Line2D at 0x7f299ecd4610

#### 5-я итерация

![5th](https://user-images.githubusercontent.com/66885212/192842650-534fb295-773f-4013-9596-3457600c2569.png)

[0.37698885] [0.83987749] [0.39825876] [0.84018515] 3019.207143774828 [<matplotlib.lines.Line2D at 0x7f299ed52d90>]

#### 10000-я итерация

![10000th](https://user-images.githubusercontent.com/66885212/192842653-63989805-2436-482f-a0f4-e7636fd7e3fd.png)

[0.18692472] [0.10658117] [1.75163077] [0.10007561] 189.05472287036343 [<matplotlib.lines.Line2D at 0x7f299edda550>]


## Задание 3
### Изучить код на Python и ответить на вопросы:

- Должна ли величина loss стремиться к нулю при изменении исходных данных? Ответьте на вопрос, приведите пример выполнения кода, который подтверждает ваш ответ.
- Какова роль параметра Lr? Ответьте на вопрос, приведите пример выполнения кода, который подтверждает ваш ответ. В качестве эксперимента можете изменить значение параметра.



## Выводы

Абзац умных слов о том, что было сделано и что было узнано.

| Plugin | README |
| ------ | ------ |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |


## Powered by

**BigDigital Team: Denisov | Fadeev | Panov**
