from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from database_module import*
from convert_wav_mp3 import*

app = FastAPI()

# TODO: POST метод для получения вопросов
@app.post("/userinfo")
def new_user(data = Body()):
    users = check_user(data)
    if users:
       user_UUID = users.user_UUID
       user_id = users.user_id
    return {"message": f"АЙДИ ПОЛЬЗОВАТЕЛЯ - {user_id}, УИД ПОЛЬЗОВАТЕЛЯ - {user_UUID}"}

# TODO: Добавить запись информации в базу и формирования на основе этой информации ссылки для скачивания файла
@app.post("/convert")
def convert_audio(data = Body()):
    audio_wav_path = data[r'wav_path']
    print(audio_wav_path)
    convert_wav_to_mp3(audio_wav_path)
    return {"message": f"ССЫЛКА ДЛЯ СКАЧИВАНИЯ - {audio_wav_path}"}


def sqlalchemy_to_json(my_object):
    # Преобразуем объект в словарь
    my_dict = my_object.__dict__

    # Удаляем некоторые ключи, которые не нужны
    keys_to_remove = ['_sa_instance_state', 'created_date']
    for key in keys_to_remove:
        my_dict.pop(key, None)

    return my_dict

@app.get("/")
def root():
    return FileResponse("public/main.html")

# для запуска сервера используйте команду
# uvicorn main_web:app --reload