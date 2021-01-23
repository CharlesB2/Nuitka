#     Copyright 2021, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
""" CType classes for C bool, this cannot represent unassigned, nor indicate exception.

"""

from .CTypeBases import CTypeBase, CTypeNotReferenceCountedMixin


class CTypeBool(CTypeNotReferenceCountedMixin, CTypeBase):
    c_type = "bool"

    # Return value only obviously.
    helper_code = "CBOOL"

    @classmethod
    def emitValueAccessCode(cls, value_name, emit, context):
        # Nothing to do for this type, pylint: disable=unused-argument
        assert False

    @classmethod
    def emitValueAssertionCode(cls, value_name, emit):
        pass

    @classmethod
    def emitAssignConversionCode(cls, to_name, value_name, needs_check, emit, context):
        # Conversion cannot fail, pylint: disable=unused-argument

        if value_name.c_type == cls.c_type:
            emit("%s = %s;" % (to_name, value_name))
        else:
            emit(
                "%s = %s;"
                % (
                    to_name,
                    value_name.getCType().getTruthCheckCode(value_name=value_name),
                )
            )

    @classmethod
    def getInitValue(cls, init_from):
        return "<not_possible>"

    @classmethod
    def getInitTestConditionCode(cls, value_name, inverted):
        return "<not_possible>"

    @classmethod
    def getDeleteObjectCode(
        cls, to_name, value_name, needs_check, tolerant, emit, context
    ):
        assert False

    @classmethod
    def emitAssignmentCodeFromBoolCondition(cls, to_name, condition, emit):
        emit("%s = (%s) ? true : false;" % (to_name, condition))

    @classmethod
    def getExceptionCheckCondition(cls, value_name):
        # Expected to not be used, pylint: disable=unused-argument
        assert False

    @classmethod
    def getTruthCheckCode(cls, value_name):
        return "%s != false" % value_name
