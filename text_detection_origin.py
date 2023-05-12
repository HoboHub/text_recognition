# coding: utf-8
from requests import post
import json
import argparse
import base64

# Функция возвращает IAM-токен для аккаунта на Яндексе.
def get_iam_token(iam_url, oauth_token):
    response = post(iam_url, json={"yandexPassportOauthToken": oauth_token})
    json_data = json.loads(response.text)


    if json_data is not None and 'iamToken' in json_data:
        return json_data['iamToken']
    return None

# Функция отправляет на сервер запрос на распознавание изображения и возвращает ответ сервера.
def request_analyze(vision_url, iam_token, folder_id, image_data):

    response = post(vision_url, headers={'Authorization': 'Bearer ' + iam_token}, json={
        'folderId': folder_id,
        'analyzeSpecs': [
            {
                'content': image_data,
                'features': [
                    {
                        'type': 'TEXT_DETECTION',
                        'textDetectionConfig': {'languageCodes': ['*']}
                    }
                ],
            }
        ]})
    return response.text


def main():
    parser = argparse.ArgumentParser()

    # parser.add_argument('--folder-id', required=True)
    # parser.add_argument('--oauth-token', required=True)
    parser.add_argument('--image-path', required=True)

    parser.add_argument('--mime', required=False) #for pdf test

    args = parser.parse_args()

    iam_url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
    vision_url = 'https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze'


    oauth_token = '<your-yandex-oath-tocken>'
    iam_token = get_iam_token(iam_url, oauth_token)

    folder_id='<your-yandex-folder-id>'


    # for img recognition
    with open(args.image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    response_text = request_analyze(vision_url, iam_token, folder_id, image_data)
    print(response_text)
    # -----------------------------------------------------------------------



    file = open('img_rec_output.json','w', encoding='utf-8')
    file.write(response_text)
    file.close()



    # return response_text;
    # 


if __name__ == '__main__':
    main()
