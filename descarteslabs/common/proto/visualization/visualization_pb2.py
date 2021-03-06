# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: descarteslabs/common/proto/visualization/visualization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='descarteslabs/common/proto/visualization/visualization.proto',
  package='descarteslabs.workflows',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<descarteslabs/common/proto/visualization/visualization.proto\x12\x17\x64\x65scarteslabs.workflows\"\xa2\x02\n\tVizOption\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05\x62\x61nds\x18\x02 \x03(\tR\x05\x62\x61nds\x12\"\n\x0c\x63heckerboard\x18\x03 \x01(\x08R\x0c\x63heckerboard\x12\x1a\n\x08\x63olormap\x18\x04 \x01(\tR\x08\x63olormap\x12\x1c\n\treduction\x18\x05 \x01(\tR\treduction\x12\x41\n\x06scales\x18\x06 \x03(\x0b\x32).descarteslabs.workflows.VizOption.ScalesR\x06scales\x12 \n\x0b\x64\x65scription\x18\x07 \x01(\tR\x0b\x64\x65scription\x1a,\n\x06Scales\x12\x10\n\x03min\x18\x01 \x01(\x01R\x03min\x12\x10\n\x03max\x18\x02 \x01(\x01R\x03maxb\x06proto3'
)




_VIZOPTION_SCALES = _descriptor.Descriptor(
  name='Scales',
  full_name='descarteslabs.workflows.VizOption.Scales',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='descarteslabs.workflows.VizOption.Scales.min', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='min', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max', full_name='descarteslabs.workflows.VizOption.Scales.max', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='max', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=336,
  serialized_end=380,
)

_VIZOPTION = _descriptor.Descriptor(
  name='VizOption',
  full_name='descarteslabs.workflows.VizOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.VizOption.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bands', full_name='descarteslabs.workflows.VizOption.bands', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bands', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checkerboard', full_name='descarteslabs.workflows.VizOption.checkerboard', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='checkerboard', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='colormap', full_name='descarteslabs.workflows.VizOption.colormap', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='colormap', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reduction', full_name='descarteslabs.workflows.VizOption.reduction', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='reduction', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scales', full_name='descarteslabs.workflows.VizOption.scales', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scales', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='descarteslabs.workflows.VizOption.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VIZOPTION_SCALES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=380,
)

_VIZOPTION_SCALES.containing_type = _VIZOPTION
_VIZOPTION.fields_by_name['scales'].message_type = _VIZOPTION_SCALES
DESCRIPTOR.message_types_by_name['VizOption'] = _VIZOPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VizOption = _reflection.GeneratedProtocolMessageType('VizOption', (_message.Message,), {

  'Scales' : _reflection.GeneratedProtocolMessageType('Scales', (_message.Message,), {
    'DESCRIPTOR' : _VIZOPTION_SCALES,
    '__module__' : 'descarteslabs.common.proto.visualization.visualization_pb2'
    # @@protoc_insertion_point(class_scope:descarteslabs.workflows.VizOption.Scales)
    })
  ,
  'DESCRIPTOR' : _VIZOPTION,
  '__module__' : 'descarteslabs.common.proto.visualization.visualization_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.VizOption)
  })
_sym_db.RegisterMessage(VizOption)
_sym_db.RegisterMessage(VizOption.Scales)


# @@protoc_insertion_point(module_scope)
