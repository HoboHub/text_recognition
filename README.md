# TEXT RECOGNITION
Text Recognition in images using Yandex Cloud Speechkit

Для работы необходим аккаунт в Yanex SpeechKit.

После регистрации, выполняя инструкции на сайте, получите oath-токен и folder_id (id папки, в которой вы работаете)
В text_detection.py вставьте данные в соотв. поля. 

+Укажите путь к интерпретатору Python (он должен быть установлен) в upload.php

# Схема работы

После выгрузки изображения, нажмите upload

Произойдет редирект на стр. с распознанным текстом (для дальнешей работы с ним).

В каталоге сгенерируется 2 новых файла:

**img_rec_output.json** - ответ Yandex SpeeckKit

**extracted_text_values.php** - отобранные из json текстовые данные с распознанным текстом.


# Больше информации о Yandex Cloud:
https://github.com/yandex-cloud/yc-architect-solution-library

# Пример

![image](https://github.com/HoboHub/text_recognition/assets/25107684/ca9cfac0-f2e2-4d1f-b9b4-073731b0898e)

![image](https://github.com/HoboHub/text_recognition/assets/25107684/69ccb3b4-fbd5-425a-bd3f-ea34feca4776)

![image](https://github.com/HoboHub/text_recognition/assets/25107684/b0975cce-186f-49f2-bded-592852cf82e5)

# Исходное изображение

![otche-nash-izhe-esi-mem-shablon](https://github.com/HoboHub/text_recognition/assets/25107684/a8e3941f-63b3-4c4c-9d60-8d9b6a4deed9)


