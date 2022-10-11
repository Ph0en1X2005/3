# Сбор, обработка и визуализация тестового набора данных[in GameDev]
Отчет по лабораторной работе #2 выполнил(а):
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
Познакомиться с программными средствами для организции передачи данных между инструментами google, Python и Unity.

## Задание 1
### Реализовать совместную работу и передачу данных в связке Python - Google-Sheets – Unity.

В Google Cloud подключил нужные расширения API сервисов: Drive, Sheets. Далее создал API-ключ, выгрузил ключ сервисного аккаунта

![1](https://user-images.githubusercontent.com/114404329/195164170-259f092c-a319-428f-a02d-d88f0f260be8.PNG)

Реализовал запись данных с помощью PyCharm на языке Python в Google Spreadsheets. Данные описывают изменение темпа инфляции на протяжении 11 отсчётных периодов, с учётом стоимости игрового объекта в каждый период.

![4](https://user-images.githubusercontent.com/114404329/195164224-1f6fa39b-85c3-490d-8464-46386b577be3.PNG)

![5](https://user-images.githubusercontent.com/114404329/195164281-366c16e6-7b4b-4d6e-bc27-6f267cea9c99.PNG)

Создал новый проект на Unity. Проект будет получать данные из Google Spreadsheets, которые я ранее записал в Google Таблицу с помощью скрипта(реализовал в PyCharm пунктом выше). Добавил в проект приложенные файлы.Написал функцию на Unity, с помощью которой воспризводится аудиофайл в зависимости от значения данных из таблицы.

![6](https://user-images.githubusercontent.com/114404329/195164390-0fc3db0d-e0fd-4454-b50c-067d9ae40520.PNG)

Проверил,вызвав одну итерацию.

![7 1](https://user-images.githubusercontent.com/114404329/195164414-ecf2af62-eb97-4009-8628-dfabedb8a6c1.PNG)

![7 2](https://user-images.githubusercontent.com/114404329/195164437-7d662e46-98ef-415f-bfab-fe8d873fe4cc.PNG)

![7 3](https://user-images.githubusercontent.com/114404329/195164452-8c6f6a19-5430-4545-adbe-beec6da7ac26.PNG)

#Вызвал остальные итерации. В момент вызова испугался громких звуков( 

![8 1](https://user-images.githubusercontent.com/114404329/195164638-8c6aa772-d697-4ba0-a2a4-9d295e2af78d.PNG)

![8 2](https://user-images.githubusercontent.com/114404329/195164648-ca6fa05c-0ca4-43b2-8c4b-c8da73ddec9f.PNG)

![8 3](https://user-images.githubusercontent.com/114404329/195164650-a96dad6b-3877-4e4a-afce-191d94139e24.PNG)

![8 4](https://user-images.githubusercontent.com/114404329/195164652-20e38df7-975f-4a7b-8ca6-d02c82932503.PNG)
## Задание 2
### Реализовать запись в Google-таблицу набора данных, полученных с помощью линейной регрессии из лабораторной работы № 1

Отрефакторил код из прошлой лабораторной работы, добавил строки, чтобы результаты выводились в Google Таблицу.

![2 1](https://user-images.githubusercontent.com/114404329/195169017-9d8b815c-a9b4-4d6e-854c-189cf14d94e3.PNG)

![2 3](https://user-images.githubusercontent.com/114404329/195169024-1c5b61c3-8602-4008-a9df-6d2220c83c36.PNG)

Проверил вывод в таблицу.

![2 2](https://user-images.githubusercontent.com/114404329/195169020-b262e3f0-2eb1-45db-9d51-5fc086f47a2b.PNG)

## Задание 3
### Самостоятельно разработать сценарий воспроизведения звукового сопровождения в Unity в зависимости от изменения считанных данных в задании 2.

Поменял значения так, чтобы это было похоже на репутацию и соответствующие реплике человуку,имеющему её.

![3 2](https://user-images.githubusercontent.com/114404329/195174890-b30d7edb-e31a-4549-85a5-88d9fff279ee.PNG)

![3 3](https://user-images.githubusercontent.com/114404329/195174893-0a327a0a-1f09-4e3f-89ea-52439943412d.PNG)

<picture> using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Networking;
    using SimpleJSON;
    public class NewBehaviourScript : MonoBehaviour
    {
        public AudioClip goodSpeak;
        public AudioClip normalSpeak;
        public AudioClip badSpeak;
        private AudioSource selectAudio;
        private Dictionary<string,float> dataSet = new Dictionary<string, float>();
        private bool statusStart = false;
        private int i = 1;

        // Start is called before the first frame update
        void Start()
        {
            StartCoroutine(GoogleSheets());
        }

        // Update is called once per frame
        void Update()
        {
            if (i > dataSet.Count) 
            {
                return;
            }
            if (dataSet["Mon_" + i.ToString()] >= 90 & statusStart == false & i <= dataSet.Count)
            {
                StartCoroutine(PlaySelectAudioGood());
                Debug.Log(dataSet["Mon_" + i.ToString()]);
            }

            if (dataSet["Mon_" + i.ToString()] <= 500 & dataSet["Mon_" + i.ToString()] >= 30 & statusStart == false & i <= dataSet.Count)
            {
                StartCoroutine(PlaySelectAudioNormal());
                Debug.Log(dataSet["Mon_" + i.ToString()]);
            }

            if (dataSet["Mon_" + i.ToString()] <= -0 & statusStart == false & i <= dataSet.Count)
            {
                StartCoroutine(PlaySelectAudioBad());
                Debug.Log(dataSet["Mon_" + i.ToString()]);
            }
        }

        IEnumerator GoogleSheets()
        {
            UnityWebRequest curentResp = UnityWebRequest.Get("https://sheets.googleapis.com/v4/spreadsheets/1xaf3NHEcjJtk_3BtuyEvQOxFDK187dLF9PCWf8NwQdU/values/Лист1?key=AIzaSyBoEQc3LUe4qNeZ_5kbk8WqL0UvbdXy86o");
            yield return curentResp.SendWebRequest();
            string rawResp = curentResp.downloadHandler.text;
            var rawJson = JSON.Parse(rawResp);
            foreach (var itemRawJson in rawJson["values"])
            {
                var parseJson = JSON.Parse(itemRawJson.ToString());
                var selectRow = parseJson[0].AsStringList;
                dataSet.Add(("Mon_" + selectRow[0]), float.Parse(selectRow[2]));
            }
        }

        IEnumerator PlaySelectAudioGood()
        {
            statusStart = true;
            selectAudio = GetComponent<AudioSource>();
            selectAudio.clip = goodSpeak;
            selectAudio.Play();
            yield return new WaitForSeconds(3);
            statusStart = false;
            i++;
        }
        IEnumerator PlaySelectAudioNormal()
        {
            statusStart = true;
            selectAudio = GetComponent<AudioSource>();
            selectAudio.clip = normalSpeak;
            selectAudio.Play();
            yield return new WaitForSeconds(3);
            statusStart = false;
            i++;
        }
        IEnumerator PlaySelectAudioBad()
        {
            statusStart = true;
            selectAudio = GetComponent<AudioSource>();
            selectAudio.clip = badSpeak;
            selectAudio.Play();
            yield return new WaitForSeconds(4);
            statusStart = false;
            i++;
        }
    }

## Выводы

В ходе данной работы я научился соединять Google таблицу с кодом,Unity. Узнал как работать с Google Spreadsheets API на Python. Также узнал как получать данные в реальном времени из Google Spreadsheets в Unity. Также узнал, что в зависимости от диапазона данных можно воспроизводить звук в Unity.

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
