import socket
import sys
from datetime import *

# IP do server
HOST = "127.0.0.7"
# Porta
PORT = 7777

s = None

# =============================================================================
# Resolva o host e a porta na lista de entradas de informações de endereço. 
# Traduza o argumento host / port em uma sequência de 5 tuplas que contém 
# todos os argumentos necessários para criar um soquete conectado a esse serviço. 
# host é um nome de domínio, uma representação de string de um endereço IPv4 / v6 ou Nenhum. 
# port é um nome de serviço de cadeia de caracteres, como 'http', um número de porta numérico ou Nenhum. 
# Ao passar None como o valor de host e port, você pode passar NULL para a API C subjacente. 
# Os argumentos family, type e proto podem ser opcionalmente especificados para 
# restringir a lista de endereços retornados. Passar zero como um valor para cada 
# um desses argumentos seleciona o intervalo total de resultados.
# =============================================================================
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    # Atribui variáveis com o servidor criado
    af, socktype, proto, canonname, sa = res
    
    try:
        # soquete de classe (soquete): Uma subclasse de _socket.socket adicionando o método makefile ().
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        # =============================================================================
        # Vincule o soquete a um endereço local. Para soquetes IP, 
        # o endereço é um par (host, porta); o host deve se referir ao host local. 
        # Para soquetes de pacotes brutos, o endereço é uma tupla 
        # (ifname, proto [, pkttype [, hatype]])
        # s.bind(sa)
        # =============================================================================
        s.bind(sa)
        print('\nServidor iniciado...IP: ', sa[0], 'PORTA: ', sa[1],' em: ',
              datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
        # =============================================================================
        # Ative um servidor para aceitar conexões. Se o backlog for especificado, 
        # ele deve ser pelo menos 0 (se for menor, é definido como 0); especifica 
        # o número de conexões não aceitas que o sistema permitirá antes de recusar 
        # novas conexões. Se não especificado, um valor razoável padrão é escolhido.
        # =============================================================================
        s.listen(1)
    except OSError as msg:
        # Feche o soquete. Não pode ser usado após esta chamada.
        s.close()
        s = None
        continue
    break

# Valida abertura do soquete
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

# =============================================================================
# Aguarda por uma conexão de entrada. Retorna um novo soquete representando 
# a conexão e o endereço do cliente. Para soquetes IP, as informações de endereço 
# são um par (hostaddr, port).
# =============================================================================
hostaddr, port = s.accept()
with hostaddr:
    print('Conectado por: ', port)
    while True:
        # =============================================================================
        # Receba até bytes buffersize do soquete. Para o argumento opcional flags, 
        # veja o manual do Unix. Quando não houver dados disponíveis, 
        # bloqueie até que pelo menos um byte esteja disponível ou até que 
        # a extremidade remota seja fechada. Quando a extremidade remota 
        # é fechada e todos os dados são lidos, retorne a string vazia.
        # =============================================================================
        data = hostaddr.recv(1024)
        if not data: break
        print('\nDados recebidos do client: <', data ,'> Em: ',
              datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
        if data == b'Primeira mensagem':
            # =============================================================================
            # Envie uma string de dados para o soquete. Para o argumento opcional 
            # flags, veja o manual do Unix. Retorna o número de bytes enviados; 
            # isso pode ser menor que len (dados) se a rede estiver ocupada.
            # =============================================================================
            hostaddr.send(b'Primeira mensagem: primeira mensagem solicitada.')
        elif data == b'Segunda mensagem':
            # =============================================================================
            # Envie uma string de dados para o soquete. Para o argumento opcional 
            # flags, veja o manual do Unix. Retorna o número de bytes enviados; 
            # isso pode ser menor que len (dados) se a rede estiver ocupada.
            # =============================================================================
            hostaddr.send(b'Segunda mensagem: segunda mensagem solicitada.')
        elif data == b'Sair':
            # =============================================================================
            # Envie uma string de dados para o soquete. Para o argumento opcional 
            # flags, veja o manual do Unix. Retorna o número de bytes enviados; 
            # isso pode ser menor que len (dados) se a rede estiver ocupada.
            # =============================================================================
            hostaddr.send(b'Fim!')
        else:
            hostaddr.send(b'Nada foi enviado para o servidor!')