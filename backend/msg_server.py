from concurrent import futures
import time
from xmlrpc.client import Server

import grpc
import msg_pb2
import msg_pb2_grpc

class MessengerService(msg_pb2_grpc.messengerServicer):
    def SayHello(self, request, context):
        print("SayHello Request Made:")
        print(request)
        hello_reply = msg_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"
        
        return hello_reply    #Unary

    def ServerSaysHello(self, request, context):
        return super().ServerSaysHello(request, context)    #Server side streaming

    def NandinSaysHello(self, request_iterator, context):
        return super().NandinSaysHello(request_iterator, context)    #Client

    def InteractingHello(self, request_iterator, context):
        return super().InteractingHello(request_iterator, context)    #Bidirectional


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    msg_pb2_grpc.add_messengerServicer_to_server(MessengerService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__": 
    serve()