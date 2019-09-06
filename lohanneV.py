from brain import lohanne_vision as eyeBalls
from brain import essentials
import glob

#Tokens Path

token = essentials.get_token('tokens/','caminho_tokens')
files = glob.glob('imagens/*')

analysys = []

for arquivo in files:
    analysys.append(eyeBalls.analisa_imagem(arquivo,token))

True









    

