import time
from concurrent import futures

import grpc

import bot
import bot_pb2
import bot_pb2_grpc


# defining grpc connection
class StockBotServicer(bot_pb2_grpc.StockBotServicer):
    def GetStock(self, request, context):
        response = bot_pb2.Stock()
        response.StockName = "AAPL"
        response.price = bot.GetPrice(request.StockName)
        return response

# create a grpc server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# add the defined class to the grpc server
bot_pb2_grpc.add_StockBotServicer_to_server(StockBotServicer(), server)

server.add_insecure_port('0.0.0.0:8060')
server.start()

# restart every now and then as server is not blocking
try:
   while True:
       time.sleep(8005)
except KeyboardInterrupt:
   server.stop(0)
