# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DataDescriptionHandler.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x44\x61taDescriptionHandler.proto\x12\x0f\x44\x61taDescripionH\"\x8a\x01\n\x10MessageUrlRecord\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08keyWords\x18\x04 \x01(\t\x12\x13\n\x0bwebsiteType\x18\x05 \x01(\t\x12\x0c\n\x04mood\x18\x06 \x01(\t\x12\x13\n\x0b\x63olorScheme\x18\x07 \x01(\t\"R\n\x15MessageUrlRecordImage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08RecordId\x18\x02 \x01(\x05\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0e\n\x06images\x18\x04 \x01(\x0c\"L\n\x16MessageUrlRecordStream\x12\x32\n\x07records\x18\x01 \x03(\x0b\x32!.DataDescripionH.MessageUrlRecord\"\x07\n\x05\x45mpty2\xb9\x01\n\x15\x44\x61taDescripionHandler\x12Q\n\x0eUploadMessages\x12\'.DataDescripionH.MessageUrlRecordStream\x1a\x16.DataDescripionH.Empty\x12M\n\x0bUploadImage\x12&.DataDescripionH.MessageUrlRecordImage\x1a\x16.DataDescripionH.Emptyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DataDescriptionHandler_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGEURLRECORD._serialized_start=50
  _MESSAGEURLRECORD._serialized_end=188
  _MESSAGEURLRECORDIMAGE._serialized_start=190
  _MESSAGEURLRECORDIMAGE._serialized_end=272
  _MESSAGEURLRECORDSTREAM._serialized_start=274
  _MESSAGEURLRECORDSTREAM._serialized_end=350
  _EMPTY._serialized_start=352
  _EMPTY._serialized_end=359
  _DATADESCRIPIONHANDLER._serialized_start=362
  _DATADESCRIPIONHANDLER._serialized_end=547
# @@protoc_insertion_point(module_scope)
