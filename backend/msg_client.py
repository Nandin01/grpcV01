import msg_pb2
import msg_pb2_grpc
import time
import grpc

def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")

        if name == "":
            break

        hello_request = msg_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = msg_pb2_grpc.messengerStub(channel)
        print("1.SayHello - Unary")
        print("2.ServerSaysHello - Server Side Streaming")
        print("3.NandinSaysHello - Client Side Streaming")
        print("4.InteractingHello - Bidirectional")
        rpc_call= input("Which rpc would you like to make?:")


        if rpc_call == "1":
            hello_request = msg_pb2.HelloRequest(greeting = "--- This is Python Client Unary RPC ---", name = "Python Client")
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
