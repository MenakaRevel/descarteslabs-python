# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workflow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import types_pb2 as types__pb2
from . import parameters_pb2 as parameters__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='workflow.proto',
  package='descarteslabs.workflows',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0eworkflow.proto\x12\x17\x64\x65scarteslabs.workflows\x1a\x0btypes.proto\x1a\x10parameters.proto\"\xd1\x03\n\x08Workflow\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x02 \x01(\x03\x12\x19\n\x11updated_timestamp\x18\x03 \x01(\x03\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x31\n\x04type\x18\t \x01(\x0e\x32#.descarteslabs.workflows.ResultType\x12\x0f\n\x07\x63hannel\x18\n \x01(\t\x12\x1f\n\x17serialized_proxy_object\x18\x10 \x01(\t\x12N\n\x0fparameters_spec\x18\x11 \x03(\x0b\x32\x35.descarteslabs.workflows.Workflow.ParametersSpecEntry\x12\x18\n\x10serialized_graft\x18\x15 \x01(\t\x12\x1b\n\x13serialized_typespec\x18\x16 \x01(\t\x12\x0c\n\x04user\x18\x17 \x01(\t\x12\x0b\n\x03org\x18\x18 \x01(\t\x1aY\n\x13ParametersSpecEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".descarteslabs.workflows.Parameter:\x02\x38\x01\"L\n\x15\x43reateWorkflowRequest\x12\x33\n\x08workflow\x18\x01 \x01(\x0b\x32!.descarteslabs.workflows.Workflow\" \n\x12GetWorkflowRequest\x12\n\n\x02id\x18\x01 \x01(\t\"L\n\x15UpdateWorkflowRequest\x12\x33\n\x08workflow\x18\x01 \x01(\x0b\x32!.descarteslabs.workflows.Workflow\"D\n\x14ListWorkflowsRequest\x12\x16\n\x0estart_datetime\x18\x01 \x01(\t\x12\x14\n\x0c\x65nd_datetime\x18\x02 \x01(\t2\xa3\x03\n\x0bWorkflowAPI\x12\x65\n\x0e\x43reateWorkflow\x12..descarteslabs.workflows.CreateWorkflowRequest\x1a!.descarteslabs.workflows.Workflow\"\x00\x12\x65\n\rListWorkflows\x12-.descarteslabs.workflows.ListWorkflowsRequest\x1a!.descarteslabs.workflows.Workflow\"\x00\x30\x01\x12_\n\x0bGetWorkflow\x12+.descarteslabs.workflows.GetWorkflowRequest\x1a!.descarteslabs.workflows.Workflow\"\x00\x12\x65\n\x0eUpdateWorkflow\x12..descarteslabs.workflows.UpdateWorkflowRequest\x1a!.descarteslabs.workflows.Workflow\"\x00\x62\x06proto3')
  ,
  dependencies=[types__pb2.DESCRIPTOR,parameters__pb2.DESCRIPTOR,])




_WORKFLOW_PARAMETERSSPECENTRY = _descriptor.Descriptor(
  name='ParametersSpecEntry',
  full_name='descarteslabs.workflows.Workflow.ParametersSpecEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='descarteslabs.workflows.Workflow.ParametersSpecEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='descarteslabs.workflows.Workflow.ParametersSpecEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=540,
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
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_timestamp', full_name='descarteslabs.workflows.Workflow.created_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_timestamp', full_name='descarteslabs.workflows.Workflow.updated_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='descarteslabs.workflows.Workflow.name', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='descarteslabs.workflows.Workflow.description', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='descarteslabs.workflows.Workflow.type', index=5,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='descarteslabs.workflows.Workflow.channel', index=6,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_proxy_object', full_name='descarteslabs.workflows.Workflow.serialized_proxy_object', index=7,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters_spec', full_name='descarteslabs.workflows.Workflow.parameters_spec', index=8,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_graft', full_name='descarteslabs.workflows.Workflow.serialized_graft', index=9,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_typespec', full_name='descarteslabs.workflows.Workflow.serialized_typespec', index=10,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='descarteslabs.workflows.Workflow.user', index=11,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='descarteslabs.workflows.Workflow.org', index=12,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORKFLOW_PARAMETERSSPECENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=540,
)


_CREATEWORKFLOWREQUEST = _descriptor.Descriptor(
  name='CreateWorkflowRequest',
  full_name='descarteslabs.workflows.CreateWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workflow', full_name='descarteslabs.workflows.CreateWorkflowRequest.workflow', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=542,
  serialized_end=618,
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
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=620,
  serialized_end=652,
)


_UPDATEWORKFLOWREQUEST = _descriptor.Descriptor(
  name='UpdateWorkflowRequest',
  full_name='descarteslabs.workflows.UpdateWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workflow', full_name='descarteslabs.workflows.UpdateWorkflowRequest.workflow', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=654,
  serialized_end=730,
)


_LISTWORKFLOWSREQUEST = _descriptor.Descriptor(
  name='ListWorkflowsRequest',
  full_name='descarteslabs.workflows.ListWorkflowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_datetime', full_name='descarteslabs.workflows.ListWorkflowsRequest.start_datetime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_datetime', full_name='descarteslabs.workflows.ListWorkflowsRequest.end_datetime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=732,
  serialized_end=800,
)

_WORKFLOW_PARAMETERSSPECENTRY.fields_by_name['value'].message_type = parameters__pb2._PARAMETER
_WORKFLOW_PARAMETERSSPECENTRY.containing_type = _WORKFLOW
_WORKFLOW.fields_by_name['type'].enum_type = types__pb2._RESULTTYPE
_WORKFLOW.fields_by_name['parameters_spec'].message_type = _WORKFLOW_PARAMETERSSPECENTRY
_CREATEWORKFLOWREQUEST.fields_by_name['workflow'].message_type = _WORKFLOW
_UPDATEWORKFLOWREQUEST.fields_by_name['workflow'].message_type = _WORKFLOW
DESCRIPTOR.message_types_by_name['Workflow'] = _WORKFLOW
DESCRIPTOR.message_types_by_name['CreateWorkflowRequest'] = _CREATEWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['GetWorkflowRequest'] = _GETWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['UpdateWorkflowRequest'] = _UPDATEWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['ListWorkflowsRequest'] = _LISTWORKFLOWSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Workflow = _reflection.GeneratedProtocolMessageType('Workflow', (_message.Message,), dict(

  ParametersSpecEntry = _reflection.GeneratedProtocolMessageType('ParametersSpecEntry', (_message.Message,), dict(
    DESCRIPTOR = _WORKFLOW_PARAMETERSSPECENTRY,
    __module__ = 'workflow_pb2'
    # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Workflow.ParametersSpecEntry)
    ))
  ,
  DESCRIPTOR = _WORKFLOW,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Workflow)
  ))
_sym_db.RegisterMessage(Workflow)
_sym_db.RegisterMessage(Workflow.ParametersSpecEntry)

CreateWorkflowRequest = _reflection.GeneratedProtocolMessageType('CreateWorkflowRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEWORKFLOWREQUEST,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.CreateWorkflowRequest)
  ))
_sym_db.RegisterMessage(CreateWorkflowRequest)

GetWorkflowRequest = _reflection.GeneratedProtocolMessageType('GetWorkflowRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETWORKFLOWREQUEST,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.GetWorkflowRequest)
  ))
_sym_db.RegisterMessage(GetWorkflowRequest)

UpdateWorkflowRequest = _reflection.GeneratedProtocolMessageType('UpdateWorkflowRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEWORKFLOWREQUEST,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.UpdateWorkflowRequest)
  ))
_sym_db.RegisterMessage(UpdateWorkflowRequest)

ListWorkflowsRequest = _reflection.GeneratedProtocolMessageType('ListWorkflowsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTWORKFLOWSREQUEST,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.ListWorkflowsRequest)
  ))
_sym_db.RegisterMessage(ListWorkflowsRequest)


_WORKFLOW_PARAMETERSSPECENTRY._options = None

_WORKFLOWAPI = _descriptor.ServiceDescriptor(
  name='WorkflowAPI',
  full_name='descarteslabs.workflows.WorkflowAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=803,
  serialized_end=1222,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateWorkflow',
    full_name='descarteslabs.workflows.WorkflowAPI.CreateWorkflow',
    index=0,
    containing_service=None,
    input_type=_CREATEWORKFLOWREQUEST,
    output_type=_WORKFLOW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListWorkflows',
    full_name='descarteslabs.workflows.WorkflowAPI.ListWorkflows',
    index=1,
    containing_service=None,
    input_type=_LISTWORKFLOWSREQUEST,
    output_type=_WORKFLOW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWorkflow',
    full_name='descarteslabs.workflows.WorkflowAPI.GetWorkflow',
    index=2,
    containing_service=None,
    input_type=_GETWORKFLOWREQUEST,
    output_type=_WORKFLOW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateWorkflow',
    full_name='descarteslabs.workflows.WorkflowAPI.UpdateWorkflow',
    index=3,
    containing_service=None,
    input_type=_UPDATEWORKFLOWREQUEST,
    output_type=_WORKFLOW,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKFLOWAPI)

DESCRIPTOR.services_by_name['WorkflowAPI'] = _WORKFLOWAPI

# @@protoc_insertion_point(module_scope)
