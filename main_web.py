from fastapi import FastAPI, Body, File, UploadFile, Form
from fastapi.responses import FileResponse
from database_module import*
from convert_wav_mp3 import*
import shutil

app = FastAPI()

# TODO: POST 
@app.post("/userinfo")
def new_user(data = Body()):
    user = check_user(data)
    if user:
       user_UUID = user.user_UUID
       user_id = user.user_id
    return {"message": f"АЙДИ ПОЛЬЗОВАТЕЛЯ - {user_id}, УИД ПОЛЬЗОВАТЕЛЯ - {user_UUID}"}

# # TODO: Добавить ссылку для скачивания файла
# @app.post("/convert")
# def convert_audio(data = Body()):
#     # print(audio_wav_path)
#     file_convert_path = convert_wav_to_mp3(data)
#     write_audio_info(data, file_convert_path)
#     return {"message": f"ССЫЛКА ДЛЯ СКАЧИВАНИЯ {file_convert_path}"}

@app.post("/")
# async def convert_audio(user_id: str, user_UUID: str, audio_file: UploadFile = Body(...)):
async def convert_audio(user_id: str = Form(...), user_UUID: str = Form(...), audio_file: UploadFile = File(...)):
    # Доступ к сохраненному файлу: audio_file
    # Доступ к другим данным из формы: user_id, user_UUID
    print('TRATATATATAT')
    
    # Определите путь для сохранения файла
    save_path = f"songs/convert/{audio_file.filename}"
    
    # Сохранение файла на сервере
    with open(save_path, "wb") as f:
        shutil.copyfileobj(audio_file.file, f)

    return {"message": "Файл аудио успешно загружен и обработан."}

@app.get("/")
def root():
    return FileResponse("public/main.html")

# для запуска сервера используйте команду
# uvicorn main_web:app --reload