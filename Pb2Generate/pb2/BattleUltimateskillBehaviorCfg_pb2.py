# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BattleUltimateskillBehaviorCfg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$BattleUltimateskillBehaviorCfg.proto\x12\x1e\x42\x61ttleUltimateskillBehaviorCfg\"=\n\x08\x43\x66gTable\x12\x31\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32#.BattleUltimateskillBehaviorCfg.Cfg\" \n\x03\x43\x66g\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\r\n\x05Value\x18\x02 \x01(\x05\x62\x06proto3')



_CFGTABLE = DESCRIPTOR.message_types_by_name['CfgTable']
_CFG = DESCRIPTOR.message_types_by_name['Cfg']
CfgTable = _reflection.GeneratedProtocolMessageType('CfgTable', (_message.Message,), {
  'DESCRIPTOR' : _CFGTABLE,
  '__module__' : 'BattleUltimateskillBehaviorCfg_pb2'
  # @@protoc_insertion_point(class_scope:BattleUltimateskillBehaviorCfg.CfgTable)
  })
_sym_db.RegisterMessage(CfgTable)

Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'BattleUltimateskillBehaviorCfg_pb2'
  # @@protoc_insertion_point(class_scope:BattleUltimateskillBehaviorCfg.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFGTABLE._serialized_start=72
  _CFGTABLE._serialized_end=133
  _CFG._serialized_start=135
  _CFG._serialized_end=167
# @@protoc_insertion_point(module_scope)
