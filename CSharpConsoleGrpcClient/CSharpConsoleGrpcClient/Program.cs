using System;
using System.Threading.Tasks;
using Grpc.Core;
using Grpc.Net.Client;

namespace CSharpConsoleGrpcClient
{
    class Program
    {
        static async Task Main(string[] args)
        {
            AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
            var connectionString = "http://localhost:50051";

            var input = new HelloRequest();
            input.Name = "C# Client";
            input.Greeting = "This is coming from .NET";

            var channelOptions = new GrpcChannelOptions();
            channelOptions.Credentials = ChannelCredentials.Insecure;

            var channel = GrpcChannel.ForAddress(connectionString, channelOptions);
            var client = new messenger.messengerClient(channel);

            var reply = await client.SayHelloAsync(input);

            Console.WriteLine("Waiting for the gRPC server");
            Console.WriteLine("------------------------------------");
            Console.WriteLine("Server said : " + reply);
        }
    }
}
