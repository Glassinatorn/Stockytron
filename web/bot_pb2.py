# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bot.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bot.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tbot.proto\"!\n\x0cStockRequest\x12\x11\n\tStockName\x18\x01 \x01(\t\")\n\x05Stock\x12\x11\n\tStockName\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x32/\n\x08StockBot\x12#\n\x08GetStock\x12\r.StockRequest\x1a\x06.Stock\"\x00\x62\x06proto3'
)




_STOCKREQUEST = _descriptor.Descriptor(
  name='StockRequest',
  full_name='StockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='StockName', full_name='StockRequest.StockName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=46,
)


_STOCK = _descriptor.Descriptor(
  name='Stock',
  full_name='Stock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='StockName', full_name='Stock.StockName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='Stock.price', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['StockRequest'] = _STOCKREQUEST
DESCRIPTOR.message_types_by_name['Stock'] = _STOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StockRequest = _reflection.GeneratedProtocolMessageType('StockRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOCKREQUEST,
  '__module__' : 'bot_pb2'
  # @@protoc_insertion_point(class_scope:StockRequest)
  })
_sym_db.RegisterMessage(StockRequest)

Stock = _reflection.GeneratedProtocolMessageType('Stock', (_message.Message,), {
  'DESCRIPTOR' : _STOCK,
  '__module__' : 'bot_pb2'
  # @@protoc_insertion_point(class_scope:Stock)
  })
_sym_db.RegisterMessage(Stock)



_STOCKBOT = _descriptor.ServiceDescriptor(
  name='StockBot',
  full_name='StockBot',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=91,
  serialized_end=138,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStock',
    full_name='StockBot.GetStock',
    index=0,
    containing_service=None,
    input_type=_STOCKREQUEST,
    output_type=_STOCK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STOCKBOT)

DESCRIPTOR.services_by_name['StockBot'] = _STOCKBOT

# @@protoc_insertion_point(module_scope)