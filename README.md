# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #4 выполнил(а):
- Винник Константин Алексеевич
- РИ210943
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

## Цель работы
### Ознакомиться с работой перцептрона
## Задание 1
### В проекте Unity реализовать перцептрон, который умеет производить вычисления
Ход работы:
- добавил пустой объект, добавил к нему скрипт Perceptron
![image](https://user-images.githubusercontent.com/60822244/204272208-bff1f805-0479-4d18-ad50-c75fb4f99268.png)
- заполнил каждый элемент
1. OR, понадобилось 3 эпохи, 4 вычисляла корректно

![image](https://user-images.githubusercontent.com/60822244/204275993-da71454e-d42c-441b-96d7-2de93902ab02.png)
![image](https://user-images.githubusercontent.com/60822244/204275107-484f83ac-a1b4-49e9-ac1b-6901d3a9fce6.png)
2. AND, понадобилось 4 эпохи, 5 вычисляла корректно

![image](https://user-images.githubusercontent.com/60822244/204276056-fc5d36d7-7c81-4c02-9bfe-e6511e0be419.png)
![image](https://user-images.githubusercontent.com/60822244/204275587-2ac5ea8d-fdec-4bb5-af15-96d5acd70b26.png)
3. NAND, понадобилось 5 эпох, 6 вычисляла корректно

![image](https://user-images.githubusercontent.com/60822244/204276085-69baf390-89f3-4508-9ed3-b178cb536b87.png)
![image](https://user-images.githubusercontent.com/60822244/204275918-b12ff651-123a-46f9-a453-e36005b06da0.png)
4. XOR, даже спустя 100000 эпох не смог обучиться и поэтому некорректно выполняет вычисления

![image](https://user-images.githubusercontent.com/60822244/204277780-5b64303f-6db7-4343-b352-b1a439c139e7.png)
![image](https://user-images.githubusercontent.com/60822244/204277742-77c17538-d4bc-45d0-937f-77fd33f14c92.png)
## Задание 2
### Построить графики зависимости количества эпох от ошибки обучения. Указать от чего зависит необходимое количество эпох обучения
Ход работы:
- занес данные в excel и построил график

![image](https://user-images.githubusercontent.com/60822244/204281211-3dae577e-bbc3-4d04-a3cf-e016dff9c4ba.png)
- количество эпох зависит от смещения и веса

![image](https://user-images.githubusercontent.com/60822244/204281641-27466562-6385-4abd-bd2f-f9cb5cdeebd2.png)
## Задание 3
### Построить визуальную модель работы перцептрона на сцене Unity
Ход работы:
- создал модель для работы NAND, черные кубы - нули, белые - единицы
![image](https://user-images.githubusercontent.com/60822244/204301909-52b25b47-9946-4397-9148-56273c261e98.png)
- создал скрипт для изменения цвета при столкновении
```
using UnityEngine;

public class ChangeColor : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.GetComponent<Renderer>().material.color == Color.black && this.gameObject.GetComponent<Renderer>().material.color == Color.black)
        {
            other.gameObject.GetComponent<Renderer>().material.color = Color.white;
            this.gameObject.GetComponent<Renderer>().material.color = Color.white;
        }
        else if (other.gameObject.GetComponent<Renderer>().material.color == Color.black && this.gameObject.GetComponent<Renderer>().material.color == Color.white)
        {
            other.gameObject.GetComponent<Renderer>().material.color = Color.white;
            this.gameObject.GetComponent<Renderer>().material.color = Color.white;
        }
        else if (other.gameObject.GetComponent<Renderer>().material.color == Color.white && this.gameObject.GetComponent<Renderer>().material.color == Color.black)
        {
            other.gameObject.GetComponent<Renderer>().material.color = Color.white;
            this.gameObject.GetComponent<Renderer>().material.color = Color.white;
        }
        else {
            other.gameObject.GetComponent<Renderer>().material.color = Color.black;
            this.gameObject.GetComponent<Renderer>().material.color = Color.black;
        }
    }
}
```
- кубы меняют цвет в зависимости от результата логического сложения

![ezgif com-gif-maker](https://user-images.githubusercontent.com/60822244/204302396-59b4abc0-8407-4eea-b6ed-1aecd9f488ea.gif)
## Выводы
Я познакомился с работой перцептрона, который вычисляет различные функции, построил график зависимостей, построил визуальную модель работы перцептрона на сцене Unity

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
