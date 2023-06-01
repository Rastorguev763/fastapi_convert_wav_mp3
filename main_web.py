from fastapi import FastAPI, Body, File, UploadFile, Form, Request
from fastapi.responses import FileResponse
from database_module import*
from convert_wav_mp3 import*

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

    return_convert = convert_wav_to_mp3(audio_file, user_id)

    file_convert_path = return_convert[0]
    file_safe_path = return_convert[1]

    write_audio_info(user_id, file_safe_path, file_convert_path)

    # TODO:download_url = f"/record?id={file_convert_path}&user={user_id}"
    # hhtp://host:port/record?id=id_audio&user=user_id

    return {"file_url": f"/record?file_path={file_convert_path}"}

# TODO: get /record?id={file_convert_path}&user={user_id}
# def get path url
@app.get("/record")
async def download_file(file_path: str):
    return FileResponse(file_path)

@app.get("/")
async def root():
    return FileResponse("public/main.html")

# для запуска сервера используйте команду
# uvicorn main_web:app --reload