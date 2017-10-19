from ..cycle import Cycle
from ..operation import ClearFlagOperation
from ..implied_instruction import ImpliedInstruction


class ClearDecimalFlagOperation(ClearFlagOperation):
    def __init__(self):
        super().__init__('D')


class Cld(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ClearDecimalFlagOperation()]))

    @property
    def name(self):
        return 'CLD'

    @property
    def opcode(self):
        return 0xD8

    @property
    def description(self):
        return 'Clear Decimal Mode'