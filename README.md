# TEXT RECOGNITION
Text Recognition in images using Yandex Cloud Speechkit

Для работы необходим аккаунт в Yanex SpeechKit.

После регистрации, выполняя инструкции на сайте, получите oath-токен и folder_id (id папки, в которой вы работаете)
В text_detection_origin.py вставьте данные в соотв. поля. 

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

![image](https://github.com/HoboHub/text_recognition/assets/25107684/8e256b32-24f8-43fe-bbcf-c0222bd68a33)

![image](https://github.com/HoboHub/text_recognition/assets/25107684/4c7cf162-fb93-456b-ad49-ae01b1dc0d1d)

![image](https://github.com/HoboHub/text_recognition/assets/25107684/ae6f0daa-bf90-4c23-b097-2836603e3d4b)

# Исходное изображение

![otche-nash-izhe-esi-mem-shablon](https://github.com/HoboHub/text_recognition/assets/25107684/a8e3941f-63b3-4c4c-9d60-8d9b6a4deed9)


