import os
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

# Заберем токен нашего бота (прописать в файле ".env")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# Заберем данные для подключения к базе данных (юзер, пароль, название бд) - тоже прописать в файле ".env"
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

admins = [
    os.getenv("ADMIN_ID"),
]

PRODUCT_OWNER = str(os.getenv("PRODUCT_OWNER"))


ip = os.getenv("ip")

# Ссылка подключения к базе данных
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
aiogram_redis = {
    'host': 'localhost',
}

redis = {
    'address': ('localhost', 6379),
    'encoding': 'utf8'
}
psycho_info_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTNjWpSCZ_J_dR7ORfy56k3KC2RXl5L3fvJ8MG3Cx32Fotb37lZJU5Ec7K1qcHcu-lFcDNmBz-33lyt/pub?output=csv"
