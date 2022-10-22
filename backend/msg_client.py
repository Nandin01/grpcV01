import msg_pb2
import msg_pb2_grpc
import time
import grpc

def run():
    with grpc.insecure_channel("localhost") as channel:
        stub = msg_pb2_grpc.messengerStub(channel)
        print("1.SayHello - Unary")
        print("2.ServerSaysHello - Server Side Streaming")
        print("3.NandinSaysHello - Client Side Streaming")
        print("4.InteractingHello - Bidirectional")
        rpc_call= input("Which rpc would you like to make?:")


        if rpc_call == "1":
            hello_request = msg_pb2.HelloRequest(greeting = "Hi", name = "Data")
            hello_reply = stub.SayHello(hello_request)
            print("Say Hello Response Recieved:")
            print(hello_reply)
        elif rpc_call == "2":
            print("not implemented")
        elif rpc_call == "3":
            print("not implemented")
        elif rpc_call == "4":
            print("not implemented")

if __name__ == "__main__":
    run()
