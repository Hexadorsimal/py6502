from ..instruction import Instruction


class Adc(Instruction):
    def execute(self, processor):
        addr = self.parameter
        mem = processor.read(addr)
        acc = processor.a.value

        value = mem + acc
        if processor.p.c:
            value += 1

        processor.p.z.update(value)
        processor.p.n.update(value)
        processor.p.v.update(not ((acc ^ mem) & 0x80) and (acc ^ value) & 0x80)
