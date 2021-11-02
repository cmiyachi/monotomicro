# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person-location-event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person-location-event.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bperson-location-event.proto\"Q\n\x1aPersonLocationEventMessage\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x10\n\x08latitude\x18\x02 \x01(\x05\x12\x11\n\tlongitude\x18\x03 \x01(\x05\x32Q\n\x0bItemService\x12\x42\n\x06\x43reate\x12\x1b.PersonLocationEventMessage\x1a\x1b.PersonLocationEventMessageb\x06proto3'
)




_PERSONLOCATIONEVENTMESSAGE = _descriptor.Descriptor(
  name='PersonLocationEventMessage',
  full_name='PersonLocationEventMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='PersonLocationEventMessage.userId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='PersonLocationEventMessage.latitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='PersonLocationEventMessage.longitude', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=31,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['PersonLocationEventMessage'] = _PERSONLOCATIONEVENTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PersonLocationEventMessage = _reflection.GeneratedProtocolMessageType('PersonLocationEventMessage', (_message.Message,), {
  'DESCRIPTOR' : _PERSONLOCATIONEVENTMESSAGE,
  '__module__' : 'person_location_event_pb2'
  # @@protoc_insertion_point(class_scope:PersonLocationEventMessage)
  })
_sym_db.RegisterMessage(PersonLocationEventMessage)



_ITEMSERVICE = _descriptor.ServiceDescriptor(
  name='ItemService',
  full_name='ItemService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=114,
  serialized_end=195,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='ItemService.Create',
    index=0,
    containing_service=None,
    input_type=_PERSONLOCATIONEVENTMESSAGE,
    output_type=_PERSONLOCATIONEVENTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ITEMSERVICE)

DESCRIPTOR.services_by_name['ItemService'] = _ITEMSERVICE

# @@protoc_insertion_point(module_scope)
