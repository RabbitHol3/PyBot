def traduzir(texto_a_traduzir,token):
    # Importação das bibliotecas google
    from google.cloud import translate as tradutor
    from google.oauth2 import service_account
    
    #Autentica credenciais
    credenciais = service_account.Credentials.from_service_account_file(f'{token}')

    # Instancia o cliente
    cliente_tradutor = tradutor.Client(credentials=credenciais)

    # Texto a traduzir
    texto = texto_a_traduzir
    # Lingua a traduzir
    target = 'pt-BR'

    # Translates some text into Russian
    traducao = cliente_tradutor.translate(
        texto,
        target_language=target)

    return traducao['translatedText'].capitalize()