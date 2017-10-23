from nes.cpu.cycle import Cycle
from nes.cpu.operations import MoveOperation
from .implied_instruction import ImpliedInstruction


class Tay(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('A', 'Y')]))

    @property
    def name(self):
        return 'TAY'

    @property
    def opcode(self):
        return 0xAB

    @property
    def description(self):
        return 'Transfer Accumulator to Index Y'
