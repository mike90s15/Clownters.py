#!/usr/bin/env python
#create by Mike Edwards
# Em desenvolvimento #

#lib 
import os
import platform
import webbrowser
import time
import datetime
import random
try:
    import requests
except:
    os.system('pip isntall requests')
    import requests

def main():
    clear()
    #links()
    clear()
    func = {1:banco, 2:bin, 3:cep, 4:cnpj, 5:ddd, 6:ip, 7:geradorCnpj, 8:geradorCpf}
    while True:
        bannerMenu()
        option = input('\n\033[1;34m ===> \033[1;36m').strip()
        if readInput(option, 'empty'): continue
        if option.lower() == 'q': return 0
        if readInput(option, 'numeric') != True: continue
        if int(option) == 99 or int(option) == 0: return 0
        if int(option) > 10:
            print(' option invalida!')
            time.sleep(1)
            continue
        str(func[int(option)]())

def sair():
    banner()
    print('\033[1;34m Obrigado por usar o painel Clownters\n Telegram: @Clownters\n YouTube: @Clownters1')
    exit()


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def links():
    if platform.system() == 'Linux':
        os.system  ('xdg-open https://instagram.com/mike90s15 &>/dev/null; clear')
        time.sleep(5)
        os.system('xdg-open https://twitter.com/mike90s15 &>/dev/null; clear')
        time.sleep(5)
        os.system('xdg-open https://github.com/mike90s15 &>/dev/null; clear')
        time.sleep(5)
    else:
        webbrowser.open('https://instagram.com/mike90s15')
        time.sleep(5)
        webbrowser.open('https://twitter.com/mike90s15')
        time.sleep(5)
        webbrowser.open('https://github.com/mike90s15')


def banner():
    clear()
    banner = ["\n \033[1;33m" ".--------.____________", "|| ° ° ° °     .2021.|| \033[1;32m®\033[1;33m", "||                    | \033[1;32m©\033[1;33m", "||\     ______________________", "|| \   // ° ° ° ° ° ° ° ° ° °/", "||\ \ //                    /", "|| \ //                    /", "||\ //                    /", "|| //                    /", "||//                    /", "||/                    /", "|/____________________/", "\033[1;31mArquivo Clownters \033[m\n", "\033[1;35m<<<   PAINEL CLOWNTERS " + str(datetime.date.today()) + "   >>>", "\033[1;32m=======================================\n"]
    for i in banner:
        print('', i)
        time.sleep(0.01)


def bannerMenu():
    banner()
    #banner_menu = ['Buscas', 'Geradores', 'Moedas', 'Validadores', 'Calculos', 'cep']
    banner_menu = ['Consulta de Banco', 'Consulta de Bin', 'Consulta de CEP', 'Consulta de CNPJ', 'Consulta de IP', 'Consulta de DDD']
    geradores = ['Gerador de CPF', 'Gerador de CNPJ']
    banner_menu = banner_menu + geradores
    a = 0
    for i in sorted(banner_menu):
        a += 1
        print(f' \033[1;32m[\033[m\033[1;36m0{a}\033[1;32m]\033[m \033[1;36m{str(i): <17}    \033[1;32m]\033[m\033[1;32m       (+_+)')
    print('\n \033[1;32m[\033[m\033[1;31m99\033[1;32m]\033[m \033[1;36mSair\t\t   \033[1;32m]\033[m\033[1;32m       (+_+)')
    

def readInput(x, typ):
    match  typ:
        case 'numeric':
            if x.isnumeric(): return True
            else: print('\033[1;33m Digite apenas números!')
            time.sleep(2)
        case 'isalpha':
            if x.isalpha(): return True
            else: print('\033[1;33m Digite apenas letras!')
            time.sleep(2)
        case 'isalnum':
            if x.isalnum(): return True
            else: print('\033[1;33m Digite apenas números e letras!')
            time.sleep(2)
        case 'empty':
            if len(x) == 0 or x.isspace():
                print('\033[1;33m Digite alguma coisa!')
                time.sleep(2)
                return True
        case other: return False


def retorneMenu():
    lst = ['Continue', 'Retorne para o menu', 'Sair do menu']
    print('\n', '=' * 39, '\n\n\033[1;34m Continue ou retornar ao menu principal?\n')
    a = 0
    for i in lst:
        a += 1
        if a == 3: a = 00
        print(f' \033[1;32m[\033[m\033[1;36m0{a}\033[1;32m]\033[m \033[1;36m{str(i): <19.19}    \033[1;32m]\033[m\033[1;32m     (+_+)')
        time.sleep(0.01)
    input_user = input('\n\033[1;34m ===> \033[1;36m').strip()
    if input_user.replace(' ', '') == '': return False
    elif input_user.lower() == 'q': return True
    elif input_user.isnumeric() == False: return False
    if int(input_user) == 0: exit()
    elif int(input_user) == 2: return True

# Funções de busca
def banco():
     while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o codigo para a consulta\n ===> \033[1;36m').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            break             
        req = requests.get(f'https://brasilapi.com.br/api/banks/v1/{input_user}').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <8}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True
    

def bin():
     while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o bin para a consulta\n ===> \033[1;36m').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            break 
        req = requests.get(f'https://lookup.binlist.net/{input_user}').json()
        print()
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <7}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True


def cep():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o CEP para a consulta\n ===> \033[1;36m').strip().replace('-', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            if len(input_user) != 8:
                print('\033[1;33m O cep é formado por 8 digitos númerico!')
                time.sleep(2)
                continue
            break               
        req = requests.get(f'https://viacep.com.br/ws/{input_user}/json/').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <11}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True


def cnpj():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o CNPJ para a consulta\n ===> \033[1;36m').strip().replace('.', '').replace('-', '').replace('/', '')
            print(input_user)
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            if len(input_user) != 14:
                print('\033[1;33m O cep é formado por 8 digitos númerico!')
                time.sleep(2)
                continue
            break               
        req = requests.get(f'https://brasilapi.com.br/api/cnpj/v1/${input_user}').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <11}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True
    

def ddd():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o DDD para a consulta\n ===> \033[1;36m').strip().replace('0', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            if len(input_user) != 2:
                print('\033[1;33m O número não corresponde ao um DDD existente!')
                time.sleep(2)
                continue
            break
        req = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{input_user}').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <6}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True


def ip():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o ip para a consulta\n ===> \033[1;36m').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            #if readInput(input_user, 'numeric') != True: continue
            break
        req = requests.get(f'http://ip-api.com/json/{input_user}').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <11}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True

# Funções de geredores
def geradorCpf():
    while True:
        banner()
        soma = 0
        var = ''
        for i in range(0, 8): var = var + str(random.randint(0, 9))
        var = var + '8'
        #var = '435231910'
        num = 11
        for i in range(0, 9):
            num -= 1
            soma += int(var[i:i+1]) * num
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        var = var + str(soma)
        soma = 0
        num = 11
        for i in range(0, 10):
            soma += int(var[i:i+1]) * num
            num -= 1
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        var = var + str(soma)
        print(f'\033[1;34m CPF gerado:\033[0;32m {var}\n\033[1;34m CPF gerado:\033[0;32m {var[0:3]}.{var[3:6]}.{var[6:9]}-{var[9:]}')
        if retorneMenu() == True: return True


def geradorCnpj():
    while True:
        banner()
        var = ''
        soma = 0
        for i in range(0, 8):
            var = var + str(random.randint(0,9))
        var = var + '0001'
        num = 6
        #var = '112223330001'
        for i in range(0, 12):
            num -= 1
            if num < 2: num = 9
            soma += int(var[i:i+1]) * num
        if (soma % 11) < 2: var = var + '0'
        else: var = var + str(11 - (soma % 11))
        soma = 0 
        num = 6
        for i in range(0, 13):
            soma += int(var[i:i+1]) * num
            num -= 1
            if num < 2: num = 9
        if (soma % 11) < 2: var = var + '0'
        else: var = var + str(11 - (soma % 11))
        print(f'\033[1;34m CNPJ gerado:\033[0;32m {var}\n\033[1;34m CNPJ gerado:\033[0;32m {var[0:2]}.{var[2:5]}.{var[5:8]}/{var[8:12]}-{var[12:]}')
        if retorneMenu() == True: return True

if __name__ == '__main__':
    try: 
        main()
        time.sleep(1)
        sair()
    except KeyboardInterrupt:
        print('\n\033[1;33m Programa interrompido pelo usuário')
        time.sleep(2)
        sair()
    except EOFError: 
        print('\n\033[1;33m Programa interrompido pelo usuário')
        time.sleep(2)
        sair()