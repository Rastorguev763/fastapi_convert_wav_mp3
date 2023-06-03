from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

# Создание базы данных и таблицы
Base = declarative_base()

class Users(Base):
    __tablename__ = 'user_convert'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    user_UUID = Column(String)

class Audio(Base):
    __tablename__ = 'audio_convert'
    audio_id = Column(Integer, primary_key=True, autoincrement=True)
    audio_name = Column(String)
    file_path = Column(String)
    file_convert_path = Column(String)
    audiomp3_UUID = Column(String)
    user_id_create = Column(String)
    created_date = Column(DateTime, default=datetime.now)

# # создание sqlite 
# engine = create_engine('sqlite:///questions.sqlite')
# Base.metadata.create_all(bind=engine)
# Session = sessionmaker(bind=engine)

# Подключение и создание таблицы в PosgreSQL
# Замените значения на свои соответствующие параметры которые задавали при создания PostgreSQL
db_user = 'root'
db_password = 'root'
db_host = '127.0.0.1'
db_port = '5432'
db_name = 'postgres'
container_name = 'postgres_convert'

# Формируем строку подключения
# запуск с локальной машины
# db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# запуск с контейнера
db_url = f'postgresql://{db_user}:{db_password}@{container_name}/{db_name}'

engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

def sqlalchemy_to_json(my_object):
    # Преобразуем объект в словарь
    my_dict = my_object.__dict__

    # Удаляем некоторые ключи, которые не нужны
    keys_to_remove = ['_sa_instance_state', 'created_date']
    for key in keys_to_remove:
        my_dict.pop(key, None)

    return my_dict

def generate_uuid(username):
    code_word = 'babaski'
    # Генерируем UUID на основе имени пользователя и имени пространства имен UUID
    user_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, username+code_word)
    return user_uuid

def write_audio_info(user_id_create, file_path, file_convert_path):
    session = Session()
    user_id_create = user_id_create
    file_path = file_path
    file_convert_path = file_convert_path
    audio_name = file_path.split('/')[-1].split('.')[0]
    audiomp3_UUID = generate_uuid(audio_name)

# Сохранение вопроса в БД
    audio = Audio(user_id_create=user_id_create, audio_name=audio_name, audiomp3_UUID=str(audiomp3_UUID), file_path=file_path, file_convert_path=file_convert_path)
    session.add(audio)
    session.commit()

    audio_in_base = session.query(Audio).filter_by(user_id_create=user_id_create).order_by(Audio.created_date.desc()).first()
    return audio_in_base

def check_user(data):
    session = Session()
    # Проверка наличия вопроса в БД
    user_name = data['user_name']
    user_in_base = session.query(Users).filter_by(user_name=user_name).first()
    if user_in_base:
        print(f'ПОЛЬЗОВАТЕЛЬ С ТАКИМ ИМЕНЕМ УЖЕ ЕСТЬ {user_name}')
        return user_in_base
    else:
        user_UUID = generate_uuid(data['user_name'])
        user = Users(user_name=user_name, user_UUID=str(user_UUID))
        session.add(user)
        session.commit()
        print(f'ПОЛЬЗОВАТЕЛЬ С ТАКИМ ИМЕНЕМ {user_name} СОЗДАН')
        user_in_base = session.query(Users).filter_by(user_name=user_name).first()
        return user_in_base
    
def get_audio(id, user):
    session = Session()
    audio_info = session.query(Audio).filter_by(user_id_create=user,audio_id=id ).all()
    return audio_info

# TODO: сделать функцию проверки в базе на соответсвие user и UUID

def check_UUID(user_UUID):
    session = Session()
    user_info = session.query(Users).filter_by(user_UUID=user_UUID).all()
    return user_info