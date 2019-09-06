from brain import lohanne_vision as eyeBalls
from brain import essentials
import glob
from exemplos import exemplos_vision

files = glob.glob('imagens/*')

#Tokens Path
token = essentials.get_token('tokens/','caminho_tokens')
exemplos_vision.exemplo_rotulos(files,token)

analysys = []

for arquivo in files:
    analysys.append(eyeBalls.analisa_imagem(arquivo,token))









    

