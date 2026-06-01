from dataclasses import dataclass

@dataclass
class Operands:
    left: int
    right: int

    def __hash__(self):
        return hash(self.left + self.right)

    def __eq__(self, other):
        if not isinstance(other, Operands):
            return False
        return self.left == other.left and self.right == other.right

    # create a domain factory (you can add validation in here instead of inside the class, domain model should stay pure)
def operands_factory(left: int, right: int):
        return Operands(left=left, right=right)