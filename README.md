# TEXT RECOGNITION
Text Recognition in images using Yandex Cloud Speechkit

Для работы необходим аккаунт в Yanex SpeechKit.

После регистрации, выполняя инструкции на сайте, получите oath-токен и folder_id (id папки, в которой вы работаете)
В text_detection.py вставьте данные в соотв. поля. 
+Укажите путь к интерпретатор Python (он должен быть установлен) в upload.php

# Схема работы

После выгрузки изображени, нажмите upload
Произойдет редирект на стр. с распознанным текстом (для дальнешей работы с ним).
В каталоге сгенерируется 2 новых файла:
img_rec_output.json - ответ Yandex SpeeckKit
extracted_text_values.php - отобранные из json текстовые данные с распознанным текстом.

