from ..instruction import Instruction


class Cld(Instruction):
    def execute(self, processor):
        processor.p.d.clear()