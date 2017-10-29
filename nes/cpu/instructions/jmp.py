from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move, Read, AddressBus, Increment, RW
from ..addressing_modes import *
from .instruction import Instruction


class Jmp(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('ADL', 'PCL'), Read('ADH'), Read('PCH'), AddressBus('PCX'), RW(1), Increment('PCL')]))

        self.addressing_modes = {
            0x4C: JmpAbsoluteAddressing,
            0x6C: IndirectAbsoluteAddressing,
        }

    @property
    def name(self):
        return 'JMP'

    @property
    def description(self):
        return 'Jump to New Location'
