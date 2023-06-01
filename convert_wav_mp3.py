from pydub import AudioSegment
import logging, time

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

def convert_wav_to_mp3(audio_file, user_id_create, ):
    file_name = audio_file.filename.split('.')[0]
    audio_wav_path = audio_file.file
    current_timestamp = int(time.time())
    song = AudioSegment.from_wav(audio_wav_path)
    file_convert_path = f".\songs\convert\{user_id_create}_{file_name}_convert_{current_timestamp}.mp3"
    song.export(file_convert_path, format="mp3")
    return file_convert_path