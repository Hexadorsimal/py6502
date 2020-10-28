from .rom import Rom


class ChrRom(Rom):
    page_size = 8 * 1024

    def __init__(self, name, data):
        super().__init__(name, self.page_size, data)
