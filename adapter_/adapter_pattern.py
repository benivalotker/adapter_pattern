'''
programer use adpter to fix the problem with differnt interface.
    - create new cpu for the client.
    - use same memory and disk.
'''

# Target interface
class Hp7KB23EA:
    def cpu(self): pass
    def memory(self): pass
    def disk(self): pass


# Adapter
class Adapter(Hp7KB23EA):
    computer = None

    def __init__(self, computer):
        self.computer = computer

    def cpu(self):
        return "Intel® Core™ i7-9750H Six Core Processor, 12M Cache, 2.60 GHz up to 4.50 GHz"

    def memory(self):
        return self.computer.memory()

    def disk(self):
        return self.computer.disk()


