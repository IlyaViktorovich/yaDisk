import requests

file_name = input('Введите имя файла с расширением, которыq хотите записать на диск:')
file_name1 = input('Введите имя файла с расширением под которым Вы хотите записать файл:')
boks = input('Введите имя папки в которую хотите записать (не знаете куда, пишите в Netology):')
token = input('Введите токин с яндекс диска(в таком случае он не будет засвечен в "github":')

class YaUploader:
    def __init__(self, token):
        self.token = token
    def upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {self.token}'
        }
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()
    def upload_file_to_disk(self, file_path, file_name):
        href_dict = self.upload_link(file_path=file_path)
        href = href_dict.get("href", "")
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
    if __name__ == '__main__':
        uploader = YaUploader(token=token)
        result = uploader.upload_file_to_disk(f'{boks}/{file_name1}', file_name)