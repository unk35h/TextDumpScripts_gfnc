# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BattleBuffCfg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x42\x61ttleBuffCfg.proto\x12\rBattleBuffCfg\",\n\x08\x43\x66gTable\x12 \n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32\x12.BattleBuffCfg.Cfg\"\xd2\x04\n\x03\x43\x66g\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x0e\n\x06IsShow\x18\x03 \x01(\x08\x12\x0c\n\x04Icon\x18\x04 \x01(\t\x12\x0e\n\x06\x41\x63tion\x18\x05 \x01(\x05\x12\x10\n\x08ShowText\x18\x06 \x01(\x08\x12\x14\n\x0c\x43onflictSelf\x18\x07 \x01(\x08\x12\x13\n\x0b\x42uffGroupId\x18\x08 \x01(\x05\x12\r\n\x05Level\x18\t \x01(\x05\x12\x0f\n\x07MaxTier\x18\n \x01(\x05\x12\x13\n\x0bRefreshTier\x18\x0b \x01(\x08\x12\x12\n\nDispelType\x18\x0c \x01(\x05\x12\x0f\n\x07\x46\x65\x61ture\x18\r \x01(\t\x12\x11\n\tIsControl\x18\x0e \x01(\x08\x12\x12\n\nBreakSkill\x18\x0f \x01(\x08\x12\x19\n\x11ResistanceFormula\x18\x10 \x01(\x05\x12\x14\n\x0c\x44urationType\x18\x11 \x01(\x05\x12\x10\n\x08\x44uration\x18\x12 \x01(\x05\x12\x11\n\tSkillList\x18\x13 \x03(\x05\x12\x14\n\x0c\x45xtraBaseNum\x18\x14 \x01(\t\x12\x14\n\x0c\x45xtraTierNum\x18\x15 \x01(\t\x12\x13\n\x0b\x41\x63tiveAudio\x18\x16 \x01(\x05\x12\x13\n\x0b\x44ispelAudio\x18\x17 \x01(\x05\x12\x0f\n\x07MatShow\x18\x18 \x01(\x05\x12\x14\n\x0c\x43reationShow\x18\x19 \x03(\x05\x12\x13\n\x0b\x41ttributeID\x18\x1a \x03(\x05\x12\x0f\n\x07\x42\x61seNum\x18\x1b \x03(\x05\x12\x0f\n\x07TierNum\x18\x1c \x03(\x05\x12\x17\n\x0f\x44\x65\x61thBuffRetain\x18\x1d \x01(\x08\x12\x10\n\x08\x42uffType\x18\x1e \x01(\x05\x12\x10\n\x08\x42reakNum\x18\x1f \x01(\x05\x62\x06proto3')



_CFGTABLE = DESCRIPTOR.message_types_by_name['CfgTable']
_CFG = DESCRIPTOR.message_types_by_name['Cfg']
CfgTable = _reflection.GeneratedProtocolMessageType('CfgTable', (_message.Message,), {
  'DESCRIPTOR' : _CFGTABLE,
  '__module__' : 'BattleBuffCfg_pb2'
  # @@protoc_insertion_point(class_scope:BattleBuffCfg.CfgTable)
  })
_sym_db.RegisterMessage(CfgTable)

Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'BattleBuffCfg_pb2'
  # @@protoc_insertion_point(class_scope:BattleBuffCfg.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFGTABLE._serialized_start=38
  _CFGTABLE._serialized_end=82
  _CFG._serialized_start=85
  _CFG._serialized_end=679
# @@protoc_insertion_point(module_scope)
