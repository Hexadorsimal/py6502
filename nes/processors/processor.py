from nes.bus import Bus
from nes.registers import Register


class Processor:
    def __init__(self, bus: Bus):
        self.registers = {}
        self.bus = bus
        self.clock = 0

    def power_on(self):
        self.clock = 0

    def tick(self):
        self.clock += 1
