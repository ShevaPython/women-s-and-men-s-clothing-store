from dotenv import load_dotenv


def load_environment(env_file, basedir):
    # Функция для загрузки переменных окружения из указанного файла
    env_path = basedir / env_file
    load_dotenv(env_path)
