import speech_recognition as sr
from docx import Document  # Importa a biblioteca para criar arquivos .docx

# Função para salvar texto em um arquivo .txt
def salvar_como_txt(texto, caminho_txt):
    with open(caminho_txt, "w", encoding="utf-8") as file:
        file.write(texto)

# Função para salvar texto em um arquivo .docx
def salvar_como_docx(texto, caminho_docx):
    doc = Document()
    doc.add_paragraph(texto)
    doc.save(caminho_docx)

# Inicializa o reconhecedor de fala
recognizer = sr.Recognizer()

# Caminho do arquivo de áudio WAV
wav_file = r"C:\Users\letic\OneDrive\Área de Trabalho\Conversão audio para txt\Letícia-sendo-avó.wav"  # Substitua pelo caminho do seu arquivo

# Carrega o arquivo de áudio e tenta reconhecer o texto
with sr.AudioFile(wav_file) as source:
    audio_data = recognizer.record(source)  # Captura os dados de áudio
    try:
        # Usa o Google Web Speech API para transcrever o áudio
        texto = recognizer.recognize_google(audio_data, language="pt-BR")
        print("Texto reconhecido:", texto)
        
        # Salva o texto em um arquivo .txt
        salvar_como_txt(texto, "resultado_transcricao.txt")
        print("Texto salvo em 'resultado_transcricao.txt'")
        
        # Salva o texto em um arquivo .docx
        salvar_como_docx(texto, "resultado_transcricao.docx")
        print("Texto salvo em 'resultado_transcricao.docx'")
        
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        
    except sr.RequestError as e:
        print(f"Erro ao solicitar o serviço de reconhecimento de fala: {e}") 