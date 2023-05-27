from pydub import AudioSegment
import logging

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


file_name = 'sample_1'
file_path = f'.\songs\{file_name}.wav'
# file_path = f'{file_name}.wav'

song = AudioSegment.from_wav(file_path)
song.export(f".\songs\convert\{file_name}_convert.mp3", format="mp3")