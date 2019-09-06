from google.cloud import vision
import io
import os
from google.oauth2 import service_account

def analisa_imagem(path,token):
    """Analisa imagem"""
    credenciais = service_account.Credentials.from_service_account_file(f'{token}')

    print('Credenciais: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))
    cliente = vision.ImageAnnotatorClient(credentials=credenciais)

    with io.open(path, 'rb') as arquivo_imagem:
        conteudo = arquivo_imagem.read()

    imagem = vision.types.Image(content=conteudo)

    resposta = cliente.label_detection(image=imagem)
    resposta_caracteristicas = resposta.label_annotations
    print('Caracteristicas:')
    caracteristicas_arr = []
    
    for caracteristicas in resposta_caracteristicas:
        caracteristicas_arr.append(caracteristicas)

    return caracteristicas_arr