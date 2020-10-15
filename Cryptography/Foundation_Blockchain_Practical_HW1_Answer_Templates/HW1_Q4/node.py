import json
import threading
import sys
from stream import Stream


class Node:
    def __init__(self,
                 uid=None,
                 next=None):

        ''' Network Variables '''
        self.stream = Stream()
        self.address = (self.stream.ip, self.stream.port)
        
        ''' Algorithm Variables '''
        self.uid = uid
        print('node', uid, 'initialized successfully with address:', self.address)

    def run(self):
        while True:
            stream_in_buff = self.stream.read_in_buf()
            for message in stream_in_buff:
                self.handle_message(message)

    def handle_message(self, message):
        print('node', self.uid, "received: ", message)
        # DO SOMETHING WITH MESSAGE
        # USE 'self.send_message' FOR SENDING MESSAGES
        # REMEMBER THAT CHANNELS HAVE DELAYS
        if message>self.uid:
            self.send_message(message)
        elif message<self.uid:
            self.send_message(self.uid)
        elif message[-6:]=='leader'
            leaderUID = [int(s) for s in a.split() if s.isdigit()]
            leaderUID = str(leaderUID[0])
            print('node', self.uid, ": node "+leaderUID+"is leader")
        else:
            self.send_message('Node ',self.uid,'is leader')
            print('node', self.uid, ": I'm leader ! ")
            
    def send_message(self, msg):
        self.stream.add_message_to_out_buff(msg)
        self.stream.send_messages()