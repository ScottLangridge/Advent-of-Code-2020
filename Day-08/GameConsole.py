class GameConsole:
    def __init__(self, program):
        self.instructions = {
            'nop': self.nop,
            'acc': self.acc,
            'jmp': self.jmp
        }

        self.pc = 0
        self.acc = 0

        self.prog = program

    def exec(self):
        visited = []

        while self.pc < len(self.prog):
            if self.pc in visited:
                return False, self.acc
            visited.append(self.pc)

            operator, operand = self.prog[self.pc]
            self.instructions[operator](operand)
            self.pc += 1

        return True, self.acc

    def nop(self, operand):
        pass

    def acc(self, operand):
        self.acc += operand

    def jmp(self, operand):
        self.pc += operand - 1
