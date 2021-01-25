import argparse

import core.socket as socket

parser = argparse.ArgumentParser()
parser.add_argument("-s", action='store_true', help='start server')
parser.add_argument("-c", action='store_true', help='start client')

args = parser.parse_args()

if __name__ == '__main__':
    if args.s:
        socket.start_server()
    elif args.c:
        socket.start_client()
    else:
        print("nothing to do")