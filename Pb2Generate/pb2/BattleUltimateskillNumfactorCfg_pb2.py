# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BattleUltimateskillNumfactorCfg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%BattleUltimateskillNumfactorCfg.proto\x12\x1f\x42\x61ttleUltimateskillNumfactorCfg\">\n\x08\x43\x66gTable\x12\x32\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32$.BattleUltimateskillNumfactorCfg.Cfg\")\n\x03\x43\x66g\x12\x0e\n\x06Number\x18\x01 \x01(\x05\x12\x12\n\nMultiplier\x18\x02 \x01(\x05\x62\x06proto3')



_CFGTABLE = DESCRIPTOR.message_types_by_name['CfgTable']
_CFG = DESCRIPTOR.message_types_by_name['Cfg']
CfgTable = _reflection.GeneratedProtocolMessageType('CfgTable', (_message.Message,), {
  'DESCRIPTOR' : _CFGTABLE,
  '__module__' : 'BattleUltimateskillNumfactorCfg_pb2'
  # @@protoc_insertion_point(class_scope:BattleUltimateskillNumfactorCfg.CfgTable)
  })
_sym_db.RegisterMessage(CfgTable)

Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'BattleUltimateskillNumfactorCfg_pb2'
  # @@protoc_insertion_point(class_scope:BattleUltimateskillNumfactorCfg.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFGTABLE._serialized_start=74
  _CFGTABLE._serialized_end=136
  _CFG._serialized_start=138
  _CFG._serialized_end=179
# @@protoc_insertion_point(module_scope)