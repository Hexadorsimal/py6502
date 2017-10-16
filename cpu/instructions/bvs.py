from ..cycle import Cycle
from ..operation import BranchOperation
from ..relative_instruction import RelativeInstruction


class Bvs(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchOperation('V', True)]))

    @property
    def name(self):
        return 'BVS'

    @property
    def opcode(self):
        return 0x70

    @property
    def description(self):
        return 'Branch on Overflow Set'
