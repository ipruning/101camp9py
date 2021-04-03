import os
from pathlib import Path

from . import api
from . import app

print("Running" if __name__ == "__main__" else "Importing", Path(__file__).resolve())
# print(os.path.abspath("."))

app.ch1()
app.ch2()