from fastapi import FastAPI, Body, File, UploadFile, Form, Request
from fastapi.responses import FileResponse
from database_module import*
from convert_wav_mp3 import*
import shutil

app = FastAPI()

@app.post("/userinfo")
async def new_user(data = Body()):
    user = check_user(data)
    if user:
       user_UUID = user.user_UUID
       user_id = user.user_id
    return {"message": f"АЙДИ ПОЛЬЗОВАТЕЛЯ - {user_id}, УИД ПОЛЬЗОВАТЕЛЯ - {user_UUID}"}

@app.post("/convert")
async def convert_audio(user_id: str = Form(...), audio_file: UploadFile = File(...)):
    # Доступ к сохраненному файлу: audio_file
    # Доступ к другим данным из формы: user_id

    try:
         # Определите путь для сохранения файла
        filename = f'{user_id}_{audio_file.filename.split(".")[0]}_{int(time.time())}.{audio_file.filename.split(".")[-1]}'
        save_path = f"songs/{filename}"

        file_convert_path = convert_wav_to_mp3(audio_file, user_id)

            # Сохранение файла на сервере
        with open(save_path, "wb") as f:
            shutil.copyfileobj(audio_file.file, f)
    except:
        return {"message": f"Произошла ошибка, попробуйте снова."} 
    
    return {"file_url": f"/record?file_path={file_convert_path}"}
# hhtp://host:port/record?id=id_audio&user=user_id

@app.get("/record")
async def download_file(file_path: str):
    print("EBALALALLA")
    return FileResponse(file_path)

@app.get("/")
async def root():
    return FileResponse("public/main.html")

# для запуска сервера используйте команду
# uvicorn main_web:app --reload