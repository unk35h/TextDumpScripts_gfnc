# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DormFightWeaponCfg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x44ormFightWeaponCfg.proto\x12\x12\x44ormFightWeaponCfg\"1\n\x08\x43\x66gTable\x12%\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32\x17.DormFightWeaponCfg.Cfg\"\xc1\x01\n\x03\x43\x66g\x12\x10\n\x08WeaponId\x18\x01 \x01(\x05\x12\x0c\n\x04Type\x18\x02 \x01(\x05\x12\x13\n\x0b\x41ttackValue\x18\x03 \x01(\x05\x12\x12\n\nThrowForce\x18\x04 \x01(\x01\x12\x12\n\nPickEpCost\x18\x05 \x01(\x05\x12\x12\n\nHoldEpCost\x18\x06 \x01(\x05\x12\x13\n\x0bThrowEpCost\x18\x07 \x01(\x05\x12\x10\n\x08PickSeId\x18\x08 \x01(\x05\x12\x11\n\tThrowSeId\x18\t \x01(\x05\x12\x0f\n\x07HitSeId\x18\n \x01(\x05\x62\x06proto3')



_CFGTABLE = DESCRIPTOR.message_types_by_name['CfgTable']
_CFG = DESCRIPTOR.message_types_by_name['Cfg']
CfgTable = _reflection.GeneratedProtocolMessageType('CfgTable', (_message.Message,), {
  'DESCRIPTOR' : _CFGTABLE,
  '__module__' : 'DormFightWeaponCfg_pb2'
  # @@protoc_insertion_point(class_scope:DormFightWeaponCfg.CfgTable)
  })
_sym_db.RegisterMessage(CfgTable)

Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'DormFightWeaponCfg_pb2'
  # @@protoc_insertion_point(class_scope:DormFightWeaponCfg.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFGTABLE._serialized_start=48
  _CFGTABLE._serialized_end=97
  _CFG._serialized_start=100
  _CFG._serialized_end=293
# @@protoc_insertion_point(module_scope)
