from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Read, Write, Increment, Decrement, RW
from nes.memory import AbsoluteAddress, StackAddress
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Pha(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([RW(0), (StackAddress('S'), 'A'), Decrement('S')]))
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IR'), Increment('PCL')]))
        self.addressing_modes = {
            0x48: ImpliedAddressing
        }

    @property
    def name(self):
        return 'PHA'

    @property
    def description(self):
        return 'Push Accumulator on Stack'
