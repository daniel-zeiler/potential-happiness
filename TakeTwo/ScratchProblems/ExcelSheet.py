import collections


class Cell:
    def __init__(self, value: int, x_position: str, y_position: str):
        self.value = value
        self.parent_operations = {}
        self.child_operations = {}
        self.x_position = x_position
        self.y_position = y_position

    def update_children(self, value):
        self.value = value
        for child_operation in self.child_operations:
            cell = child_operation.cell
            op = child_operation.op
            self.update_children(cell, value + op)

    def remove_parents(self):
        for parent_operation in self.parent_operations:
            del parent_operation.cell.child_operations[self.x_position + self.y_position]


class Operation:
    def __init__(self, cell: Cell, op: str):
        self.cell = cell
        self.op = op


class ExcelSheet:
    def __init__(self):
        self.nodes = collections.defaultdict(Cell)

    def delete(self, x_position: str, y_position: str):
        if x_position + y_position in self.nodes:
            cell = self.nodes[x_position + y_position]
            if not cell.child_operations:
                cell.remove_parents()
                del self.nodes[x_position + y_position]
            else:
                raise Exception(f"Cell {x_position + y_position} has child operations")

    def standard_write(self, x_position: str, y_position: str, value: int):
        if x_position + y_position not in self.nodes:
            self.nodes[x_position + y_position] = Cell(value, x_position, y_position)
        else:
            cell = self.nodes[x_position + y_position]
            cell.remove_parents()
            cell.parent_operations = {}
            cell.update_children(value)

    def advanced_write(self, x_position: str, y_position: str, operations: collections.Iterable[Operation]):
        if not self.check_cycle(x_position, y_position):
            raise Exception(f"Cell {x_position + y_position} operation will create a cycle")
        for operation in operations:
            if operation.cell.x_position == x_position and operation.cell.y_position == y_position:
                raise Exception(f"Cell {x_position + y_position} self reference in advanced write")

    def read_cell(self, x_position, y_position):
        if x_position + y_position in self.nodes:
            return self.nodes[x_position + y_position].value

    def check_cycle(self, x_position, y_position, starting_position):
        visited = set(starting_position)


ExcelSheet = ExcelSheet()
ExcelSheet.standard_write("1", "2", 5)
print(ExcelSheet.read_cell("1", "2"))
ExcelSheet.standard_write("1", "2", 6)
print(ExcelSheet.read_cell("1", "2"))
ExcelSheet.delete("1", "2")
print(ExcelSheet.read_cell("1", "2"))
