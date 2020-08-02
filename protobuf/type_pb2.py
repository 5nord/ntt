# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: type.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='type.proto',
  package='ntt',
  syntax='proto3',
  serialized_options=b'Z\035github.com/nokia/ntt/protobuf',
  serialized_pb=b'\n\ntype.proto\x12\x03ntt\"\xda\x05\n\x04Type\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x65ncode\x18\x03 \x01(\t\x12\x0f\n\x07variant\x18\x04 \x01(\t\x12\x11\n\textension\x18\x05 \x01(\t\x12\x1e\n\x05\x61rray\x18\t \x01(\x0b\x32\r.ntt.ListTypeH\x00\x12\"\n\trecord_of\x18\n \x01(\x0b\x32\r.ntt.ListTypeH\x00\x12\x1f\n\x06set_of\x18\x0b \x01(\x0b\x32\r.ntt.ListTypeH\x00\x12$\n\tbitstring\x18\x0c \x01(\x0b\x32\x0f.ntt.StringTypeH\x00\x12%\n\ncharstring\x18\r \x01(\x0b\x32\x0f.ntt.StringTypeH\x00\x12%\n\nhextstring\x18\x0e \x01(\x0b\x32\x0f.ntt.StringTypeH\x00\x12&\n\x0boctetstring\x18\x0f \x01(\x0b\x32\x0f.ntt.StringTypeH\x00\x12/\n\x14universal_charstring\x18\x10 \x01(\x0b\x32\x0f.ntt.StringTypeH\x00\x12\"\n\x07\x61nytype\x18\x11 \x01(\x0b\x32\x0f.ntt.StructTypeH\x00\x12!\n\x06record\x18\x12 \x01(\x0b\x32\x0f.ntt.StructTypeH\x00\x12\x1e\n\x03set\x18\x13 \x01(\x0b\x32\x0f.ntt.StructTypeH\x00\x12 \n\x05union\x18\x14 \x01(\x0b\x32\x0f.ntt.StructTypeH\x00\x12!\n\x06scalar\x18\x15 \x01(\x0e\x32\x0f.ntt.ScalarTypeH\x00\x12\'\n\tcomponent\x18\x16 \x01(\x0b\x32\x12.ntt.ComponentTypeH\x00\x12#\n\nenumerated\x18\x17 \x01(\x0b\x32\r.ntt.EnumTypeH\x00\x12\x1d\n\x04port\x18\x18 \x01(\x0b\x32\r.ntt.PortTypeH\x00\x12\x1f\n\x05timer\x18\x19 \x01(\x0b\x32\x0e.ntt.TimerTypeH\x00\x12\x1c\n\x07\x61\x64\x64ress\x18\x1a \x01(\x0b\x32\t.ntt.TypeH\x00\x42\x06\n\x04kind\".\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x04type\x18\x02 \x01(\x0b\x32\t.ntt.Type\"(\n\nStructType\x12\x1a\n\x06\x66ields\x18\x01 \x03(\x0b\x32\n.ntt.Field\"K\n\x08ListType\x12\x1a\n\x07\x65lement\x18\x01 \x01(\x0b\x32\t.ntt.Type\x12#\n\nconstraint\x18\x03 \x01(\x0b\x32\x0f.ntt.Constraint\"#\n\nStringType\x12\x15\n\relement_width\x18\x01 \x01(\x05\"2\n\nConstraint\x1a$\n\x06\x42ounds\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"\x0f\n\rComponentType\"\n\n\x08\x45numType\"\n\n\x08PortType\"\x0b\n\tTimerType*H\n\nScalarType\x12\x08\n\x04NULL\x10\x00\x12\x0b\n\x07\x42OOLEAN\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\x0b\n\x07VERDICT\x10\x04\x42\x1fZ\x1dgithub.com/nokia/ntt/protobufb\x06proto3'
)

_SCALARTYPE = _descriptor.EnumDescriptor(
  name='ScalarType',
  full_name='ntt.ScalarType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NULL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTEGER', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1062,
  serialized_end=1134,
)
_sym_db.RegisterEnumDescriptor(_SCALARTYPE)

ScalarType = enum_type_wrapper.EnumTypeWrapper(_SCALARTYPE)
NULL = 0
BOOLEAN = 1
FLOAT = 2
INTEGER = 3
VERDICT = 4



_TYPE = _descriptor.Descriptor(
  name='Type',
  full_name='ntt.Type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ntt.Type.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encode', full_name='ntt.Type.encode', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variant', full_name='ntt.Type.variant', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='ntt.Type.extension', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='array', full_name='ntt.Type.array', index=4,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record_of', full_name='ntt.Type.record_of', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_of', full_name='ntt.Type.set_of', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bitstring', full_name='ntt.Type.bitstring', index=7,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charstring', full_name='ntt.Type.charstring', index=8,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hextstring', full_name='ntt.Type.hextstring', index=9,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='octetstring', full_name='ntt.Type.octetstring', index=10,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='universal_charstring', full_name='ntt.Type.universal_charstring', index=11,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='anytype', full_name='ntt.Type.anytype', index=12,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='ntt.Type.record', index=13,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set', full_name='ntt.Type.set', index=14,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union', full_name='ntt.Type.union', index=15,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scalar', full_name='ntt.Type.scalar', index=16,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component', full_name='ntt.Type.component', index=17,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enumerated', full_name='ntt.Type.enumerated', index=18,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ntt.Type.port', index=19,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timer', full_name='ntt.Type.timer', index=20,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='ntt.Type.address', index=21,
      number=26, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='kind', full_name='ntt.Type.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=20,
  serialized_end=750,
)


_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='ntt.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ntt.Field.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ntt.Field.type', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=798,
)


_STRUCTTYPE = _descriptor.Descriptor(
  name='StructType',
  full_name='ntt.StructType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='ntt.StructType.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=800,
  serialized_end=840,
)


_LISTTYPE = _descriptor.Descriptor(
  name='ListType',
  full_name='ntt.ListType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='ntt.ListType.element', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constraint', full_name='ntt.ListType.constraint', index=1,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=842,
  serialized_end=917,
)


_STRINGTYPE = _descriptor.Descriptor(
  name='StringType',
  full_name='ntt.StringType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element_width', full_name='ntt.StringType.element_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=919,
  serialized_end=954,
)


_CONSTRAINT_BOUNDS = _descriptor.Descriptor(
  name='Bounds',
  full_name='ntt.Constraint.Bounds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ntt.Constraint.Bounds.start', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='ntt.Constraint.Bounds.end', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=970,
  serialized_end=1006,
)

_CONSTRAINT = _descriptor.Descriptor(
  name='Constraint',
  full_name='ntt.Constraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_CONSTRAINT_BOUNDS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=956,
  serialized_end=1006,
)


_COMPONENTTYPE = _descriptor.Descriptor(
  name='ComponentType',
  full_name='ntt.ComponentType',
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
  serialized_start=1008,
  serialized_end=1023,
)


_ENUMTYPE = _descriptor.Descriptor(
  name='EnumType',
  full_name='ntt.EnumType',
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
  serialized_start=1025,
  serialized_end=1035,
)


_PORTTYPE = _descriptor.Descriptor(
  name='PortType',
  full_name='ntt.PortType',
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
  serialized_start=1037,
  serialized_end=1047,
)


_TIMERTYPE = _descriptor.Descriptor(
  name='TimerType',
  full_name='ntt.TimerType',
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
  serialized_start=1049,
  serialized_end=1060,
)

_TYPE.fields_by_name['array'].message_type = _LISTTYPE
_TYPE.fields_by_name['record_of'].message_type = _LISTTYPE
_TYPE.fields_by_name['set_of'].message_type = _LISTTYPE
_TYPE.fields_by_name['bitstring'].message_type = _STRINGTYPE
_TYPE.fields_by_name['charstring'].message_type = _STRINGTYPE
_TYPE.fields_by_name['hextstring'].message_type = _STRINGTYPE
_TYPE.fields_by_name['octetstring'].message_type = _STRINGTYPE
_TYPE.fields_by_name['universal_charstring'].message_type = _STRINGTYPE
_TYPE.fields_by_name['anytype'].message_type = _STRUCTTYPE
_TYPE.fields_by_name['record'].message_type = _STRUCTTYPE
_TYPE.fields_by_name['set'].message_type = _STRUCTTYPE
_TYPE.fields_by_name['union'].message_type = _STRUCTTYPE
_TYPE.fields_by_name['scalar'].enum_type = _SCALARTYPE
_TYPE.fields_by_name['component'].message_type = _COMPONENTTYPE
_TYPE.fields_by_name['enumerated'].message_type = _ENUMTYPE
_TYPE.fields_by_name['port'].message_type = _PORTTYPE
_TYPE.fields_by_name['timer'].message_type = _TIMERTYPE
_TYPE.fields_by_name['address'].message_type = _TYPE
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['array'])
_TYPE.fields_by_name['array'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['record_of'])
_TYPE.fields_by_name['record_of'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['set_of'])
_TYPE.fields_by_name['set_of'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['bitstring'])
_TYPE.fields_by_name['bitstring'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['charstring'])
_TYPE.fields_by_name['charstring'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['hextstring'])
_TYPE.fields_by_name['hextstring'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['octetstring'])
_TYPE.fields_by_name['octetstring'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['universal_charstring'])
_TYPE.fields_by_name['universal_charstring'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['anytype'])
_TYPE.fields_by_name['anytype'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['record'])
_TYPE.fields_by_name['record'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['set'])
_TYPE.fields_by_name['set'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['union'])
_TYPE.fields_by_name['union'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['scalar'])
_TYPE.fields_by_name['scalar'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['component'])
_TYPE.fields_by_name['component'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['enumerated'])
_TYPE.fields_by_name['enumerated'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['port'])
_TYPE.fields_by_name['port'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['timer'])
_TYPE.fields_by_name['timer'].containing_oneof = _TYPE.oneofs_by_name['kind']
_TYPE.oneofs_by_name['kind'].fields.append(
  _TYPE.fields_by_name['address'])
_TYPE.fields_by_name['address'].containing_oneof = _TYPE.oneofs_by_name['kind']
_FIELD.fields_by_name['type'].message_type = _TYPE
_STRUCTTYPE.fields_by_name['fields'].message_type = _FIELD
_LISTTYPE.fields_by_name['element'].message_type = _TYPE
_LISTTYPE.fields_by_name['constraint'].message_type = _CONSTRAINT
_CONSTRAINT_BOUNDS.containing_type = _CONSTRAINT
DESCRIPTOR.message_types_by_name['Type'] = _TYPE
DESCRIPTOR.message_types_by_name['Field'] = _FIELD
DESCRIPTOR.message_types_by_name['StructType'] = _STRUCTTYPE
DESCRIPTOR.message_types_by_name['ListType'] = _LISTTYPE
DESCRIPTOR.message_types_by_name['StringType'] = _STRINGTYPE
DESCRIPTOR.message_types_by_name['Constraint'] = _CONSTRAINT
DESCRIPTOR.message_types_by_name['ComponentType'] = _COMPONENTTYPE
DESCRIPTOR.message_types_by_name['EnumType'] = _ENUMTYPE
DESCRIPTOR.message_types_by_name['PortType'] = _PORTTYPE
DESCRIPTOR.message_types_by_name['TimerType'] = _TIMERTYPE
DESCRIPTOR.enum_types_by_name['ScalarType'] = _SCALARTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Type = _reflection.GeneratedProtocolMessageType('Type', (_message.Message,), {
  'DESCRIPTOR' : _TYPE,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.Type)
  })
_sym_db.RegisterMessage(Type)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
  'DESCRIPTOR' : _FIELD,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.Field)
  })
_sym_db.RegisterMessage(Field)

StructType = _reflection.GeneratedProtocolMessageType('StructType', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTTYPE,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.StructType)
  })
_sym_db.RegisterMessage(StructType)

ListType = _reflection.GeneratedProtocolMessageType('ListType', (_message.Message,), {
  'DESCRIPTOR' : _LISTTYPE,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.ListType)
  })
_sym_db.RegisterMessage(ListType)

StringType = _reflection.GeneratedProtocolMessageType('StringType', (_message.Message,), {
  'DESCRIPTOR' : _STRINGTYPE,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.StringType)
  })
_sym_db.RegisterMessage(StringType)

Constraint = _reflection.GeneratedProtocolMessageType('Constraint', (_message.Message,), {

  'Bounds' : _reflection.GeneratedProtocolMessageType('Bounds', (_message.Message,), {
    'DESCRIPTOR' : _CONSTRAINT_BOUNDS,
    '__module__' : 'type_pb2'
    # @@protoc_insertion_point(class_scope:ntt.Constraint.Bounds)
    })
  ,
  'DESCRIPTOR' : _CONSTRAINT,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.Constraint)
  })
_sym_db.RegisterMessage(Constraint)
_sym_db.RegisterMessage(Constraint.Bounds)

ComponentType = _reflection.GeneratedProtocolMessageType('ComponentType', (_message.Message,), {
  'DESCRIPTOR' : _COMPONENTTYPE,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.ComponentType)
  })
_sym_db.RegisterMessage(ComponentType)

EnumType = _reflection.GeneratedProtocolMessageType('EnumType', (_message.Message,), {
  'DESCRIPTOR' : _ENUMTYPE,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.EnumType)
  })
_sym_db.RegisterMessage(EnumType)

PortType = _reflection.GeneratedProtocolMessageType('PortType', (_message.Message,), {
  'DESCRIPTOR' : _PORTTYPE,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.PortType)
  })
_sym_db.RegisterMessage(PortType)

TimerType = _reflection.GeneratedProtocolMessageType('TimerType', (_message.Message,), {
  'DESCRIPTOR' : _TIMERTYPE,
  '__module__' : 'type_pb2'
  # @@protoc_insertion_point(class_scope:ntt.TimerType)
  })
_sym_db.RegisterMessage(TimerType)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
