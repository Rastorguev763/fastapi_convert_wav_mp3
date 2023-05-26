from pydub import AudioSegment



file_name = 'sample_1'
# file_path = f'.\songs\{file_name}.wav'
file_path = f'{file_name}.wav'

song = AudioSegment.from_wav(file_path)
song.export(f"{file_name}_convert.mp3", format="mp3")