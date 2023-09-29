import os

from dotenv import load_dotenv

load_dotenv()

TOKEN_TODO = os.getenv("TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN_TODO}"
}
ABS_PATH = os.path.abspath(__file__ + "../../../")
