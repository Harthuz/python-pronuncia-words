# **Documentação: Geração de Áudios com gTTS**

Este programa utiliza a biblioteca `gTTS` (Google Text-to-Speech) para gerar áudios em formato `.mp3` com a pronúncia de palavras ou frases fornecidas em um arquivo de texto. Os áudios são salvos individualmente em uma pasta chamada `audios`.

---

## **Requisitos**

- **Python**: 3.6 ou superior.
- **Bibliotecas Necessárias**: Instale as dependências executando:

```bash
pip install gtts
```

---

## **Estrutura do Programa**

### **Funções**

#### `read_words_from_file(file_path)`
- **Descrição**: Lê palavras ou frases de um arquivo de texto.
- **Parâmetros**:
  - `file_path` (str): Caminho para o arquivo de texto contendo as palavras/frases.
- **Retorno**:
  - `list`: Lista de palavras/frases (uma por linha).
- **Exemplo**:
  ```python
  words = read_words_from_file("words.txt")
  # Retorna: ['hello', 'world', 'Python']
  ```

---

#### `generate_individual_audio(words, output_folder="audios", language="en")`
- **Descrição**: Gera arquivos de áudio individuais para cada palavra/frase e os salva em uma pasta específica.
- **Parâmetros**:
  - `words` (list): Lista de palavras/frases a serem convertidas em áudio.
  - `output_folder` (str): Nome da pasta onde os arquivos serão salvos (padrão: `audios`).
  - `language` (str): Idioma da pronúncia (código ISO, padrão: `en` para inglês).
- **Comportamento**:
  - Cria a pasta `audios` se ela não existir.
  - Salva cada palavra/frase em um arquivo `.mp3` na pasta.
- **Exemplo**:
  ```python
  generate_individual_audio(['hello', 'world'], output_folder="audios")
  # Salva: audios/hello.mp3 e audios/world.mp3
  ```

---

### **Como Usar**

#### 1. **Preparar o Arquivo de Texto**
Crie um arquivo chamado `words.txt` no mesmo diretório do programa. Cada linha deve conter uma palavra ou frase:

```
Scarf
Shell casings
Tie
Ham
```

#### 2. **Executar o Programa**
Execute o script Python:

```bash
python nome_do_arquivo.py
```

#### 3. **Verificar os Áudios**
Os arquivos `.mp3` serão salvos na pasta `audios`. O nome de cada arquivo será baseado na palavra ou frase, com espaços substituídos por `_`.

---

### **Exemplo Completo**

#### Arquivo `words.txt`
```
Hello
World
Python
Automation
```

#### Execução
```bash
python words.py
```

#### Resultado
Os arquivos de áudio serão salvos na pasta `audios`:
```
audios/
    Hello.mp3
    World.mp3
    Python.mp3
    Automation.mp3
```

---

## **Observações**

1. **Idioma Suportado**:
   - O idioma padrão é o inglês (`en`). Para outro idioma, altere o parâmetro `language` para o código ISO correspondente (exemplo: `pt` para português).

2. **Erros Comuns**:
   - **Arquivo não encontrado**: Certifique-se de que o `words.txt` está no mesmo diretório ou forneça o caminho correto.
   - **Biblioteca ausente**: Instale a biblioteca `gTTS` com `pip install gtts`.
