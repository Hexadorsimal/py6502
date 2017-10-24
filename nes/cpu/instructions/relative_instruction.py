from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ReadMicroinstruction, IncrementMicroinstruction
from nes.memory import AbsoluteAddress
from .instruction import Instruction


class RelativeInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'DL'), IncrementMicroinstruction('PCL')]))

    @property
    def size(self):
        return 2