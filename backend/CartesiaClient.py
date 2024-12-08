from cartesia import Cartesia
from dotenv import load_dotenv
import os

load_dotenv()
client = Cartesia(api_key=os.environ.get("CARTESIA_API_KEY"))
print('test')
