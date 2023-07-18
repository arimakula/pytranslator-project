from py_translator import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def main():
    text = input("Enter the text to translate: ")
    src_lang = input("Enter the source language code (e.g., en): ")
    dest_lang = input("Enter the destination language code (e.g., fr): ")

    translated_text = translate_text(text, src_lang, dest_lang)
    print("Translated Text:", translated_text)

if __name__ == "__main__":
    main() 
