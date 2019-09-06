from google.cloud import vision
import io
import os
from google.oauth2 import service_account

def analisa_imagem(path,token):
    """Analisa imagem"""
    credenciais = service_account.Credentials.from_service_account_file(f'{token}')

    #print('Credenciais: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))
    cliente = vision.ImageAnnotatorClient(credentials=credenciais)

    with io.open(path, 'rb') as arquivo_imagem:
        conteudo = arquivo_imagem.read()

    imagem = vision.types.Image(content=conteudo)
    
    resposta = cliente.label_detection(image=imagem)
    resposta_caracteristicas = resposta.label_annotations
    print('Caracteristicas:')
    caracteristicas_arr = []

    for caracteristicas in resposta_caracteristicas:
        print(caracteristicas)
        caracteristicas_arr.append(caracteristicas)

    return caracteristicas_arr

def rotulos_imagem(file_path,token):
    import io
    import os
    import brain.tradutor_lib as tradutor
    import json
    #Bibliotecas Google
    from google.cloud import vision
    from google.cloud.vision import types
    from google.oauth2 import service_account
    
    #[Autentica credenciais]
    credenciais = service_account.Credentials.from_service_account_file(f'{token}')

    # Estancia cliente
    cliente = vision.ImageAnnotatorClient(credentials=credenciais)
    
    # Nome do arquivo
    arquivo_nome = os.path.abspath(file_path)
    
    # Carrega imagem na memoria
    with io.open(arquivo_nome, 'rb') as image_file:
        conteudo = image_file.read()
    imagem = types.Image(content=conteudo)
    
    # detecta rotulos da imagem
    return cliente.label_detection(image=imagem)
    
