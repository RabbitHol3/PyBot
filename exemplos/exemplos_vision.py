def exemplo_rotulos(arquivos,token):
    
    #importação lib de vision
    from brain import lohanne_vision as eyeBalls
    #importação lib de tradução
    from brain import tradutor_lib

    for arquivo in arquivos:
        #resposta do vision
        resposta = eyeBalls.rotulos_imagem(arquivo,token)    

        #PRINT - COMEÇO
        rotulos = resposta.label_annotations

        print('\n')
        string_traduzir = ''
        scores_print = []

        for i in range(len(rotulos)):  
            string_traduzir += f' {rotulos[i].description} - '
            scores_print.append(rotulos[i].score)

        rotulos_traduzidos = tradutor_lib.traduzir(string_traduzir,token).replace('-','').title().split('  ')
        titulo_print = 'Caracteristicas'
        print(f'{titulo_print:=^20}')
        for j in range(len(rotulos_traduzidos)):
            print(f'Pontos: {scores_print[j] * 10:_<20.2f} {rotulos_traduzidos[j]}')

        #PRINT FIM
