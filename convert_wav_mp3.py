from pydub import AudioSegment
import logging, time, shutil

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

# Создание объекта Logger
logger = logging.getLogger('pydub')

# Создание обработчика журнала
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Добавление обработчика к объекту Logger
logger.addHandler(handler)

# Указываем путь до исполняющего файла FFMPEG.EXE <'C:\ffmpeg\bin\ffmpeg.exe'>'
AudioSegment.converter = r'C:\ffmpeg\bin\ffmpeg.exe'

# TODO: создавать папки если их не существует
def convert_wav_to_mp3(audio_file, user_id, ):
    try:
         # Определите путь для сохранения файла
        filename = f'{user_id}_{audio_file.filename.split(".")[0]}_{int(time.time())}.{audio_file.filename.split(".")[-1]}'
        file_save_path = f"songs\{filename}"

            # Сохранение файла на сервере
        with open(file_save_path, "wb") as f:
            shutil.copyfileobj(audio_file.file, f)
    except Exception as e:
        print(e)
     
    file_name = audio_file.filename.split('.')[0]
    current_timestamp = int(time.time())
    song = AudioSegment.from_wav(audio_file.file)
    file_convert_path = f"songs\convert\{user_id}_{file_name}_convert_{current_timestamp}.mp3"
    song.export(file_convert_path, format="mp3")

    # print(file_convert_path, file_save_path)
    return file_convert_path, file_save_path