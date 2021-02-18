# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: descarteslabs/common/proto/typespec/typespec.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='descarteslabs/common/proto/typespec/typespec.proto',
  package='descarteslabs.workflows',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2descarteslabs/common/proto/typespec/typespec.proto\x12\x17\x64\x65scarteslabs.workflows\"\xeb\x01\n\x08Typespec\x12\x42\n\tprimitive\x18\x01 \x01(\x0b\x32\".descarteslabs.workflows.PrimitiveH\x00R\tprimitive\x12\x14\n\x04type\x18\x02 \x01(\tH\x00R\x04type\x12\x30\n\x03map\x18\x03 \x01(\x0b\x32\x1c.descarteslabs.workflows.MapH\x00R\x03map\x12\x46\n\tcomposite\x18\x04 \x01(\x0b\x32&.descarteslabs.workflows.CompositeTypeH\x00R\tcompositeB\x0b\n\tcomponent\"t\n\tPrimitive\x12\x13\n\x04int_\x18\x01 \x01(\x05H\x00R\x03int\x12\x17\n\x06\x66loat_\x18\x02 \x01(\x02H\x00R\x05\x66loat\x12\x15\n\x05\x62ool_\x18\x03 \x01(\x08H\x00R\x04\x62ool\x12\x19\n\x07string_\x18\x04 \x01(\tH\x00R\x06stringB\x07\n\x05value\"y\n\rMapFieldEntry\x12\x33\n\x03key\x18\x01 \x01(\x0b\x32!.descarteslabs.workflows.TypespecR\x03key\x12\x33\n\x03val\x18\x02 \x01(\x0b\x32!.descarteslabs.workflows.TypespecR\x03val\"C\n\x03Map\x12<\n\x05items\x18\x01 \x03(\x0b\x32&.descarteslabs.workflows.MapFieldEntryR\x05items\"^\n\rCompositeType\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x39\n\x06params\x18\x02 \x03(\x0b\x32!.descarteslabs.workflows.TypespecR\x06paramsb\x06proto3'
)




_TYPESPEC = _descriptor.Descriptor(
  name='Typespec',
  full_name='descarteslabs.workflows.Typespec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='primitive', full_name='descarteslabs.workflows.Typespec.primitive', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='primitive', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='descarteslabs.workflows.Typespec.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map', full_name='descarteslabs.workflows.Typespec.map', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='map', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='composite', full_name='descarteslabs.workflows.Typespec.composite', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='composite', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='component', full_name='descarteslabs.workflows.Typespec.component',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=80,
  serialized_end=315,
)


_PRIMITIVE = _descriptor.Descriptor(
  name='Primitive',
  full_name='descarteslabs.workflows.Primitive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_', full_name='descarteslabs.workflows.Primitive.int_', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='int', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='float_', full_name='descarteslabs.workflows.Primitive.float_', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='float', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_', full_name='descarteslabs.workflows.Primitive.bool_', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bool', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_', full_name='descarteslabs.workflows.Primitive.string_', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='string', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='value', full_name='descarteslabs.workflows.Primitive.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=317,
  serialized_end=433,
)


_MAPFIELDENTRY = _descriptor.Descriptor(
  name='MapFieldEntry',
  full_name='descarteslabs.workflows.MapFieldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='descarteslabs.workflows.MapFieldEntry.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='val', full_name='descarteslabs.workflows.MapFieldEntry.val', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='val', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=435,
  serialized_end=556,
)


_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='descarteslabs.workflows.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='descarteslabs.workflows.Map.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='items', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=558,
  serialized_end=625,
)


_COMPOSITETYPE = _descriptor.Descriptor(
  name='CompositeType',
  full_name='descarteslabs.workflows.CompositeType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='descarteslabs.workflows.CompositeType.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='descarteslabs.workflows.CompositeType.params', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=627,
  serialized_end=721,
)

_TYPESPEC.fields_by_name['primitive'].message_type = _PRIMITIVE
_TYPESPEC.fields_by_name['map'].message_type = _MAP
_TYPESPEC.fields_by_name['composite'].message_type = _COMPOSITETYPE
_TYPESPEC.oneofs_by_name['component'].fields.append(
  _TYPESPEC.fields_by_name['primitive'])
_TYPESPEC.fields_by_name['primitive'].containing_oneof = _TYPESPEC.oneofs_by_name['component']
_TYPESPEC.oneofs_by_name['component'].fields.append(
  _TYPESPEC.fields_by_name['type'])
_TYPESPEC.fields_by_name['type'].containing_oneof = _TYPESPEC.oneofs_by_name['component']
_TYPESPEC.oneofs_by_name['component'].fields.append(
  _TYPESPEC.fields_by_name['map'])
_TYPESPEC.fields_by_name['map'].containing_oneof = _TYPESPEC.oneofs_by_name['component']
_TYPESPEC.oneofs_by_name['component'].fields.append(
  _TYPESPEC.fields_by_name['composite'])
_TYPESPEC.fields_by_name['composite'].containing_oneof = _TYPESPEC.oneofs_by_name['component']
_PRIMITIVE.oneofs_by_name['value'].fields.append(
  _PRIMITIVE.fields_by_name['int_'])
_PRIMITIVE.fields_by_name['int_'].containing_oneof = _PRIMITIVE.oneofs_by_name['value']
_PRIMITIVE.oneofs_by_name['value'].fields.append(
  _PRIMITIVE.fields_by_name['float_'])
_PRIMITIVE.fields_by_name['float_'].containing_oneof = _PRIMITIVE.oneofs_by_name['value']
_PRIMITIVE.oneofs_by_name['value'].fields.append(
  _PRIMITIVE.fields_by_name['bool_'])
_PRIMITIVE.fields_by_name['bool_'].containing_oneof = _PRIMITIVE.oneofs_by_name['value']
_PRIMITIVE.oneofs_by_name['value'].fields.append(
  _PRIMITIVE.fields_by_name['string_'])
_PRIMITIVE.fields_by_name['string_'].containing_oneof = _PRIMITIVE.oneofs_by_name['value']
_MAPFIELDENTRY.fields_by_name['key'].message_type = _TYPESPEC
_MAPFIELDENTRY.fields_by_name['val'].message_type = _TYPESPEC
_MAP.fields_by_name['items'].message_type = _MAPFIELDENTRY
_COMPOSITETYPE.fields_by_name['params'].message_type = _TYPESPEC
DESCRIPTOR.message_types_by_name['Typespec'] = _TYPESPEC
DESCRIPTOR.message_types_by_name['Primitive'] = _PRIMITIVE
DESCRIPTOR.message_types_by_name['MapFieldEntry'] = _MAPFIELDENTRY
DESCRIPTOR.message_types_by_name['Map'] = _MAP
DESCRIPTOR.message_types_by_name['CompositeType'] = _COMPOSITETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Typespec = _reflection.GeneratedProtocolMessageType('Typespec', (_message.Message,), {
  'DESCRIPTOR' : _TYPESPEC,
  '__module__' : 'descarteslabs.common.proto.typespec.typespec_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Typespec)
  })
_sym_db.RegisterMessage(Typespec)

Primitive = _reflection.GeneratedProtocolMessageType('Primitive', (_message.Message,), {
  'DESCRIPTOR' : _PRIMITIVE,
  '__module__' : 'descarteslabs.common.proto.typespec.typespec_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Primitive)
  })
_sym_db.RegisterMessage(Primitive)

MapFieldEntry = _reflection.GeneratedProtocolMessageType('MapFieldEntry', (_message.Message,), {
  'DESCRIPTOR' : _MAPFIELDENTRY,
  '__module__' : 'descarteslabs.common.proto.typespec.typespec_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.MapFieldEntry)
  })
_sym_db.RegisterMessage(MapFieldEntry)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {
  'DESCRIPTOR' : _MAP,
  '__module__' : 'descarteslabs.common.proto.typespec.typespec_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Map)
  })
_sym_db.RegisterMessage(Map)

CompositeType = _reflection.GeneratedProtocolMessageType('CompositeType', (_message.Message,), {
  'DESCRIPTOR' : _COMPOSITETYPE,
  '__module__' : 'descarteslabs.common.proto.typespec.typespec_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.CompositeType)
  })
_sym_db.RegisterMessage(CompositeType)


# @@protoc_insertion_point(module_scope)
