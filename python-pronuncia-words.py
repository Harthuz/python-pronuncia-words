import os
from gtts import gTTS

def read_words_from_file(file_path):
    """
    Lê palavras de um arquivo de texto, cada linha contendo uma palavra ou frase.

    :param file_path: Caminho para o arquivo de texto.
    :return: Lista de palavras/frases.
    """
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def generate_individual_audio(words, output_folder="audios", language="en"):
    """
    Gera arquivos de áudio individuais para cada palavra/frase e os salva em uma pasta.

    :param words: Lista de palavras (strings) a serem convertidas em áudio.
    :param output_folder: Pasta onde os arquivos de áudio serão salvos.
    :param language: Código do idioma (padrão é 'en' para inglês).
    """
    # Cria a pasta se ela não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for word in words:
        tts = gTTS(text=word, lang=language)
        # Substitui espaços por underscores no nome do arquivo
        filename = os.path.join(output_folder, f"{word.replace(' ', '_')}.mp3")
        tts.save(filename)
        print(f"Áudio salvo como {filename}")

# Exemplo de uso:
if __name__ == "__main__":
    # Nome do arquivo de texto com as palavras
    input_file = "words.txt"

    # Lê palavras do arquivo e gera o áudio
    word_list = read_words_from_file(input_file)
    if word_list:
        generate_individual_audio(word_list)
    else:
        print(f"O arquivo {input_file} está vazio ou não contém palavras válidas.")
