from pydub import AudioSegment
import logging, time

# TODO: подключаем logging к pydub
# Настройка логирования
# logging.basicConfig(level=logging.DEBUG, filename='app.log',
#                     format='%(asctime)s %(levelname)s: %(message)s')
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

# file_name = 'sample_1'
# file_path = f'.\songs\{file_name}.wav'

def convert_wav_to_mp3(data):
    audio_wav_path = data['wav_path']
    user_id_create = data['user_id']
    file_name = audio_wav_path.split('\\')[-1].split('.')[0]
    current_timestamp = int(time.time())
    song = AudioSegment.from_wav(audio_wav_path)
    file_convert_path = f".\songs\convert\{user_id_create}_{file_name}_convert_{current_timestamp}.mp3"
    song.export(file_convert_path, format="mp3")
    return file_convert_path