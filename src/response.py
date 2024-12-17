from googletrans import Translator
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def translate_text(text):
    parts = text.split(" ", 1)
    if len(parts) == 2:
        code, input_text = parts
        try:
            translator = Translator()
            translation = translator.translate(text=input_text, dest=code)
            logging.info(f"Translated text: {translation.text}")
            return translation.text
        except Exception as e:
            logging.error(f"Translation failed: {e}")
            return "Translation error occurred."
    else:
        return "Invalid input format."

if __name__ == "__main__":
    print(translate_text("es Hello World"))
