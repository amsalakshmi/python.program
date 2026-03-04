import operator
import re

class MiniInterpreter:
    def __init__(self):
        self.variables = {}

    def eval_expr(self, expr):
        """
        Evaluate arithmetic expressions safely using variables.
        """
        for var in self.variables:
            expr = expr.replace(var, str(self.variables[var]))
        return eval(expr)

    def execute(self, lines):
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Skip empty lines
            if not line:
                i += 1
                continue

            # PRINT
            if line.startswith("print"):
                expr = line[6:]
                print(self.eval_expr(expr))

            # IF
            elif line.startswith("if"):
                condition = line[3:-1]
                if self.eval_expr(condition):
                    i += 1
                    while i < len(lines) and lines[i].startswith("    "):
                        self.execute([lines[i].strip()])
                        i += 1
                    continue

            # WHILE
            elif line.startswith("while"):
                condition = line[6:-1]
                loop_block = []
                j = i + 1
                while j < len(lines) and lines[j].startswith("    "):
                    loop_block.append(lines[j].strip())
                    j += 1

                while self.eval_expr(condition):
                    self.execute(loop_block)

                i = j
                continue

            # ASSIGNMENT
            elif "=" in line:
                var, expr = line.split("=")
                var = var.strip()
                expr = expr.strip()
                self.variables[var] = self.eval_expr(expr)

            i += 1


# Run Program
program = """
x = 5
y = 10
z = x + y * 2
print z

if z > 20:
    print z

i = 0
while i < 3:
    print i
    i = i + 1
"""

interpreter = MiniInterpreter()
interpreter.execute(program.split("\n"))