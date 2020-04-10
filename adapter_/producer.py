'''
the wrong uses interface.
    - Computer object need to use Hp7KB23EA hardwear and not HpAW0005NJ.
'''
class HpAW0005NJ:
    def cpu(self): pass
    def memory(self): pass
    def disk(self): pass


class Computer(HpAW0005NJ):
    def cpu(self):
        return "Intel® Core™ i7-1065G7 Quad Core Processor, 8M Cache, 1.3 GHz up to 3.9 GHz"

    def memory(self):
        return "16GB DDR4-2666 SDRAM (2 x 8GB)"

    def disk(self):
        return "1TB (7200RPM) Sata + 512GB M.2 SSD PCIe NVMe"