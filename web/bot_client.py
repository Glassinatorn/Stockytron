import grpc

# import the generated classes
import bot_pb2
import bot_pb2_grpc

# open a grpc channel
channel = grpc.insecure_channel('stockytron_bot_1:8060')

# generate a stub (client)
stub = bot_pb2_grpc.StockBotStub(channel)

# get the price of a requested stock
stock = bot_pb2.Stock(StockName="AAPL")

# get a response
response = stub.GetStock(stock)

print(response)
