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
    audiomp3_UUID = Column(String)
    created_date = Column(DateTime, default=datetime.now)

# создание sqlite 
engine = create_engine('sqlite:///questions.sqlite')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

# Подключение и создание таблицы в PosgreSQL
# Замените значения на свои соответствующие параметры которые задавали при создания PostgreSQL
# db_user = 'root'
# db_password = 'root'
# db_host = '127.0.0.1'
# db_port = '5432'
# db_name = 'postgres'
# TODO: container_name = 'postgres_questions'

# Формируем строку подключения
# запуск с локальной машины
# db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# TODO: запуск с контейнера
# db_url = f'postgresql://{db_user}:{db_password}@{container_name}/{db_name}'
# engine = create_engine(db_url)
# Base.metadata.create_all(bind=engine)
# Session = sessionmaker(bind=engine)

def generate_uuid(username):
    # Генерируем UUID на основе имени пользователя и имени пространства имен UUID
    user_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, username)
    return user_uuid

def write_in_database(data):
    session = Session()
    # TODO: user_id = data[]
    user_name = data['user_name']
    user_UUID = generate_uuid(data['user_name'])
    audio_name = data['audio_path']
    # TODO: audio_id = data[]
    # audiomp3_UUID = data[]

# Сохранение вопроса в БД
    user = Users(user_name=user_name, user_UUID=str(user_UUID))
    audio = Audio(audio_name=audio_name)
    session.add(user)
    session.add(audio)
    session.commit()

def check_user(data):
    session = Session()
    # Проверка наличия вопроса в БД
    user_name = data['user_name']
    user_UUID = generate_uuid(data['user_name'])
    user_in_base = session.query(Users).filter_by(user_name=user_name).first()
    if user_in_base:
        print(f'ПОЛЬЗОВАТЕЛЬ С ТАКИМ ИМЕНЕМ УЖЕ ЕСТЬ {user_name}')
        return user_in_base
    else:
        user = Users(user_name=user_name, user_UUID=str(user_UUID))
        session.add(user)
        session.commit()
        print(f'ПОЛЬЗОВАТЕЛЬ С ТАКИМ ИМЕНЕМ {user_name} СОЗДАН')
        user_in_base = session.query(Users).filter_by(user_name=user_name).first()
        return user_in_base
