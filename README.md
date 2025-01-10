# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #1 выполнил(а):
- Полушин Максим Викторович
- РИ231122
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
Разработать оптимальный баланс нанесения урона оружием для игры Save RTF (конами-код для начисления денег / жизней и т.д.)

## Задание 1
### Расширьте варианты доступного оружия в игре. Используйте шаблон таблицы для визуализации оружия игры Save RTF.
Ход работы:
- Изучить игру и предложенные виды оружия
- Построить таблицу, добавив свои виды оружия

Ссылка на гугл-таблицу: https://docs.google.com/spreadsheets/d/1KIIE18FYnqLvxIIUsrHOu3RzTzvf1hT-tSwLXu3q3Nw/edit?gid=0#gid=0




## Задание 2
### Визуализируйте параметры оружия в таблице. Используйте шаблон таблицы для визуализации оружия игры Save RTF. Постройте примеры для следующих математических величин (см. пример в презентации):
- Среднеквадратическое отклонение (СКО)
- Разброс урона оружия
- Вариативность времени отклика игрока (реакция на события)


Пример для арбалета:
-
- Среднеквадратическое отклонение (СКО)

![image](https://github.com/user-attachments/assets/e429f934-6808-4aab-9785-813b82c291fd)
-
- Разброс урона оружия

![image](https://github.com/user-attachments/assets/c665d9f5-9d13-4884-b185-4c87454f8f87)
-
- Вариативность времени отклика игрока (реакция на события)

![image](https://github.com/user-attachments/assets/a1d63d2a-e704-4e78-a8f6-23c433bce539)


Пример для автомата:
-
- Среднеквадратическое отклонение (СКО)

![image](https://github.com/user-attachments/assets/7ca1f5e2-8c5c-4a7e-90d3-a4622fbb0851)
-
- Разброс урона оружия

![image](https://github.com/user-attachments/assets/8ac30945-9504-440b-b222-e3c181e0fe8d)
-
- Вариативность времени отклика игрока (реакция на события)

![image](https://github.com/user-attachments/assets/9012c99a-570e-4849-9a5d-b47b0d2d6992)






## Задание 3
### Решение в 80+ баллов должно визуализировать данные из google-таблицы, и с помощью Python передавать переменные в проект Unity. В Python данные также должны быть визуализированы.

import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1KIIE18FYnqLvxIIUsrHOu3RzTzvf1hT-tSwLXu3q3Nw/edit?gid=0#gid=0'
data = pd.read_csv(url)

plt.figure(figsize=(10, 6))
plt.bar(data['Weapon'], data['Damage'], color='coral')
plt.title('Урон различных типов оружия')
plt.xlabel('Оружие')
plt.ylabel('Урон')
plt.show()





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
