from pydub import AudioSegment
import logging

# TODO: подключаем logging к pydub
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)
# handler.setFormatter(formatter)
# logger.addHandler(handler)


# Указываем путь до исполняющего файла FFMPEG.EXE <'C:\ffmpeg\bin\ffmpeg.exe'>'
AudioSegment.converter = r'C:\ffmpeg\bin\ffmpeg.exe'


file_name = 'sample_1'
file_path = f'.\songs\{file_name}.wav'
# file_path = f'{file_name}.wav'

song = AudioSegment.from_wav(file_path)
song.export(f".\songs\convert\{file_name}_convert.mp3", format="mp3")