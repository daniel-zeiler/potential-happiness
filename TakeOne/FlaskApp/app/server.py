import grpc
from concurrent import futures
import time
from protos import open_ai_pb2_grpc


class OpenAIServicer(open_ai_pb2_grpc.OpenAIServicer):
    def __init__(self):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    open_ai_pb2_grpc.add_OpenAIServicer_to_server(OpenAIServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        print('started server')
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
