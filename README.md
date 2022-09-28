# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #1 выполнил:
- Кутявин Данил Сергеевич
- РИ-210945
Отметка о выполнении заданий (заполняется студентом):

| Задание | Выполнение | Баллы |
| ------ | ------ | ------ |
| Задание 1 | # | 60 |
| Задание 2 | # | 20 |
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
Ознакомиться с основными операторами языка Python на примере реализации линейной регрессии.

## Задание 1
### Написать программы Hellow World на Python и Unity.
Ход работы:
- Для Python в отчете привести скриншоты с демонстрацией сохранения документа google.
colab на свой диск с запуском программы, выводящей сообщение Hellow World.
![Снимок экрана (53)](https://user-images.githubusercontent.com/103362515/192768065-c0cc3eb7-4ef0-4014-b606-29a0e1a51dba.png)
![Снимок экрана (54)](https://user-images.githubusercontent.com/103362515/192768259-539699cb-e1d2-4af4-90f2-d14b0ed94579.png)

- Для Unity в отчетепривести скриншоты вывода сообщения Hellow World в консоль.
![Снимок экрана (55)](https://user-images.githubusercontent.com/103362515/192768743-66aaa671-5e34-4a6f-87fa-9461dedd55d3.png)


## Задание 2
### В разделе "ход работы" пошагово выполнять каждый пункт с описанием и примером реализации задачи по теме лабораторной работы.
### Ход работы.
1. Произвести подготовку данных для работы с алгоритмом линейной регрессии. 10 видов данных были установлены случайным образом, и данные находились в линейной зависимости. Данные преобразуются в формат массива, чтобы их можно было вычислить напрямую при использовании умножения и сложения.
![Снимок экрана (56)](https://user-images.githubusercontent.com/103362515/192774939-d9470644-1393-4ee0-9c66-cf1e437bbcc9.png)

2. Определите связанные функции. Функция модели: определяет модель линейной регрессии wx + b. Функция потерь: функция потерь среднеквадратичной ошибки. Функция оптимизации: метод градиентного спуска для нахождения частных производных w и b.
![Снимок экрана (57)](https://user-images.githubusercontent.com/103362515/192775742-253f912c-09db-4af9-90db-430255ec7bcb.png)
3. Начать итерацию
   
   Шаг 1. Инициализация и модель итеративной оптимизации
   
![Снимок экрана (58)](https://user-images.githubusercontent.com/103362515/192776031-f41404ff-71b8-4a44-980c-7147f45da746.png)

   Шаг 2. На всторой итерации отображаются значения переметров, значения потерь и эффекты визуализации после итерации
   
![Снимок экрана (60)](https://user-images.githubusercontent.com/103362515/192776311-ffffc2ad-c3bc-420b-a5b6-4c7f6ee7b2eb.png)

   Шаг 3. Третья итерация показывает значения параметров, значения потерь и визуализацию после итерации
   
![Снимок экрана (61)](https://user-images.githubusercontent.com/103362515/192776603-df3cea32-2fd1-4482-a95f-1589274e4463.png)

   Шаг 4. На четвертой итерации отображаются значения параметров, значения потерь и эффекты визуализации
   
![Снимок экрана (62)](https://user-images.githubusercontent.com/103362515/192776863-a63fb213-090e-41c4-9a77-08abadadc8c3.png)

   Шаг 5. Пятая итерация показывает значение парметра, значение потерь и эффект визуализации после итерации
   
![Снимок экрана (63)](https://user-images.githubusercontent.com/103362515/192777191-85bc6cf4-2c95-41fe-b991-5cd5e40cb5ab.png)

   Шаг 6. 10000-я итерация, показывающая значения параметров, потери и визуализацию после итерации
   
![Снимок экрана (65)](https://user-images.githubusercontent.com/103362515/192777408-bf08b59c-c3af-4499-b80b-362ac1acd85e.png)


## Задание 3
### Какова роль параметра Lr? Ответьте на вопрос, приведите пример выполнения кода, который подтверждает ваш ответ. В качестве эксперимента можете изменить значение параметра.

- Перечисленные в этом туториале действия могут быть выполнены запуском на исполнение скрипт-файла, доступного [в репозитории](https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/ScreatingSphereInAEDT.py).
- Для запуска скрипт-файла откройте Ansys Electronics Desktop. Перейдите во вкладку [Automation] - [Run Script] - [Выберите файл с именем ScreatingSphereInAEDT.py из репозитория].

```py

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.Rename("C:/Users/denisov.dv/Documents/Ansoft/SphereDIffraction.aedt", True)
oProject.InsertDesign("HFSS", "HFSSDesign1", "HFSS Terminal Network", "")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateSphere(
	[
		"NAME:SphereParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "1.0770329614269mm"
	], 
)

```

## Выводы

Абзац умных слов о том, что было сделано и что было узнано.

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
