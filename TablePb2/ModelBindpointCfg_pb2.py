# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ModelBindpointCfg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17ModelBindpointCfg.proto\x12\x11ModelBindpointCfg\"0\n\x08\x43\x66gTable\x12$\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32\x16.ModelBindpointCfg.Cfg\"\x1f\n\x03\x43\x66g\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0c\n\x04Path\x18\x02 \x01(\tb\x06proto3')



_CFGTABLE = DESCRIPTOR.message_types_by_name['CfgTable']
_CFG = DESCRIPTOR.message_types_by_name['Cfg']
CfgTable = _reflection.GeneratedProtocolMessageType('CfgTable', (_message.Message,), {
  'DESCRIPTOR' : _CFGTABLE,
  '__module__' : 'ModelBindpointCfg_pb2'
  # @@protoc_insertion_point(class_scope:ModelBindpointCfg.CfgTable)
  })
_sym_db.RegisterMessage(CfgTable)

Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'ModelBindpointCfg_pb2'
  # @@protoc_insertion_point(class_scope:ModelBindpointCfg.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFGTABLE._serialized_start=46
  _CFGTABLE._serialized_end=94
  _CFG._serialized_start=96
  _CFG._serialized_end=127
# @@protoc_insertion_point(module_scope)