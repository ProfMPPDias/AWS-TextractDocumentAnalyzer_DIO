# AWS Textract Document Analyzer

Este projeto é um script Python para análise de texto em imagens utilizando o **AWS Textract**. Ele processa uma imagem, envia para o serviço Textract, e extrai o texto em um formato legível. O resultado é salvo em um arquivo JSON para futura referência e reutilização.

## **Funcionalidades**
1. Processar uma imagem para identificar texto usando AWS Textract.
2. Salvar a resposta da API em um arquivo JSON.
3. Extrair linhas de texto legíveis da resposta JSON.
4. Tratar erros de forma robusta, garantindo confiabilidade.

---

## **Pré-requisitos**

### 1. Dependências
- **Python** 3.7 ou superior.
- Bibliotecas Python:
  - `boto3`
  - `json`
  - `pathlib`
  - `typing`

Instale as dependências necessárias com o comando:
```bash
pip install boto3
```
### 2. Configuração do AWS Textract
- Certifique-se de ter uma conta AWS configurada.
- Configure as credenciais AWS no seu ambiente local:
```bash
aws configure
```
## **Como Usar**
Baixe o projeto e coloque a imagem que deseja processar no diretório images/.

Execute o script:
```bash
python main.py
```

## **Descrição Técnica**

1. Estrutura do Código
O script é dividido em duas funções principais:

analyze_document_with_textract:

- Lê a imagem em bytes e envia para a API do AWS Textract.
- Salva a resposta da API em um arquivo JSON.
- extract_text_lines_from_response:
- Lê o arquivo JSON gerado e filtra os blocos de texto para retornar apenas as linhas legíveis.

2. Tratamento de Erros
 
- Verifica se a imagem existe antes de processá-la.
- Valida a presença do arquivo JSON de resposta antes de tentar ler.
- Captura erros da API AWS Textract e exibe mensagens descritivas.

4. Modularidade
 
- Funções bem definidas facilitam a manutenção e reutilização.
- A resposta JSON é reutilizada para evitar reprocessamento.
- Insights Aprendidos

**Modularidade:**

- Dividir responsabilidades em funções específicas tornou o código mais claro e reutilizável.
Tratamento de Erros:

- Adicionar verificações e mensagens claras ajudou a identificar problemas rapidamente.
Salvamento de Respostas:

- Salvar o resultado da análise em JSON economizou chamadas repetidas à API, reduzindo custos na AWS.

**Portabilidade:**

O uso do Pathlib garantiu que o script funcione em diferentes sistemas operacionais.
