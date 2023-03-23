from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

API_TOKEN = config['API_TOKEN']
LINK_CAT = config['LINK_CAT']
CRYPTO_API = config['CRYPTO_API']
BANK_API = config['BANK_API']
URL_TOP_FILMS = config['URL_TOP_FILMS']
URL_JOKE = config['URL_JOKE']
RECEPT_API = config['RECEPT_API']
