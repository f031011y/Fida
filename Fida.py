# Importando bibliotecas
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import ChatPromptTemplate

# Definindo variáveis
api_key = 'your_api_key'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Carrega uma URL
def load_website():
    url = input('\nDigite a URL do site: ')
    loader = WebBaseLoader(url)
    document_list = loader.load()
    document = ''
    for doc in document_list:
        document += doc.page_content
    return document

# Carrega um vídeo do YouTube
def load_yt():
    url = input('\nDigite o link do vídeo anexado no YouTube: ')
    loader = YoutubeLoader.from_youtube_url(url, language=['pt'])
    document_list = loader.load()
    document = ''
    for doc in document_list:
        document += doc.page_content
    return document

# Carrega um arquivo PDF
def load_pdf():
    path = input('\nDigite o caminho do documento: ')
    loader = PyPDFLoader(path)
    document = ''
    for doc in document_list:
        document += doc.page_content
    return document

# Gera resposta
def respond(messages, document):
    behave = '''
    Você é um assistente especialista que sempre responde de forma sucinta.
    Você utiliza as seguintes informações para formular suas respostas: {informacoes}
    '''
    role = [('system', behave)]
    role += messages
    template = ChatPromptTemplate.from_messages(role)
    chain = template | chat
    return chain.invoke({'informacoes': document}).content
    
while True:
    option = int(input('\nChatbot\n\n[1] Chat livre\n[2] Consultar URL (link do site)\n[3] Consultar vídeo do YouTube\n[4] Consultar PDF\n\nOpção: '))

    document = ''
    
    if option == 1:
        break
    
    elif option == 2:
        document = load_website()
        break

    elif option == 3:
        document = load_yt()
        break
    
    elif option == 4:
        document = load_pdf()
        break
    
    else:
        print('Opção inválida')

messages = []

while True:
    prompt = input('\nInsira um prompt ou X para encerrar: ')
    if prompt.upper() == 'X':
        break
    messages.append(('user', prompt))
    response = respond(messages, document)
    messages.append({'role': 'assistant', 'content': response})
    print(f'\nResposta: {response}')

print(f'\n{messages}')
