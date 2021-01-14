# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: descarteslabs/common/proto/workflow/workflow.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from descarteslabs.common.proto.typespec import typespec_pb2 as descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2
from descarteslabs.common.proto.visualization import visualization_pb2 as descarteslabs_dot_common_dot_proto_dot_visualization_dot_visualization__pb2
from descarteslabs.common.proto.widgets import widgets_pb2 as descarteslabs_dot_common_dot_proto_dot_widgets_dot_widgets__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='descarteslabs/common/proto/workflow/workflow.proto',
  package='descarteslabs.workflows',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n2descarteslabs/common/proto/workflow/workflow.proto\x12\x17\x64\x65scarteslabs.workflows\x1a\x32\x64\x65scarteslabs/common/proto/typespec/typespec.proto\x1a<descarteslabs/common/proto/visualization/visualization.proto\x1a\x30\x64\x65scarteslabs/common/proto/widgets/widgets.proto\"\xaa\x04\n\x08Workflow\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12+\n\x11\x63reated_timestamp\x18\x02 \x01(\x03R\x10\x63reatedTimestamp\x12+\n\x11updated_timestamp\x18\x03 \x01(\x03R\x10updatedTimestamp\x12\x16\n\x06public\x18\x05 \x01(\x08R\x06public\x12\x14\n\x05title\x18\t \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12R\n\x10versioned_grafts\x18\x1a \x03(\x0b\x32\'.descarteslabs.workflows.VersionedGraftR\x0fversionedGrafts\x12\x45\n\x06labels\x18\x1b \x03(\x0b\x32-.descarteslabs.workflows.Workflow.LabelsEntryR\x06labels\x12\x12\n\x04tags\x18\x1d \x03(\tR\x04tags\x12\x12\n\x04user\x18\x17 \x01(\tR\x04user\x12\x10\n\x03org\x18\x18 \x01(\tR\x03org\x12\x14\n\x05\x65mail\x18\x19 \x01(\tR\x05\x65mail\x12\x12\n\x04name\x18\x1c \x01(\tR\x04name\x12*\n\x11wmts_url_template\x18\x1e \x01(\tR\x0fwmtsUrlTemplate\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x87\x03\n\x15UpsertWorkflowRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06public\x18\x02 \x01(\x08R\x06public\x12\x14\n\x05title\x18\x03 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12R\n\x10versioned_grafts\x18\x1a \x03(\x0b\x32\'.descarteslabs.workflows.VersionedGraftR\x0fversionedGrafts\x12R\n\x06labels\x18\x1b \x03(\x0b\x32:.descarteslabs.workflows.UpsertWorkflowRequest.LabelsEntryR\x06labels\x12\x12\n\x04tags\x18\x1d \x03(\tR\x04tags\x12\x17\n\x07\x64ry_run\x18\x32 \x01(\x08R\x06\x64ryRun\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"$\n\x12GetWorkflowRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"=\n\x11GetVersionRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\"\'\n\x15\x44\x65leteWorkflowRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"c\n\x16SearchWorkflowsRequest\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\x12\x1f\n\x0bname_prefix\x18\x02 \x01(\tR\nnamePrefix\x12\x12\n\x04tags\x18\x1d \x03(\tR\x04tags\"\xe0\x05\n\x0eVersionedGraft\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12\x1c\n\tdocstring\x18\x05 \x01(\tR\tdocstring\x12)\n\x10serialized_graft\x18\x02 \x01(\tR\x0fserializedGraft\x12=\n\x08typespec\x18\x04 \x01(\x0b\x32!.descarteslabs.workflows.TypespecR\x08typespec\x12\x42\n\nparameters\x18\x0b \x03(\x0b\x32\".descarteslabs.workflows.ParameterR\nparameters\x12\x18\n\x07\x63hannel\x18\x03 \x01(\tR\x07\x63hannel\x12%\n\x0e\x63lient_version\x18\n \x01(\tR\rclientVersion\x12K\n\x06labels\x18\x06 \x03(\x0b\x32\x33.descarteslabs.workflows.VersionedGraft.LabelsEntryR\x06labels\x12+\n\x11\x63reated_timestamp\x18\x07 \x01(\x03R\x10\x63reatedTimestamp\x12+\n\x11updated_timestamp\x18\x08 \x01(\x03R\x10updatedTimestamp\x12\x31\n\x14\x64\x65precated_timestamp\x18\t \x01(\x03R\x13\x64\x65precatedTimestamp\x12!\n\x0curl_template\x18\x0c \x01(\tR\x0burlTemplate\x12*\n\x11wmts_url_template\x18\r \x01(\tR\x0fwmtsUrlTemplate\x12\x43\n\x0bviz_options\x18\x0e \x03(\x0b\x32\".descarteslabs.workflows.VizOptionR\nvizOptions\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"E\n\x17WmtsUrlTemplateResponse\x12*\n\x11wmts_url_template\x18\x01 \x01(\tR\x0fwmtsUrlTemplate\"\x07\n\x05\x45mpty2\xf3\x04\n\x0bWorkflowAPI\x12\x65\n\x0eUpsertWorkflow\x12..descarteslabs.workflows.UpsertWorkflowRequest\x1a!.descarteslabs.workflows.Workflow\"\x00\x12_\n\x0bGetWorkflow\x12+.descarteslabs.workflows.GetWorkflowRequest\x1a!.descarteslabs.workflows.Workflow\"\x00\x12\x63\n\nGetVersion\x12*.descarteslabs.workflows.GetVersionRequest\x1a\'.descarteslabs.workflows.VersionedGraft\"\x00\x12i\n\x0fSearchWorkflows\x12/.descarteslabs.workflows.SearchWorkflowsRequest\x1a!.descarteslabs.workflows.Workflow\"\x00\x30\x01\x12\x62\n\x0e\x44\x65leteWorkflow\x12..descarteslabs.workflows.DeleteWorkflowRequest\x1a\x1e.descarteslabs.workflows.Empty\"\x00\x12h\n\x12GetWmtsUrlTemplate\x12\x1e.descarteslabs.workflows.Empty\x1a\x30.descarteslabs.workflows.WmtsUrlTemplateResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2.DESCRIPTOR,descarteslabs_dot_common_dot_proto_dot_visualization_dot_visualization__pb2.DESCRIPTOR,descarteslabs_dot_common_dot_proto_dot_widgets_dot_widgets__pb2.DESCRIPTOR,])




_WORKFLOW_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='descarteslabs.workflows.Workflow.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='descarteslabs.workflows.Workflow.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='descarteslabs.workflows.Workflow.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=798,
)

_WORKFLOW = _descriptor.Descriptor(
  name='Workflow',
  full_name='descarteslabs.workflows.Workflow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.Workflow.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_timestamp', full_name='descarteslabs.workflows.Workflow.created_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='createdTimestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_timestamp', full_name='descarteslabs.workflows.Workflow.updated_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updatedTimestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public', full_name='descarteslabs.workflows.Workflow.public', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='public', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='descarteslabs.workflows.Workflow.title', index=4,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='title', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='descarteslabs.workflows.Workflow.description', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versioned_grafts', full_name='descarteslabs.workflows.Workflow.versioned_grafts', index=6,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='versionedGrafts', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='descarteslabs.workflows.Workflow.labels', index=7,
      number=27, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='descarteslabs.workflows.Workflow.tags', index=8,
      number=29, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='descarteslabs.workflows.Workflow.user', index=9,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='user', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='descarteslabs.workflows.Workflow.org', index=10,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='org', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='descarteslabs.workflows.Workflow.email', index=11,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='email', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='descarteslabs.workflows.Workflow.name', index=12,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wmts_url_template', full_name='descarteslabs.workflows.Workflow.wmts_url_template', index=13,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='wmtsUrlTemplate', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORKFLOW_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=798,
)


_UPSERTWORKFLOWREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='descarteslabs.workflows.UpsertWorkflowRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='descarteslabs.workflows.UpsertWorkflowRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='descarteslabs.workflows.UpsertWorkflowRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=798,
)

_UPSERTWORKFLOWREQUEST = _descriptor.Descriptor(
  name='UpsertWorkflowRequest',
  full_name='descarteslabs.workflows.UpsertWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.UpsertWorkflowRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public', full_name='descarteslabs.workflows.UpsertWorkflowRequest.public', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='public', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='descarteslabs.workflows.UpsertWorkflowRequest.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='title', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='descarteslabs.workflows.UpsertWorkflowRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versioned_grafts', full_name='descarteslabs.workflows.UpsertWorkflowRequest.versioned_grafts', index=4,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='versionedGrafts', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='descarteslabs.workflows.UpsertWorkflowRequest.labels', index=5,
      number=27, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='descarteslabs.workflows.UpsertWorkflowRequest.tags', index=6,
      number=29, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dry_run', full_name='descarteslabs.workflows.UpsertWorkflowRequest.dry_run', index=7,
      number=50, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dryRun', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPSERTWORKFLOWREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=1192,
)


_GETWORKFLOWREQUEST = _descriptor.Descriptor(
  name='GetWorkflowRequest',
  full_name='descarteslabs.workflows.GetWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.GetWorkflowRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
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
  serialized_start=1194,
  serialized_end=1230,
)


_GETVERSIONREQUEST = _descriptor.Descriptor(
  name='GetVersionRequest',
  full_name='descarteslabs.workflows.GetVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.GetVersionRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='descarteslabs.workflows.GetVersionRequest.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='version', file=DESCRIPTOR),
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
  serialized_start=1232,
  serialized_end=1293,
)


_DELETEWORKFLOWREQUEST = _descriptor.Descriptor(
  name='DeleteWorkflowRequest',
  full_name='descarteslabs.workflows.DeleteWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.DeleteWorkflowRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
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
  serialized_start=1295,
  serialized_end=1334,
)


_SEARCHWORKFLOWSREQUEST = _descriptor.Descriptor(
  name='SearchWorkflowsRequest',
  full_name='descarteslabs.workflows.SearchWorkflowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='descarteslabs.workflows.SearchWorkflowsRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='email', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_prefix', full_name='descarteslabs.workflows.SearchWorkflowsRequest.name_prefix', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='namePrefix', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='descarteslabs.workflows.SearchWorkflowsRequest.tags', index=2,
      number=29, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR),
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
  serialized_start=1336,
  serialized_end=1435,
)


_VERSIONEDGRAFT_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='descarteslabs.workflows.VersionedGraft.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='descarteslabs.workflows.VersionedGraft.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='descarteslabs.workflows.VersionedGraft.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=798,
)

_VERSIONEDGRAFT = _descriptor.Descriptor(
  name='VersionedGraft',
  full_name='descarteslabs.workflows.VersionedGraft',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='descarteslabs.workflows.VersionedGraft.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='version', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docstring', full_name='descarteslabs.workflows.VersionedGraft.docstring', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='docstring', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_graft', full_name='descarteslabs.workflows.VersionedGraft.serialized_graft', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serializedGraft', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typespec', full_name='descarteslabs.workflows.VersionedGraft.typespec', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='typespec', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='descarteslabs.workflows.VersionedGraft.parameters', index=4,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parameters', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='descarteslabs.workflows.VersionedGraft.channel', index=5,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_version', full_name='descarteslabs.workflows.VersionedGraft.client_version', index=6,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='clientVersion', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='descarteslabs.workflows.VersionedGraft.labels', index=7,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_timestamp', full_name='descarteslabs.workflows.VersionedGraft.created_timestamp', index=8,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='createdTimestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_timestamp', full_name='descarteslabs.workflows.VersionedGraft.updated_timestamp', index=9,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updatedTimestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deprecated_timestamp', full_name='descarteslabs.workflows.VersionedGraft.deprecated_timestamp', index=10,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='deprecatedTimestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url_template', full_name='descarteslabs.workflows.VersionedGraft.url_template', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='urlTemplate', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wmts_url_template', full_name='descarteslabs.workflows.VersionedGraft.wmts_url_template', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='wmtsUrlTemplate', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='viz_options', full_name='descarteslabs.workflows.VersionedGraft.viz_options', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='vizOptions', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VERSIONEDGRAFT_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1438,
  serialized_end=2174,
)


_WMTSURLTEMPLATERESPONSE = _descriptor.Descriptor(
  name='WmtsUrlTemplateResponse',
  full_name='descarteslabs.workflows.WmtsUrlTemplateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wmts_url_template', full_name='descarteslabs.workflows.WmtsUrlTemplateResponse.wmts_url_template', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='wmtsUrlTemplate', file=DESCRIPTOR),
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
  serialized_start=2176,
  serialized_end=2245,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='descarteslabs.workflows.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=2247,
  serialized_end=2254,
)

_WORKFLOW_LABELSENTRY.containing_type = _WORKFLOW
_WORKFLOW.fields_by_name['versioned_grafts'].message_type = _VERSIONEDGRAFT
_WORKFLOW.fields_by_name['labels'].message_type = _WORKFLOW_LABELSENTRY
_UPSERTWORKFLOWREQUEST_LABELSENTRY.containing_type = _UPSERTWORKFLOWREQUEST
_UPSERTWORKFLOWREQUEST.fields_by_name['versioned_grafts'].message_type = _VERSIONEDGRAFT
_UPSERTWORKFLOWREQUEST.fields_by_name['labels'].message_type = _UPSERTWORKFLOWREQUEST_LABELSENTRY
_VERSIONEDGRAFT_LABELSENTRY.containing_type = _VERSIONEDGRAFT
_VERSIONEDGRAFT.fields_by_name['typespec'].message_type = descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2._TYPESPEC
_VERSIONEDGRAFT.fields_by_name['parameters'].message_type = descarteslabs_dot_common_dot_proto_dot_widgets_dot_widgets__pb2._PARAMETER
_VERSIONEDGRAFT.fields_by_name['labels'].message_type = _VERSIONEDGRAFT_LABELSENTRY
_VERSIONEDGRAFT.fields_by_name['viz_options'].message_type = descarteslabs_dot_common_dot_proto_dot_visualization_dot_visualization__pb2._VIZOPTION
DESCRIPTOR.message_types_by_name['Workflow'] = _WORKFLOW
DESCRIPTOR.message_types_by_name['UpsertWorkflowRequest'] = _UPSERTWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['GetWorkflowRequest'] = _GETWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['GetVersionRequest'] = _GETVERSIONREQUEST
DESCRIPTOR.message_types_by_name['DeleteWorkflowRequest'] = _DELETEWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['SearchWorkflowsRequest'] = _SEARCHWORKFLOWSREQUEST
DESCRIPTOR.message_types_by_name['VersionedGraft'] = _VERSIONEDGRAFT
DESCRIPTOR.message_types_by_name['WmtsUrlTemplateResponse'] = _WMTSURLTEMPLATERESPONSE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Workflow = _reflection.GeneratedProtocolMessageType('Workflow', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _WORKFLOW_LABELSENTRY,
    '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
    # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Workflow.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _WORKFLOW,
  '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Workflow)
  })
_sym_db.RegisterMessage(Workflow)
_sym_db.RegisterMessage(Workflow.LabelsEntry)

UpsertWorkflowRequest = _reflection.GeneratedProtocolMessageType('UpsertWorkflowRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPSERTWORKFLOWREQUEST_LABELSENTRY,
    '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
    # @@protoc_insertion_point(class_scope:descarteslabs.workflows.UpsertWorkflowRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _UPSERTWORKFLOWREQUEST,
  '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.UpsertWorkflowRequest)
  })
_sym_db.RegisterMessage(UpsertWorkflowRequest)
_sym_db.RegisterMessage(UpsertWorkflowRequest.LabelsEntry)

GetWorkflowRequest = _reflection.GeneratedProtocolMessageType('GetWorkflowRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETWORKFLOWREQUEST,
  '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.GetWorkflowRequest)
  })
_sym_db.RegisterMessage(GetWorkflowRequest)

GetVersionRequest = _reflection.GeneratedProtocolMessageType('GetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONREQUEST,
  '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.GetVersionRequest)
  })
_sym_db.RegisterMessage(GetVersionRequest)

DeleteWorkflowRequest = _reflection.GeneratedProtocolMessageType('DeleteWorkflowRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEWORKFLOWREQUEST,
  '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.DeleteWorkflowRequest)
  })
_sym_db.RegisterMessage(DeleteWorkflowRequest)

SearchWorkflowsRequest = _reflection.GeneratedProtocolMessageType('SearchWorkflowsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHWORKFLOWSREQUEST,
  '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.SearchWorkflowsRequest)
  })
_sym_db.RegisterMessage(SearchWorkflowsRequest)

VersionedGraft = _reflection.GeneratedProtocolMessageType('VersionedGraft', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _VERSIONEDGRAFT_LABELSENTRY,
    '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
    # @@protoc_insertion_point(class_scope:descarteslabs.workflows.VersionedGraft.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _VERSIONEDGRAFT,
  '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.VersionedGraft)
  })
_sym_db.RegisterMessage(VersionedGraft)
_sym_db.RegisterMessage(VersionedGraft.LabelsEntry)

WmtsUrlTemplateResponse = _reflection.GeneratedProtocolMessageType('WmtsUrlTemplateResponse', (_message.Message,), {
  'DESCRIPTOR' : _WMTSURLTEMPLATERESPONSE,
  '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.WmtsUrlTemplateResponse)
  })
_sym_db.RegisterMessage(WmtsUrlTemplateResponse)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'descarteslabs.common.proto.workflow.workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Empty)
  })
_sym_db.RegisterMessage(Empty)


_WORKFLOW_LABELSENTRY._options = None
_UPSERTWORKFLOWREQUEST_LABELSENTRY._options = None
_VERSIONEDGRAFT_LABELSENTRY._options = None

_WORKFLOWAPI = _descriptor.ServiceDescriptor(
  name='WorkflowAPI',
  full_name='descarteslabs.workflows.WorkflowAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2257,
  serialized_end=2884,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpsertWorkflow',
    full_name='descarteslabs.workflows.WorkflowAPI.UpsertWorkflow',
    index=0,
    containing_service=None,
    input_type=_UPSERTWORKFLOWREQUEST,
    output_type=_WORKFLOW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWorkflow',
    full_name='descarteslabs.workflows.WorkflowAPI.GetWorkflow',
    index=1,
    containing_service=None,
    input_type=_GETWORKFLOWREQUEST,
    output_type=_WORKFLOW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetVersion',
    full_name='descarteslabs.workflows.WorkflowAPI.GetVersion',
    index=2,
    containing_service=None,
    input_type=_GETVERSIONREQUEST,
    output_type=_VERSIONEDGRAFT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SearchWorkflows',
    full_name='descarteslabs.workflows.WorkflowAPI.SearchWorkflows',
    index=3,
    containing_service=None,
    input_type=_SEARCHWORKFLOWSREQUEST,
    output_type=_WORKFLOW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteWorkflow',
    full_name='descarteslabs.workflows.WorkflowAPI.DeleteWorkflow',
    index=4,
    containing_service=None,
    input_type=_DELETEWORKFLOWREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWmtsUrlTemplate',
    full_name='descarteslabs.workflows.WorkflowAPI.GetWmtsUrlTemplate',
    index=5,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_WMTSURLTEMPLATERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKFLOWAPI)

DESCRIPTOR.services_by_name['WorkflowAPI'] = _WORKFLOWAPI

# @@protoc_insertion_point(module_scope)
