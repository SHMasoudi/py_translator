import os
import sys
import logging
from deep_translator import GoogleTranslator

# Setup logger
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def translate_file(input_path: str, output_path: str = "output.txt"):
    """
    Translate the contents of a file from English to Persian using Deep Translator (Google).
    """
    if not os.path.exists(input_path):
        logging.error(f"Input file '{input_path}' not found.")
        return

    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except Exception as e:
        logging.error(f"Failed to read input file: {e}")
        return

    translated_lines = []

    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            translated_lines.append("")
            continue
        try:
            translated = GoogleTranslator(source='en', target='fa').translate(line)
            translated_lines.append(translated)
            logging.info(f"[Line {i}] Translated.")
        except Exception as e:
            logging.warning(f"[Line {i}] Failed to translate: {e}")
            translated_lines.append(line)

    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write("\n".join(translated_lines))
        logging.info(f"Translation completed. Output saved to '{output_path}'.")
    except Exception as e:
        logging.error(f"Failed to write output file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python translator.py <input_file>")
    else:
        translate_file(sys.argv[1])
