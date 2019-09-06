'''essentials'''

def get_token(path,token=None):
    from os import listdir
    from os.path import isfile, join
    import glob
    tokens_list = glob.glob(f'{path}{token}.txt')
    if len(tokens_list) is not 1 or len(tokens_list) is 0:
        raise 'Token não existe ou há mais de um'
    else:
        path_token =  open(tokens_list[0],'r').read()
        return glob.glob(f'{path_token}*')[0]