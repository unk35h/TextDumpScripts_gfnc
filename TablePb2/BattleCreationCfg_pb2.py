# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BattleCreationCfg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x42\x61ttleCreationCfg.proto\x12\x11\x42\x61ttleCreationCfg\"0\n\x08\x43\x66gTable\x12$\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32\x16.BattleCreationCfg.Cfg\"\xd3\x03\n\x03\x43\x66g\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0f\n\x07\x41udioId\x18\x02 \x01(\x05\x12\x16\n\x0eNeedShowEffect\x18\x03 \x01(\x08\x12\x0f\n\x07SrcName\x18\x04 \x01(\t\x12\x13\n\x0b\x42\x61seSrcPath\x18\x05 \x01(\t\x12\x10\n\x08LoadType\x18\x06 \x01(\x05\x12\x14\n\x0c\x45\x66\x66\x65\x63tEnable\x18\x07 \x01(\x08\x12\x11\n\tBirthType\x18\x08 \x01(\x05\x12\x12\n\nBirthPoint\x18\t \x01(\x05\x12\x10\n\x08\x44\x65stType\x18\n \x01(\x05\x12\x11\n\tDestPoint\x18\x0b \x01(\x05\x12\x10\n\x08\x42indType\x18\x0c \x01(\x05\x12\x11\n\tBindPoint\x18\r \x01(\x05\x12\x0f\n\x07\x44ieType\x18\x0e \x01(\x05\x12\x11\n\tRouteType\x18\x0f \x01(\x05\x12\r\n\x05Track\x18\x10 \x01(\x08\x12\r\n\x05Speed\x18\x11 \x01(\x05\x12\x12\n\nExistFrame\x18\x12 \x01(\x05\x12\x14\n\x0cMotionEasing\x18\x13 \x01(\x05\x12\x19\n\x11\x45\x66\x66\x65\x63tTriggerCode\x18\x14 \x01(\x05\x12\x19\n\x11TriggerCreationId\x18\x15 \x03(\x05\x12\x1c\n\x14TriggerCreationDelay\x18\x16 \x03(\x05\x12\x18\n\x10\x43reationBuffType\x18\x17 \x03(\x05\x62\x06proto3')



_CFGTABLE = DESCRIPTOR.message_types_by_name['CfgTable']
_CFG = DESCRIPTOR.message_types_by_name['Cfg']
CfgTable = _reflection.GeneratedProtocolMessageType('CfgTable', (_message.Message,), {
  'DESCRIPTOR' : _CFGTABLE,
  '__module__' : 'BattleCreationCfg_pb2'
  # @@protoc_insertion_point(class_scope:BattleCreationCfg.CfgTable)
  })
_sym_db.RegisterMessage(CfgTable)

Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'BattleCreationCfg_pb2'
  # @@protoc_insertion_point(class_scope:BattleCreationCfg.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFGTABLE._serialized_start=46
  _CFGTABLE._serialized_end=94
  _CFG._serialized_start=97
  _CFG._serialized_end=564
# @@protoc_insertion_point(module_scope)
