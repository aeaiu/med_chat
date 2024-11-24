from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
import string
from nltk.corpus import stopwords
import spacy
import chatterbot_corpus
import yaml

#python -m spacy download en_core_web_sm


def chat(t1):    
    return "test" 

# Create object of ChatBot class with Storage Adapter
bot = ChatBot('Doctor',   read_only=True)
bot = ChatBot(
    'Doctor',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
bot = ChatBot(
    'Doctor',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
        ],
)
trainer = ChatterBotCorpusTrainer(bot)
# put the yaml file under: \.venv\Lib\site-packages\chatterbot_corpus\data\custom
#trainer.train("chatterbot.corpus.custom.medical")
response = bot.get_response("diabetes")
print("response")
print(response)
  