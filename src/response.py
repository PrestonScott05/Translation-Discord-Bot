from googletrans import Translator

def translate_text(text):
    parts = text.split(" ", 1)

    if len(parts) == 2:
        code, input_text = parts
        translator = Translator()
        translation = translator.translate(text=input_text, dest=code)
        return translation.text
    else:
        return "Invalid input format"

# Example Usage
if __name__ == "__main__":
    print(translate_text("es Hello World"))
