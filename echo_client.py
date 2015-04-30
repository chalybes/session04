import socket
import sys


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM,
                         socket.IPPROTO_IP)
    
    print >>log_buffer, 'connecting to {0} port {1}'.format(*server_address)
    
    sock.connect(server_address)
    
    try:
        print >>log_buffer, 'sending "{0}"'.format(msg)
        sock.sendall(msg)
        response = len(msg)
        while response is not 0:
            chunk = sock.recv(16)
            response -= len(chunk)
        print >>log_buffer, 'received "{0}"'.format(chunk)
    finally:
        print >>log_buffer, 'closing socket'
        sock.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usg = '\nusage: python echo_client.py "this is my message"\n'
        print >>sys.stderr, usg
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
