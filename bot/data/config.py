from environs import Env

env: Env = Env()
env.read_env()

class Config:

    token: str = env.str('TOKEN')

    user: str = env.str('USER')
    password: str = env.str('PASSWORD')
    host: str = env.str('HOST')
    database: str = env.str('DATABASE')
    
    url: str = f'postgresql+asyncpg://{user}:{password}@{host}/{database}'