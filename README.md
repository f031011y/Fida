# 💬 Fida: Seu Assistente Conversacional Inteligente

![Logo do Fida](logo.png)

**Fida é uma ferramenta de conversação versátil que interage com a poderosa API do Groq, utilizando a robusta biblioteca Langchain. Converse livremente ou obtenha insights de links da web, vídeos do YouTube e documentos PDF, tudo em uma interface simples e intuitiva.**

O Fida foi criado com o objetivo de ser um assistente de múltipla utilidade, capaz de fornecer consultas e interações a partir de diversos tipos de dados. Ele busca centralizar a busca por informações em uma única interface, tornando a experiência do usuário mais simples e eficiente.

## 🎯 Público-Alvo

* **Desenvolvedores:** Que buscam integrar ou entender o funcionamento de LLMs com diferentes fontes de dados.
* **Estudantes e Pesquisadores:** Que necessitam de uma forma rápida de extrair e interagir com informações de documentos, vídeos e páginas web.
* **Usuários em Geral:** Que desejam uma maneira facilitada e direta de interagir com inteligência artificial para obter respostas e informações.

## ⚙️ Como Funciona

O Fida opera como um chatbot que pode ser executado localmente no seu terminal. Ele oferece um menu interativo onde você pode escolher entre:

1. **Chat Livre:** Conversar diretamente com o modelo de linguagem da Groq (Llama 3) sem um contexto de documento específico.
2. **Consultar URL:** Fornecer um link de uma página da web. O Fida carregará o conteúdo textual da página e você poderá fazer perguntas sobre ele.
3. **Consultar Vídeo do YouTube:** Inserir o link de um vídeo do YouTube. O Fida transcreverá o áudio (se disponível em português) e permitirá que você converse sobre o conteúdo do vídeo.
4. **Consultar PDF:** Informar o caminho local para um arquivo PDF. O Fida extrairá o texto do documento para que você possa fazer perguntas e obter informações dele.

Em todos os modos de consulta de documentos, o Fida utiliza o conteúdo carregado como base para formular respostas sucintas e diretas às suas perguntas.

## ✨ Recursos Principais

* **Interface de Linha de Comando (CLI) Interativa:** Fácil de usar e navegar.
* **Múltiplas Fontes de Dados:** Suporte para chat aberto, URLs da web, vídeos do YouTube e arquivos PDF.
* **Integração com Groq API:** Utiliza modelos de linguagem de alta performance para respostas rápidas e coerentes.
* **Processamento de Linguagem Natural com Langchain:** Orquestra a interação entre o usuário, os documentos e o modelo de linguagem.
* **Respostas Contextualizadas:** As respostas são baseadas no documento fornecido (URL, YouTube, PDF) ou em conhecimento geral no modo de chat livre.
* **Histórico de Conversa:** Ao final de cada sessão, o histórico da conversa é exibido para referência.
* **Tratamento de Erros:** Inclui tratamento básico para carregamento de documentos e interações.

## 🛠️ Ferramentas Utilizadas

O Fida é construído com as seguintes tecnologias principais:

* **Python 3:** Linguagem de programação principal do projeto. É necessário ter o Python 3 ou superior instalado.
* **Langchain (`langchain`):** Uma biblioteca fundamental que atua como o cérebro do Fida. Ela facilita a criação de aplicações com Modelos de Linguagem (LLMs), permitindo a conexão com diversas fontes de dados, o gerenciamento de prompts e a orquestração de cadeias de processamento. É crucial para integrar o modelo da Groq com os diferentes tipos de documentos.
* **Langchain-Groq (`langchain-groq`):** O conector específico que permite ao Langchain se comunicar eficientemente com a API da Groq, viabilizando o uso de seus modelos de linguagem rápidos e poderosos.
* **Langchain-Community (`langchain-community`):** Contém uma vasta gama de integrações e componentes desenvolvidos pela comunidade Langchain. No Fida, destacam-se os `DocumentLoaders` (`WebBaseLoader`, `YoutubeLoader`, `PyPDFLoader`), que são essenciais para carregar e processar o conteúdo de URLs, vídeos do YouTube e arquivos PDF, respectivamente.
* **Langchain-Core (`langchain-core`):** Fornece as abstrações base e a Linguagem de Expressão LangChain (LCEL), que são os blocos de construção para criar e personalizar as cadeias de interações no Fida.
* **Dotenv (`python-dotenv`):** Utilizada para gerenciar variáveis de ambiente de forma segura, especialmente para carregar a chave da API da Groq a partir de um arquivo `.env` sem expô-la no código.
* **API da Groq:** Fornece o acesso ao modelo de linguagem grande (LLM) que gera as respostas conversacionais.

## 🚀 Como Instalar e Executar

Siga os passos abaixo para configurar e rodar o Fida em seu ambiente local:

1.  **Pré-requisitos:**
    * Certifique-se de ter o **Python 3** (versão 3.0 ou superior) instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).

2.  **Clone o Repositório (Opcional):**
    Se você ainda não tem os arquivos do projeto, clone este repositório:
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO_FIDA>
    cd Fida 
    ```
    Caso já tenha os arquivos, navegue até o diretório do projeto.

3.  **Crie um Ambiente Virtual (Recomendado):**
    É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.
    ```bash
    python -m venv venv
    ```
    Ative o ambiente virtual:
    * No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    * No macOS e Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as Dependências:**
    Com o ambiente virtual ativado, instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure a Chave da API da Groq:**
    * Crie um arquivo chamado `.env` na raiz do diretório do projeto.
    * Dentro do arquivo `.env`, adicione sua chave da API da Groq da seguinte forma:
        ```env
        API_KEY="SUA_CHAVE_API_DA_GROQ_AQUI"
        ```
    * Substitua `"SUA_CHAVE_API_DA_GROQ_AQUI"` pela sua chave real. Você pode obter uma chave da API no site da [GroqCloud](https://console.groq.com/keys).

6.  **Execute o Fida:**
    Após a instalação e configuração, execute o script principal:
    ```bash
    python Fida.py
    ```

## 📖 Como Usar

Ao iniciar o Fida, você verá um menu com as seguintes opções:

Fida

[1] Chat livre
[2] Consultar URL (link do site)
[3] Consultar vídeo do YouTube
[4] Consultar PDF

* Digite o número da opção desejada e pressione Enter.
* Siga as instruções para fornecer a URL, o link do YouTube ou o caminho do arquivo PDF, conforme a opção escolhida.
* Após o carregamento do documento (se aplicável), você poderá iniciar a conversa.
* Para encerrar a sessão de chat atual e retornar ao menu principal ou sair, digite `X` (ou `x`) e pressione Enter.
* Ao final de uma sessão, será perguntado se você deseja iniciar uma nova consulta ou encerrar o programa.

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Se você tem ideias para melhorar o Fida, encontrou algum bug ou quer adicionar novas funcionalidades, sinta-se à vontade para:

1.  Fazer um "fork" do projeto.
2.  Criar uma nova "branch" para sua feature (`git checkout -b feature/NovaFeature`).
3.  Fazer "commit" de suas alterações (`git commit -am 'Adiciona NovaFeature'`).
4.  Fazer "push" para a "branch" (`git push origin feature/NovaFeature`).
5.  Abrir um "Pull Request".
