import socket
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.bind(address)
    # TODO: Set an option to allow the socket address to be reused immediately
    #       see the end of http://docs.python.org/2/library/socket.html
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # log that we are building a server
    print >>log_buffer, "making a server on {0}:{1}".format(*address)

    sock.listen(1)
    # TODO: bind your new sock 'sock' to the address above and begin to listen
    #       for incoming connections
    
    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print >>log_buffer, 'waiting for a connection'
            conn, addr = sock.accept()
            
            try:
                print >>log_buffer, 'connection - {0}:{1}'.format(*addr)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    data = conn.recv(32)
                    print >>log_buffer, 'received "{0}"'.format(data)

            finally:
                conn.close()

    except KeyboardInterrupt:
        # TODO: Use the python KeyboardIntterupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems
        conn.close()
        sys.exit(0)


if __name__ == '__main__':
    server()
    sys.exit(0)
