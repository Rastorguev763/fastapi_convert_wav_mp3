from fastapi import FastAPI, Body, File, UploadFile, Form, Request
from fastapi.responses import FileResponse
from database_module import*
from convert_wav_mp3 import*
import uvicorn

app = FastAPI()

@app.post("/userinfo")
async def new_user(data = Body()):
    user = check_user(data)
    if user:
       user_UUID = user.user_UUID
       user_id = user.user_id
    return {"message": f"АЙДИ ПОЛЬЗОВАТЕЛЯ - {user_id}, УИД ПОЛЬЗОВАТЕЛЯ - {user_UUID}"}


# проверка usera и UUID

@app.post("/convert")
async def convert_audio(user_id: str = Form(...), user_UUID: str = Form(...), audio_file: UploadFile = File(...)):
    # Доступ к сохраненному файлу: audio_file
    # Доступ к другим данным из формы: user_id
    user_info = check_UUID(user_UUID)
    
    try:
        if str(user_info[0].user_id) == user_id:
            return_convert = convert_wav_to_mp3(audio_file, user_id)

            file_convert_path = return_convert[0]
            file_safe_path = return_convert[1]

            audio_info = write_audio_info(user_id, file_safe_path, file_convert_path)
            return {"file_url": f"/record?id={audio_info.audio_id}&user={audio_info.user_id_create}"}
        
    except:

        return {"message": f"UUID ПОЛЬЗОВАТЕЛЯ - {user_id} ВВЕДЕН НЕ ВЕРНО"}
   

@app.get("/record")
async def download_file(id: str, user: str):
    audio_info = get_audio(id, user)
    file_path = audio_info[0].file_convert_path
    return FileResponse(file_path)


@app.get("/")
async def root():
    return FileResponse("public/main.html")

# для запуска сервера используйте команду
# uvicorn main_web:app --reload

if __name__ == "__main__":
    uvicorn.run("main_web:app", reload=True)