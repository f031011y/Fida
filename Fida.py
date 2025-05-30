# Importando bibliotecas
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage

# Definindo variáveis e constantes
api_key = ''
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama-3.3-70b-versatile')

BEHAVE_SYSTEM_PROMPT = '''
Você é um assistente especialista que sempre responde de forma sucinta.
Você utiliza as seguintes informações para formular suas respostas: {informacoes}
'''

# Carrega uma URL
def load_website():
    url = input('\nDigite a URL do site: ')
    try: # Ponto 2: Tratamento de Erros
        loader = WebBaseLoader(url)
        document_list = loader.load()
        document = "".join([doc.page_content for doc in document_list if doc.page_content])
        if not document:
            print("\nNenhum conteúdo encontrado no site ou o conteúdo está vazio.")
            return ""
        print("\nSite carregado com sucesso!")
        return document
    except Exception as e:
        print(f"Erro ao carregar o site: {e}")
        return ""

# Carrega um vídeo do YouTube
def load_yt():
    url = input('\nDigite o link do vídeo anexado no YouTube: ')
    try: # Ponto 2: Tratamento de Erros
        loader = YoutubeLoader.from_youtube_url(url, language=['pt'])
        document_list = loader.load()
        document = "".join([doc.page_content for doc in document_list if doc.page_content])
        if not document:
            print("\nNenhum conteúdo encontrado no vídeo ou o conteúdo está vazio.")
            return ""
        print("\nVídeo do YouTube carregado com sucesso!")
        return document
    except Exception as e:
        print(f"\nErro ao carregar o vídeo do YouTube: {e}")
        return ""

# Carrega um arquivo PDF
def load_pdf():
    path = input('\nDigite o caminho do documento: ')
    try: # Ponto 2: Tratamento de Erros
        loader = PyPDFLoader(path)
        document_list = loader.load() 
        document = "".join([doc.page_content for doc in pages if doc.page_content])
        if not document:
            print("\nNenhum conteúdo encontrado no PDF ou o conteúdo está vazio.")
            return ""
        print("\nPDF carregado com sucesso!")
        return document
    except FileNotFoundError:
        print(f"\nErro: Arquivo não encontrado em '{path}'. Verifique o caminho e tente novamente.")
        return ""
    except Exception as e:
        print(f"\nErro ao carregar o PDF: {e}")
        return ""

# Gera resposta
def respond(messages_history, current_document):
    system_message_content_template = BEHAVE_SYSTEM_PROMPT

    prompt_messages_for_template = [
        ('system', system_message_content_template)
    ]
    
    prompt_messages_for_template.extend(messages_history)

    template = ChatPromptTemplate.from_messages(prompt_messages_for_template)
    chain = template | chat
    return chain.invoke({'informacoes': current_document}).content

# Execução
def run_fida_chatbot():
    while True:
        document = ''
        valid_option_selected = False

        # Loop para seleção de opção e carregamento de documento
        while not valid_option_selected:
            print('\nFida')
            print('\n[1] Chat livre')
            print('[2] Consultar URL (link do site)')
            print('[3] Consultar vídeo do YouTube')
            print('[4] Consultar PDF')
            option_input = input('\nOpção: ')

            try:
                option = int(option_input)
                if option == 1:
                    print("\nIniciando chat livre...\n")
                    document = ''
                    valid_option_selected = True
                elif option == 2:
                    document = load_website()
                    if document: # Procede apenas se o documento foi carregado com sucesso
                        valid_option_selected = True
                    else:
                        print("\nNão foi possível carregar o documento do site. Por favor, tente outra URL ou opção.")
                elif option == 3:
                    document = load_yt()
                    if document:
                        valid_option_selected = True
                    else:
                        print("\nNão foi possível carregar o documento do YouTube. Por favor, tente outro vídeo ou opção.")
                elif option == 4:
                    document = load_pdf()
                    if document:
                        valid_option_selected = True
                    else:
                        print("\nNão foi possível carregar o documento PDF. Por favor, tente outro arquivo ou opção.")
                else:
                    print('\nOpção inválida. Por favor, escolha uma opção de 1 a 4.')
            except ValueError:
                print("\nEntrada inválida. Por favor, digite um número correspondente à opção.")
            except Exception as e:
                print(f"\nOcorreu um erro inesperado durante a seleção: {e}")

        # Loop de chat
        messages = [] # Reinicia o histórico de mensagens para cada nova sessão/documento
        print("Digite 'X' (ou 'x') a qualquer momento para encerrar esta sessão de chat.")

        while True:
            prompt = input('\nVocê: ')
            if prompt.upper() == 'X':
                print("\nEncerrando esta sessão de chat...")
                break

            messages.append(HumanMessage(content=prompt))

            try:
                response_content = respond(messages, document)
                messages.append(AIMessage(content=response_content))
                print(f'\nFida: {response_content}')
            except Exception as e:
                print(f"Erro ao tentar obter resposta do assistente: {e}")

                if messages: messages.pop()

        print(f'\nFim da sessão')
        if messages: # Mostra o histórico se houver mensagens
             print(f'Histórico da conversa nesta sessão:')
             for msg in messages:
                 if isinstance(msg, HumanMessage):
                     print(f"  Você: {msg.content}")
                 elif isinstance(msg, AIMessage):
                     print(f"  Fida: {msg.content}")

        while True:
            choice_again = input('\nDeseja iniciar uma nova consulta ou chat? (S para Sim / N para Não): ').upper()
            if choice_again == 'S':
                break # Volta para o início do loop externo run_fida_chatbot
            elif choice_again == 'N':
                print("\nObrigado por usar o Chatbot Fida! Até logo.")
                return # Encerra a função run_fida_chatbot e o programa
            else:
                print("Opção inválida. Por favor, digite S ou N.")

# Executa o chatbot
if __name__ == "__main__":
    run_fida_chatbot()
