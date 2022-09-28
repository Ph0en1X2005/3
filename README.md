# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #1 выполнил(а):
- Мокроносов Александр Сергеевич
- РИ210950
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
### Написать программы Hello World на Python и Unity. 

Python:
![image](https://user-images.githubusercontent.com/113508468/192731093-2398b509-0e72-4dc5-b73a-56556db99698.png)
![image](https://user-images.githubusercontent.com/113508468/192731114-6ee36c9d-4207-4a9e-87c0-a34171633713.png)

Unity:
![image](https://user-images.githubusercontent.com/113508468/192731201-81fea6ab-52ad-46fb-9942-cc9fa90bdf9e.png)

## Задание 2
### В разделе «ход работы» пошагово выполнить каждый пункт с описанием и примером реализации задачи по теме лабораторной работы.

Ход работы:
- 1.	Произвести подготовку данных для работы с алгоритмом линейной регрессии. 10 видов данных были установлены случайным образом, и данные находились в линейной зависимости. Данные преобразуются в формат массива, чтобы их можно было вычислить напрямую при использовании умножения и сложения.

 1:
 ![image](https://user-images.githubusercontent.com/113508468/192731718-3d4099ca-6228-482d-b504-b1c5e2aa10f3.png)

 2:
 ![image](https://user-images.githubusercontent.com/113508468/192732091-445f14f9-bbd9-4f26-b4db-eb059d4a2b2f.png)

 3:
 Шаг 1:
 ![image](https://user-images.githubusercontent.com/113508468/192732242-daf9a0bd-60e3-47a4-94c6-9502c1e8af4d.png)
 ![image](https://user-images.githubusercontent.com/113508468/192732257-d0bd732e-1253-48b9-b459-834a7346000c.png)

 Шаг 2:
 ![image](https://user-images.githubusercontent.com/113508468/192732314-8433d0bb-facd-43ac-bd1f-5737e6f5a643.png)
 ![image](https://user-images.githubusercontent.com/113508468/192732334-3befa9b2-f64e-48e9-8c7e-ae7efc293c23.png)

 Шаг 3:
 ![image](https://user-images.githubusercontent.com/113508468/192732435-0a367528-7367-4c42-87a4-6ddef0128df6.png)
 ![image](https://user-images.githubusercontent.com/113508468/192732456-55c364dd-850f-4499-99ec-7ba8c82922cb.png)

 Шаг 4:
 ![image](https://user-images.githubusercontent.com/113508468/192732513-6f0fe776-f034-458f-b681-a322e7765824.png)
 ![image](https://user-images.githubusercontent.com/113508468/192732553-5669f94b-fafe-40f5-bae7-95a2b0f28d78.png)
 
 Шаг 5:
 ![image](https://user-images.githubusercontent.com/113508468/192732577-7c4fb657-21ee-4412-8394-272c61b9bdf6.png)
 ![image](https://user-images.githubusercontent.com/113508468/192732595-ebad0c91-d4af-4dcf-b335-9c9bdd8c1aeb.png)

 Шаг 6:
 ![image](https://user-images.githubusercontent.com/113508468/192732650-19500738-28bb-4e85-ab4c-8f9c5e1267fe.png)
 ![image](https://user-images.githubusercontent.com/113508468/192732681-c65d8885-3cba-4a16-8b83-d3c53b95765a.png)


## Задание 3
### Должна ли величина loss стремиться к нулю при изменении исходных данных? Ответьте на вопрос, приведите пример выполнения кода, который подтверждает ваш ответ.

При уменьшении размера массивов x и y величина less будет стремить к нулю
# ![image](https://user-images.githubusercontent.com/113508468/192739494-69026f64-2a8d-4441-85d5-3ab82248ccdc.png)
![image](https://user-images.githubusercontent.com/113508468/192739753-b9d5360f-8623-4845-ab8c-2fe3c38890e5.png)

Но при увеличении размеров массивов всё наоборот
# ![image](https://user-images.githubusercontent.com/113508468/192740447-517a4b08-d0c4-495e-91b1-5c7a2c489c05.png)
![image](https://user-images.githubusercontent.com/113508468/192740480-7194b348-8105-4263-ab97-57e92487b77e.png)


## Задание 3
### Какова роль параметра Lr? Ответьте на вопрос, приведите пример выполнения кода, который подтверждает ваш ответ. В качестве эксперимента можете изменить значение параметра.

Параметр Lr помогает более точно подогнать отрезок и чем меньше параметр, тем меньше точность.
#![image](https://user-images.githubusercontent.com/113508468/192744027-98d8dc1f-0016-4229-9369-65b7421906e5.png)
![image](https://user-images.githubusercontent.com/113508468/192744213-96402b46-3039-4326-9f52-a4614c2b416e.png)


## Выводы

В первом задании научились писать программу "Hello World" на unity, а также python, а именно в google colab.
Во втором задании ознакомились с основными операторами языка python на примере реализации линейной регрессии.

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
