# translator.py
from googletrans import Translator

translator = Translator()

translator.raise_Exception = True


def translator_translate(word):
    try:
        result = translator.translate(word, dest='en')
        return result.text
    except Exception as e:
        return word