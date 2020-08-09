import grpc

# import the generated classes
from . import bot_pb2, bot_pb2_grpc


def GetData():
    # open a grpc channel
    channel = grpc.insecure_channel('stockytron_bot_1:8060')

    # generate a stub (client)
    stub = bot_pb2_grpc.StockBotStub(channel)

    # get the price of a requested stock
    stock = bot_pb2.StockRequest(StockName="AAPL")

    # get a response
    response = stub.GetStock(stock)

    return response
print(GetData())
