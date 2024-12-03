import json
from pathlib import Path
import boto3
from botocore.exceptions import ClientError
from typing import List, Dict


def analyze_document_with_textract(image_name: str, output_file: str = "output.json") -> None:
    """
    Analisa um documento com AWS Textract e salva o resultado em um arquivo JSON.
    
    :param image_name: Nome do arquivo de imagem a ser analisado.
    :param output_file: Caminho do arquivo para salvar a resposta do Textract.
    """
    textract_client = boto3.client("textract")

    # Diretório padrão para imagens
    images_directory = Path(__file__).parent / "images"
    image_path = images_directory / image_name

    if not image_path.exists():
        print(f"Arquivo de imagem '{image_name}' não encontrado em '{images_directory}'.")
        return

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    try:
        response = textract_client.detect_document_text(Document={"Bytes": image_bytes})
        with open(output_file, "w") as json_file:
            json.dump(response, json_file, indent=4)
        print(f"Resultado salvo em '{output_file}'.")
    except ClientError as error:
        print(f"Erro ao processar o documento: {error}")


def extract_text_lines_from_response(response_file: str) -> List[str]:
    """
    Extrai todas as linhas de texto de um arquivo de resposta JSON do Textract.
    
    :param response_file: Caminho para o arquivo JSON contendo a resposta.
    :return: Lista de strings com o texto extraído por linha.
    """
    try:
        with open(response_file, "r") as file:
            response_data: Dict = json.load(file)
        blocks = response_data.get("Blocks", [])
        return [block["Text"] for block in blocks if block.get("BlockType") == "LINE"]
    except FileNotFoundError:
        print(f"Arquivo de resposta '{response_file}' não encontrado. Certifique-se de executar a análise primeiro.")
    except KeyError as e:
        print(f"Erro ao processar o arquivo de resposta: chave ausente {e}")
    return []


if __name__ == "__main__":
    # Nome do arquivo de imagem
    IMAGE_FILE = "lista-material-escolar.jpeg"
    RESPONSE_FILE = "output.json"

    # Analisa o documento se o arquivo JSON de resposta não existir
    if not Path(RESPONSE_FILE).exists():
        analyze_document_with_textract(IMAGE_FILE, RESPONSE_FILE)

    # Extrai as linhas de texto e as exibe
    lines = extract_text_lines_from_response(RESPONSE_FILE)
    if lines:
        print("Linhas extraídas do documento:")
        for line in lines:
            print(line)
    else:
        print("Nenhuma linha de texto foi extraída.")