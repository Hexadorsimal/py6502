from ..instruction import Instruction


class Clc(Instruction):
    def execute(self, processor):
        processor.p.c.clear()