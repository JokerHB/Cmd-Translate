#coding=utf8

import readline
import sys
import JsonServer
import HttpServer

js = JsonServer.JsonDecode()
hp = HttpServer.HttpServer()

def main(argv=None):
    if argv != None:
        if argv == 'exit()':
            return None
        print js.decode(hp.querry(argv))
        return None
    while True:
        content = raw_input('>')
        if content == 'exit()':
            return None
        print js.decode(hp.querry(content))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        sys.exit(int(main(sys.argv[1]) or 0))
    sys.exit(int(main() or 0))
