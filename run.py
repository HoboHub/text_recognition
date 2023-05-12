import json

def extract_text_values(data):
    text_values = []

    def extract_values(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == 'text':
                    text_values.append(value)
                elif isinstance(value, (dict, list)):
                    extract_values(value)
        elif isinstance(obj, list):
            for item in obj:
                extract_values(item)

    extract_values(data)
    return text_values

# Загрузка данных из файла JSON с учетом кодировки UTF-8
with open('img_rec_output.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Извлечение значений 'text'
extracted_values = extract_text_values(json_data)

# Сохранение значений в файл с кодировкой UTF-8
with open('extracted_text_values.php', 'w', encoding='utf-8') as file:
    file.write('<?php\n')
    file.write('$text_values = array(\n')
    for value in extracted_values:
        file.write("\t'" + value.replace("'", "\\'") + "',\n")
    file.write(');\n')