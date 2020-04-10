# Client
class Client:
    computer = None

    def __init__(self, computer):
        self.computer = computer

    def __str__(self):
        return '{}\n{}\n{}\n' \
            .format(
                    self.computer.cpu(), 
                    self.computer.disk(),
                    self.computer.memory()    
                )
        