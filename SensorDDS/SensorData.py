
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from SensorData.idl
# using RTI Code Generator (rtiddsgen) version 4.5.0.
# The rtiddsgen tool is part of the RTI Connext DDS distribution.
# For more information, type 'rtiddsgen -help' at a command shell
# or consult the Code Generator User's Manual.

from dataclasses import field
from typing import Union, Sequence, Optional
import rti.idl as idl
import rti.rpc as rpc
from enum import IntEnum
import sys
import os
from abc import ABC



@idl.struct(

    member_annotations = {
        'sensor_id': [idl.key, idl.bound(255),],
        'sensor_type': [idl.bound(255),],
    }
)
class SensorData:
    sensor_id: str = ""
    sensor_type: str = ""
    value: float = 0.0
    timestamp: idl.int32 = 0
