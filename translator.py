# translator.py
from googletrans import Translator

translator = Translator()

translator.raise_Exception = True


def translator_translate(word):
    """
    Translates a given word to English using the translator module.

    :param word: The word to be translated. It should be a string in any language supported by the translator.
    :return: The translated word in English. If an error occurs during translation, the original word is returned.
    """
    try:
        result = translator.translate(word, dest='en')
        return result.text
    except Exception as ex:
        return word
