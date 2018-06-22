#!/usr/local/bin/python3
import socket
import json
import time

class SocketWriter():
    def __init__(self, address = "/tmp/socket" ):
        self.address = address

    def formatSingle(self, change):
        if ( isinstance(change, dict) ):
            try:
                change = json.dumps(change)
            except:
                print("couldn't convert: ", change)
        else:
            try:
                change = str(change)
            except:
                print("couldn't convert: ", change)
        return change


    def sendNewDeviceResponse(self, value, m_type, sender):
        message = """{"message_type": "new_device", "value": "%s", "type" : "%s", "sender": "%s"}""" % (self.formatSingle(value), self.formatSingle(m_type), self.formatSingle(sender))
        self.writeResponse(message)

    def writeResponse(self, response):
            # print('Connecting to {}.'.format(config.RESP_SOCK_ADDR))
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            count = 0
            while count < 5:
                try:
                    sock.connect(self.address)
                    break
                except socket.error as msg:
                    # print(msg)
                    time.sleep(.1)
                    count +=1
            if count == 5:
                self.sock = None
                print("Unable to connect to Iotivity response socket.")

            if sock != None:
                try:
                    message = bytes(response, 'utf-8')
                    print('Sending response to Iotivity:\n',json.dumps(json.loads(message.decode("utf-8")), indent=4),"\n\n")
                    # print('sending {!r}'.format(message))
                    sock.sendall(message)
                finally:
                    print('closing socket')
                    sock.close()
