# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: descarteslabs/common/proto/job/job.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from descarteslabs.common.proto.destinations import destinations_pb2 as descarteslabs_dot_common_dot_proto_dot_destinations_dot_destinations__pb2
from descarteslabs.common.proto.formats import formats_pb2 as descarteslabs_dot_common_dot_proto_dot_formats_dot_formats__pb2
from descarteslabs.common.proto.types import types_pb2 as descarteslabs_dot_common_dot_proto_dot_types_dot_types__pb2
from descarteslabs.common.proto.typespec import typespec_pb2 as descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2
from descarteslabs.common.proto.errors import errors_pb2 as descarteslabs_dot_common_dot_proto_dot_errors_dot_errors__pb2

from descarteslabs.common.proto.errors.errors_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='descarteslabs/common/proto/job/job.proto',
  package='descarteslabs.workflows',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n(descarteslabs/common/proto/job/job.proto\x12\x17\x64\x65scarteslabs.workflows\x1a\x1egoogle/protobuf/wrappers.proto\x1a:descarteslabs/common/proto/destinations/destinations.proto\x1a\x30\x64\x65scarteslabs/common/proto/formats/formats.proto\x1a,descarteslabs/common/proto/types/types.proto\x1a\x32\x64\x65scarteslabs/common/proto/typespec/typespec.proto\x1a.descarteslabs/common/proto/errors/errors.proto\"\xe5\t\n\x03Job\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12)\n\x10serialized_graft\x18\x02 \x01(\tR\x0fserializedGraft\x12=\n\x08typespec\x18\x03 \x01(\x0b\x32!.descarteslabs.workflows.TypespecR\x08typespec\x12\x1e\n\nparameters\x18\x04 \x01(\tR\nparameters\x12\x19\n\x08no_cache\x18\x05 \x01(\x08R\x07noCache\x12\x18\n\x07\x63hannel\x18\x06 \x01(\tR\x07\x63hannel\x12%\n\x0e\x63lient_version\x18\x0e \x01(\tR\rclientVersion\x12\x1c\n\ttimestamp\x18\x07 \x01(\x03R\ttimestamp\x12\x12\n\x04user\x18\x08 \x01(\tR\x04user\x12\x10\n\x03org\x18\t \x01(\tR\x03org\x12\x38\n\x05state\x18\n \x01(\x0b\x32\".descarteslabs.workflows.Job.StateR\x05state\x12\x37\n\x04type\x18\x0b \x01(\x0e\x32#.descarteslabs.workflows.ResultTypeR\x04type\x12\x37\n\x06\x66ormat\x18\x0c \x01(\x0b\x32\x1f.descarteslabs.workflows.FormatR\x06\x66ormat\x12\x46\n\x0b\x64\x65stination\x18\r \x01(\x0b\x32$.descarteslabs.workflows.DestinationR\x0b\x64\x65stination\x1a\xed\x01\n\rTasksProgress\x12\x36\n\x07waiting\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x07waiting\x12\x32\n\x05ready\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x05ready\x12\x36\n\x07running\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x07running\x12\x38\n\x08\x66inished\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x08\x66inished\x1aY\n\x05\x45rror\x12\x36\n\x04\x63ode\x18\x01 \x01(\x0e\x32\".descarteslabs.workflows.ErrorCodeR\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x1a\xec\x01\n\x05State\x12\x38\n\x05stage\x18\x01 \x01(\x0e\x32\".descarteslabs.workflows.Job.StageR\x05stage\x12Q\n\x0etasks_progress\x18\x02 \x01(\x0b\x32*.descarteslabs.workflows.Job.TasksProgressR\rtasksProgress\x12\x38\n\x05\x65rror\x18\x03 \x01(\x0b\x32\".descarteslabs.workflows.Job.ErrorR\x05\x65rror\x12\x1c\n\ttimestamp\x18\x04 \x01(\x03R\ttimestamp\"v\n\x05Stage\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\r\n\tPREPARING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\n\n\x06SAVING\x10\x04\x12\n\n\x06\x46\x41ILED\x10\x05\x12\r\n\tSUCCEEDED\x10\x06\x12\r\n\tCANCELLED\x10\x07\"\xb2\x03\n\x10\x43reateJobRequest\x12)\n\x10serialized_graft\x18\x01 \x01(\tR\x0fserializedGraft\x12=\n\x08typespec\x18\x02 \x01(\x0b\x32!.descarteslabs.workflows.TypespecR\x08typespec\x12\x1e\n\nparameters\x18\x03 \x01(\tR\nparameters\x12\x19\n\x08no_cache\x18\x04 \x01(\x08R\x07noCache\x12\x18\n\x07\x63hannel\x18\x05 \x01(\tR\x07\x63hannel\x12%\n\x0e\x63lient_version\x18\t \x01(\tR\rclientVersion\x12\x37\n\x04type\x18\x06 \x01(\x0e\x32#.descarteslabs.workflows.ResultTypeR\x04type\x12\x37\n\x06\x66ormat\x18\x07 \x01(\x0b\x32\x1f.descarteslabs.workflows.FormatR\x06\x66ormat\x12\x46\n\x0b\x64\x65stination\x18\x08 \x01(\x0b\x32$.descarteslabs.workflows.DestinationR\x0b\x64\x65stination\"\x1f\n\rGetJobRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\"\n\x10\x43\x61ncelJobRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x13\n\x11\x43\x61ncelJobResponse\"!\n\x0fWatchJobRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"[\n\x0fListJobsRequest\x12%\n\x0estart_datetime\x18\x01 \x01(\tR\rstartDatetime\x12!\n\x0c\x65nd_datetime\x18\x02 \x01(\tR\x0b\x65ndDatetime2\xce\x03\n\x06JobAPI\x12V\n\tCreateJob\x12).descarteslabs.workflows.CreateJobRequest\x1a\x1c.descarteslabs.workflows.Job\"\x00\x12V\n\x08ListJobs\x12(.descarteslabs.workflows.ListJobsRequest\x1a\x1c.descarteslabs.workflows.Job\"\x00\x30\x01\x12P\n\x06GetJob\x12&.descarteslabs.workflows.GetJobRequest\x1a\x1c.descarteslabs.workflows.Job\"\x00\x12\x64\n\tCancelJob\x12).descarteslabs.workflows.CancelJobRequest\x1a*.descarteslabs.workflows.CancelJobResponse\"\x00\x12\\\n\x08WatchJob\x12(.descarteslabs.workflows.WatchJobRequest\x1a\".descarteslabs.workflows.Job.State\"\x00\x30\x01P\x05\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,descarteslabs_dot_common_dot_proto_dot_destinations_dot_destinations__pb2.DESCRIPTOR,descarteslabs_dot_common_dot_proto_dot_formats_dot_formats__pb2.DESCRIPTOR,descarteslabs_dot_common_dot_proto_dot_types_dot_types__pb2.DESCRIPTOR,descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2.DESCRIPTOR,descarteslabs_dot_common_dot_proto_dot_errors_dot_errors__pb2.DESCRIPTOR,],
  public_dependencies=[descarteslabs_dot_common_dot_proto_dot_errors_dot_errors__pb2.DESCRIPTOR,])



_JOB_STAGE = _descriptor.EnumDescriptor(
  name='Stage',
  full_name='descarteslabs.workflows.Job.Stage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEUED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREPARING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAVING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1493,
  serialized_end=1611,
)
_sym_db.RegisterEnumDescriptor(_JOB_STAGE)


_JOB_TASKSPROGRESS = _descriptor.Descriptor(
  name='TasksProgress',
  full_name='descarteslabs.workflows.Job.TasksProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='waiting', full_name='descarteslabs.workflows.Job.TasksProgress.waiting', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='waiting', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ready', full_name='descarteslabs.workflows.Job.TasksProgress.ready', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ready', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='running', full_name='descarteslabs.workflows.Job.TasksProgress.running', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='running', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished', full_name='descarteslabs.workflows.Job.TasksProgress.finished', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='finished', file=DESCRIPTOR),
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
  serialized_start=924,
  serialized_end=1161,
)

_JOB_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='descarteslabs.workflows.Job.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='descarteslabs.workflows.Job.Error.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='code', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='descarteslabs.workflows.Job.Error.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='message', file=DESCRIPTOR),
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
  serialized_start=1163,
  serialized_end=1252,
)

_JOB_STATE = _descriptor.Descriptor(
  name='State',
  full_name='descarteslabs.workflows.Job.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage', full_name='descarteslabs.workflows.Job.State.stage', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stage', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tasks_progress', full_name='descarteslabs.workflows.Job.State.tasks_progress', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tasksProgress', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='descarteslabs.workflows.Job.State.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='error', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='descarteslabs.workflows.Job.State.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR),
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
  serialized_start=1255,
  serialized_end=1491,
)

_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='descarteslabs.workflows.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.Job.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_graft', full_name='descarteslabs.workflows.Job.serialized_graft', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serializedGraft', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typespec', full_name='descarteslabs.workflows.Job.typespec', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='typespec', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='descarteslabs.workflows.Job.parameters', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parameters', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_cache', full_name='descarteslabs.workflows.Job.no_cache', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='noCache', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='descarteslabs.workflows.Job.channel', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_version', full_name='descarteslabs.workflows.Job.client_version', index=6,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='clientVersion', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='descarteslabs.workflows.Job.timestamp', index=7,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='descarteslabs.workflows.Job.user', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='user', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='descarteslabs.workflows.Job.org', index=9,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='org', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='descarteslabs.workflows.Job.state', index=10,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='state', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='descarteslabs.workflows.Job.type', index=11,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='format', full_name='descarteslabs.workflows.Job.format', index=12,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='format', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='descarteslabs.workflows.Job.destination', index=13,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='destination', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_JOB_TASKSPROGRESS, _JOB_ERROR, _JOB_STATE, ],
  enum_types=[
    _JOB_STAGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=1611,
)


_CREATEJOBREQUEST = _descriptor.Descriptor(
  name='CreateJobRequest',
  full_name='descarteslabs.workflows.CreateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_graft', full_name='descarteslabs.workflows.CreateJobRequest.serialized_graft', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serializedGraft', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typespec', full_name='descarteslabs.workflows.CreateJobRequest.typespec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='typespec', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='descarteslabs.workflows.CreateJobRequest.parameters', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parameters', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_cache', full_name='descarteslabs.workflows.CreateJobRequest.no_cache', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='noCache', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='descarteslabs.workflows.CreateJobRequest.channel', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_version', full_name='descarteslabs.workflows.CreateJobRequest.client_version', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='clientVersion', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='descarteslabs.workflows.CreateJobRequest.type', index=6,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='format', full_name='descarteslabs.workflows.CreateJobRequest.format', index=7,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='format', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='descarteslabs.workflows.CreateJobRequest.destination', index=8,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='destination', file=DESCRIPTOR),
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
  serialized_start=1614,
  serialized_end=2048,
)


_GETJOBREQUEST = _descriptor.Descriptor(
  name='GetJobRequest',
  full_name='descarteslabs.workflows.GetJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.GetJobRequest.id', index=0,
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
  serialized_start=2050,
  serialized_end=2081,
)


_CANCELJOBREQUEST = _descriptor.Descriptor(
  name='CancelJobRequest',
  full_name='descarteslabs.workflows.CancelJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.CancelJobRequest.id', index=0,
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
  serialized_start=2083,
  serialized_end=2117,
)


_CANCELJOBRESPONSE = _descriptor.Descriptor(
  name='CancelJobResponse',
  full_name='descarteslabs.workflows.CancelJobResponse',
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
  serialized_start=2119,
  serialized_end=2138,
)


_WATCHJOBREQUEST = _descriptor.Descriptor(
  name='WatchJobRequest',
  full_name='descarteslabs.workflows.WatchJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.WatchJobRequest.id', index=0,
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
  serialized_start=2140,
  serialized_end=2173,
)


_LISTJOBSREQUEST = _descriptor.Descriptor(
  name='ListJobsRequest',
  full_name='descarteslabs.workflows.ListJobsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_datetime', full_name='descarteslabs.workflows.ListJobsRequest.start_datetime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='startDatetime', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_datetime', full_name='descarteslabs.workflows.ListJobsRequest.end_datetime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='endDatetime', file=DESCRIPTOR),
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
  serialized_start=2175,
  serialized_end=2266,
)

_JOB_TASKSPROGRESS.fields_by_name['waiting'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_JOB_TASKSPROGRESS.fields_by_name['ready'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_JOB_TASKSPROGRESS.fields_by_name['running'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_JOB_TASKSPROGRESS.fields_by_name['finished'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_JOB_TASKSPROGRESS.containing_type = _JOB
_JOB_ERROR.fields_by_name['code'].enum_type = descarteslabs_dot_common_dot_proto_dot_errors_dot_errors__pb2._ERRORCODE
_JOB_ERROR.containing_type = _JOB
_JOB_STATE.fields_by_name['stage'].enum_type = _JOB_STAGE
_JOB_STATE.fields_by_name['tasks_progress'].message_type = _JOB_TASKSPROGRESS
_JOB_STATE.fields_by_name['error'].message_type = _JOB_ERROR
_JOB_STATE.containing_type = _JOB
_JOB.fields_by_name['typespec'].message_type = descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2._TYPESPEC
_JOB.fields_by_name['state'].message_type = _JOB_STATE
_JOB.fields_by_name['type'].enum_type = descarteslabs_dot_common_dot_proto_dot_types_dot_types__pb2._RESULTTYPE
_JOB.fields_by_name['format'].message_type = descarteslabs_dot_common_dot_proto_dot_formats_dot_formats__pb2._FORMAT
_JOB.fields_by_name['destination'].message_type = descarteslabs_dot_common_dot_proto_dot_destinations_dot_destinations__pb2._DESTINATION
_JOB_STAGE.containing_type = _JOB
_CREATEJOBREQUEST.fields_by_name['typespec'].message_type = descarteslabs_dot_common_dot_proto_dot_typespec_dot_typespec__pb2._TYPESPEC
_CREATEJOBREQUEST.fields_by_name['type'].enum_type = descarteslabs_dot_common_dot_proto_dot_types_dot_types__pb2._RESULTTYPE
_CREATEJOBREQUEST.fields_by_name['format'].message_type = descarteslabs_dot_common_dot_proto_dot_formats_dot_formats__pb2._FORMAT
_CREATEJOBREQUEST.fields_by_name['destination'].message_type = descarteslabs_dot_common_dot_proto_dot_destinations_dot_destinations__pb2._DESTINATION
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['CreateJobRequest'] = _CREATEJOBREQUEST
DESCRIPTOR.message_types_by_name['GetJobRequest'] = _GETJOBREQUEST
DESCRIPTOR.message_types_by_name['CancelJobRequest'] = _CANCELJOBREQUEST
DESCRIPTOR.message_types_by_name['CancelJobResponse'] = _CANCELJOBRESPONSE
DESCRIPTOR.message_types_by_name['WatchJobRequest'] = _WATCHJOBREQUEST
DESCRIPTOR.message_types_by_name['ListJobsRequest'] = _LISTJOBSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {

  'TasksProgress' : _reflection.GeneratedProtocolMessageType('TasksProgress', (_message.Message,), {
    'DESCRIPTOR' : _JOB_TASKSPROGRESS,
    '__module__' : 'descarteslabs.common.proto.job.job_pb2'
    # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Job.TasksProgress)
    })
  ,

  'Error' : _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
    'DESCRIPTOR' : _JOB_ERROR,
    '__module__' : 'descarteslabs.common.proto.job.job_pb2'
    # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Job.Error)
    })
  ,

  'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
    'DESCRIPTOR' : _JOB_STATE,
    '__module__' : 'descarteslabs.common.proto.job.job_pb2'
    # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Job.State)
    })
  ,
  'DESCRIPTOR' : _JOB,
  '__module__' : 'descarteslabs.common.proto.job.job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Job)
  })
_sym_db.RegisterMessage(Job)
_sym_db.RegisterMessage(Job.TasksProgress)
_sym_db.RegisterMessage(Job.Error)
_sym_db.RegisterMessage(Job.State)

CreateJobRequest = _reflection.GeneratedProtocolMessageType('CreateJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEJOBREQUEST,
  '__module__' : 'descarteslabs.common.proto.job.job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.CreateJobRequest)
  })
_sym_db.RegisterMessage(CreateJobRequest)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBREQUEST,
  '__module__' : 'descarteslabs.common.proto.job.job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.GetJobRequest)
  })
_sym_db.RegisterMessage(GetJobRequest)

CancelJobRequest = _reflection.GeneratedProtocolMessageType('CancelJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELJOBREQUEST,
  '__module__' : 'descarteslabs.common.proto.job.job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.CancelJobRequest)
  })
_sym_db.RegisterMessage(CancelJobRequest)

CancelJobResponse = _reflection.GeneratedProtocolMessageType('CancelJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELJOBRESPONSE,
  '__module__' : 'descarteslabs.common.proto.job.job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.CancelJobResponse)
  })
_sym_db.RegisterMessage(CancelJobResponse)

WatchJobRequest = _reflection.GeneratedProtocolMessageType('WatchJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _WATCHJOBREQUEST,
  '__module__' : 'descarteslabs.common.proto.job.job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.WatchJobRequest)
  })
_sym_db.RegisterMessage(WatchJobRequest)

ListJobsRequest = _reflection.GeneratedProtocolMessageType('ListJobsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTJOBSREQUEST,
  '__module__' : 'descarteslabs.common.proto.job.job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.ListJobsRequest)
  })
_sym_db.RegisterMessage(ListJobsRequest)



_JOBAPI = _descriptor.ServiceDescriptor(
  name='JobAPI',
  full_name='descarteslabs.workflows.JobAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2269,
  serialized_end=2731,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateJob',
    full_name='descarteslabs.workflows.JobAPI.CreateJob',
    index=0,
    containing_service=None,
    input_type=_CREATEJOBREQUEST,
    output_type=_JOB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListJobs',
    full_name='descarteslabs.workflows.JobAPI.ListJobs',
    index=1,
    containing_service=None,
    input_type=_LISTJOBSREQUEST,
    output_type=_JOB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='descarteslabs.workflows.JobAPI.GetJob',
    index=2,
    containing_service=None,
    input_type=_GETJOBREQUEST,
    output_type=_JOB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CancelJob',
    full_name='descarteslabs.workflows.JobAPI.CancelJob',
    index=3,
    containing_service=None,
    input_type=_CANCELJOBREQUEST,
    output_type=_CANCELJOBRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WatchJob',
    full_name='descarteslabs.workflows.JobAPI.WatchJob',
    index=4,
    containing_service=None,
    input_type=_WATCHJOBREQUEST,
    output_type=_JOB_STATE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBAPI)

DESCRIPTOR.services_by_name['JobAPI'] = _JOBAPI

# @@protoc_insertion_point(module_scope)
