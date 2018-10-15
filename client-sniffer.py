# -*- coding: utf-8 -*-
# Echo client program
import socket
import sys

HOST = '127.0.0.7'      # The remote host
PORT = 7777             # The same port as used by the server
s = None

# =============================================================================
# Resolva o host e a porta na lista de entradas de informações de endereço. 
# Traduza o argumento host / port em uma sequência de 5 tuplas que contém 
# todos os argumentos necessários para criar um soquete conectado a 
# esse serviço. host é um nome de domínio, uma representação de string de 
# um endereço IPv4 / v6 ou Nenhum. port é um nome de serviço de cadeia de 
# caracteres, como 'http', um número de porta numérico ou Nenhum. 
# Ao passar None como o valor de host e port, você pode passar NULL para 
# a API C subjacente. Os argumentos family, type e proto podem ser 
# opcionalmente especificados para restringir a lista de endereços 
# retornados. Passar zero como um valor para cada um desses argumentos 
# seleciona o intervalo total de resultados.
# =============================================================================
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    # Atribui variáveis com o servidor criado
    af, socktype, proto, canonname, sa = res
    try:
        # soquete de classe (soquete): Uma subclasse de _socket.socket adicionando o método makefile ().
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        # Conecte o soquete a um endereço remoto. Para soquetes IP, o endereço é um par (host, porta).
        s.connect(sa)
    except OSError as msg:
        # Feche o soquete. Não pode ser usado após esta chamada.
        s.close()
        s = None
        continue
    break

if s is None:
    print('não foi possível abrir o soquete')
    # =============================================================================
    # Saia do interpretador levantando SystemExit (status). Se o status for 
    # omitido ou Nenhum, o padrão será zero (ou seja, sucesso). Se o status for 
    # um inteiro, ele será usado como o status de saída do sistema.
    # Se for outro tipo de objeto, ele será impresso e o status de 
    # saída do sistema será um (isto é, falha).
    # =============================================================================
    sys.exit(1)
    
with s:
    # =============================================================================
    # Envie uma string de dados para o soquete. Para o argumento opcional flags, 
    # veja o manual do Unix. Isso chama send () repetidamente até que todos 
    # os dados sejam enviados. Se ocorrer um erro, é impossível dizer 
    # quantos dados foram enviados.
    # =============================================================================
    s.sendall(b'Primeira mensagem')
    print('Enviado: Primeira mensagem')
    data = s.recv(1024)
    print('Recebido: ', repr(data))
    
    s.sendall(b'Segunda mensagem')
    print('Enviado: Segunda mensagem')
    data = s.recv(1024)
    print('Recebido: ', repr(data))
    
    s.sendall(b'Sair')
    print('Enviado: Sair')
    data = s.recv(1024)
    print('Recebido: ', repr(data))