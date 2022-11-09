# АНАЛИЗ ДАННЫХ И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ [in GameDev]
Отчет по лабораторной работе #3 выполнил(а):
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
Познакомиться с программными средствами для создания системы машинного обучения и ее интеграции в Unity.

## Задание 1
### Реализовать систему машинного обучения в связке Python - Google-Sheets – Unity.
- Создаём новый Unity 3D проект.
- Скачиваем папку с ML агентом.
- Добавляем в Package Manager ML-Agents.

![image](https://user-images.githubusercontent.com/113508468/200816640-fe89cb89-952f-4fb5-810e-17d4163e3033.png)

- Далее запускаем Anaconda Prompt для возможности запуска команд через консоль.
- Далее пишем серию команд для создания и активации нового ML-агента, а также для скачивания необходимых библиотек:
o mlagents 0.28.0;
o torch 1.7.1;

![image](https://user-images.githubusercontent.com/113508468/200818714-d7a3c8e8-fe06-409e-ac4c-e173d5eddd0d.png)

-Создаём на сцене плоскость, куб и сферу. А также добавляем сфере C#-скрипт

![image](https://user-images.githubusercontent.com/113508468/200824149-2a6e339a-a08a-4fcc-a8d2-7193a8ee8f47.png)

-В скрипт файл добавляем код

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;
using Unity.MLAgents.Actuators;

public class RollerAgent : Agent
{
    Rigidbody rBody;
    // Start is called before the first frame update
    void Start()
    {
        rBody = GetComponent<Rigidbody>();
    }

    public Transform Target;
    public override void OnEpisodeBegin()
    {
        if (this.transform.localPosition.y < 0)
        {
            this.rBody.angularVelocity = Vector3.zero;
            this.rBody.velocity = Vector3.zero;
            this.transform.localPosition = new Vector3(0, 0.5f, 0);
        }

        Target.localPosition = new Vector3(Random.value * 8-4, 0.5f, Random.value * 8-4);
    }
    public override void CollectObservations(VectorSensor sensor)
    {
        sensor.AddObservation(Target.localPosition);
        sensor.AddObservation(this.transform.localPosition);
        sensor.AddObservation(rBody.velocity.x);
        sensor.AddObservation(rBody.velocity.z);
    }
    public float forceMultiplier = 10;
    public override void OnActionReceived(ActionBuffers actionBuffers)
    {
        Vector3 controlSignal = Vector3.zero;
        controlSignal.x = actionBuffers.ContinuousActions[0];
        controlSignal.z = actionBuffers.ContinuousActions[1];
        rBody.AddForce(controlSignal * forceMultiplier);

        float distanceToTarget = Vector3.Distance(this.transform.localPosition, Target.localPosition);

        if(distanceToTarget < 1.42f)
        {
            SetReward(1.0f);
            EndEpisode();
        }
        else if (this.transform.localPosition.y < 0)
        {
            EndEpisode();
        }
    }
}

```
-Объекту сфера добавляем и изменяем компоненты

![image](https://user-images.githubusercontent.com/113508468/200825828-3e2cdb55-0167-4785-90d6-5991ef661f19.png)
![image](https://user-images.githubusercontent.com/113508468/200825877-d69dc7c0-0fb1-46ed-8f43-4c0a50e925fd.png)

-Добавляем файл конфигурации нейронной сети и следующий код:
```yaml
behaviors:
  RollerBall:
    trainer_type: ppo
    hyperparameters:                 
      batch_size: 10
      buffer_size: 100
      learning_rate: 3.0e-4
      beta: 5.0e-4
      epsilon: 0.2
      lambd: 0.99
      num_epoch: 3
      learning_rate_schedule: linear
    network_settings: 
      normalize: false
      hidden_units: 128
      num_layers: 2
    reward_signals:
      extrinsic:
        gamma: 0.99
        strength: 1.0
    max_steps: 500000
    time_horizon: 64
    summary_freq: 10000
```
-Запускаем ml-agent
![image](https://user-images.githubusercontent.com/113508468/200826303-0ecef4a0-63b6-463c-beba-a6eca763d13b.png)


![image](https://user-images.githubusercontent.com/113508468/200826564-f2447ca5-6153-4963-b760-c8414861689c.png)
![image](https://user-images.githubusercontent.com/113508468/200826624-1099cd6a-b173-4a35-8359-52b31c4ac9dd.png)

-3 копии:
![image](https://user-images.githubusercontent.com/113508468/200826849-7390a063-f876-4c0a-8be9-4e545e324d7a.png)
![image](https://user-images.githubusercontent.com/113508468/200826922-6e9ccfaa-9a81-4f15-9b2a-210245b64973.png)

-После обучения модели видно, что шарик стал двигаться напрямую к кубику, перестал постоянно падать за пределы платформы и стал быстрее находить кубик.


## Задание 2
### Подробно опишите каждую строку файла конфигурации нейронной сети, доступного в папке с файлами проекта по ссылке. Самостоятельно найдите информацию о компонентах Decision Requester, Behavior Parameters, добавленных на сфере.

```
behaviors:
  RollerBall:                        #Имя агента
    trainer_type: ppo                #Устанавливаем режим обучения.
    hyperparameters:                 #Задаются гиперпараметры.
      batch_size: 10                 #Количество опытов на каждой итерации для обновления экстремумов функции.
      buffer_size: 100               #Количество опыта, которое нужно набрать перед обновлением модели.
      learning_rate: 3.0e-4          #Устанавливает шаг обучения (начальная скорость).
      beta: 5.0e-4                   #Отвечает за случайность действия, повышая разнообразие и иследованность пространства обучения.
      epsilon: 0.2                   #Порог расхождений между старой и новой политиками при обновлении.
      lambd: 0.99                    #Определяет авторитетность оценок значений во времени. Чем выше значение, тем более авторитетен набор предыдущих оценок.
      num_epoch: 3                   #Количество проходов через буфер опыта, при выполнении оптимизации.
      learning_rate_schedule: linear #Определяет, как скорость обучения изменяется с течением времени, линейно уменьшает скорость.
    network_settings:                #Определяет сетевые настройки.
      normalize: false               #Отключается нормализация входных данных.
      hidden_units: 128              #Количество нейронов в скрытых слоях сети.
      num_layers: 2                  #Количество скрытых слоев для размещения нейронов.
    reward_signals:                  #Задает сигналы о вознаграждении.
      extrinsic:
        gamma: 0.99                  #Коэффициент скидки для будущих вознаграждений.
        strength: 1.0                #Шаг для learning_rate.
    max_steps: 500000                #Общее количество шагов, которые должны быть выполнены в среде до завершения обучения.
    time_horizon: 64                 #Количество циклов ML агента, хранящихся в буфере до ввода в модель.
    summary_freq: 10000              #Количество опыта, который необходимо собрать перед созданием и отображением статистики.
```

- Decision Requester - запрашивает решение через регулярные промежутки времени и обрабатывает чередование между ними во время обучения.

- Behavior Parameters - определяет принятие объектом решений, в него указывается какой тип поведения будет использоваться: уже обученная модель или удалённый процесс обучения.

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
