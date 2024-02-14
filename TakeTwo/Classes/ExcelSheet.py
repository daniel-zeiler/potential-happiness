import collections
from typing import List


class Cell:
    def __init__(self, row: str, column: str, value: int):
        self.row = row
        self.column = column
        self.value = value


class ExcelSheet:
    def __init__(self):
        self.cells = collections.defaultdict(Cell)

    def __str__(self):
        result = ""
        for cell in self.cells.values():
            result += f"row: {cell.row} column: {cell.column} value: {cell.value}\n"
        return result

    def assign_value(self, row: str, column: str, value: int) -> Cell:
        if row + column not in self.cells:
            self.cells[row + column] = Cell(row, column, value)
        else:
            self.cells[row + column].value = value
        return self.cells[row + column]

    def delete_value(self, row: str, column: str):
        if row + column in self.cells:
            del self.cells[row + column]

    def read_value(self, row, column) -> int:
        if row + column in self.cells:
            return self.cells[row + column].value

    def perform_operations(self, row: str, column: str, initial_value: int, cell_coordinates: List[str],
                           operations: List[str]) -> Cell:
        new_cell = self.assign_value(row, column, initial_value)
        for cell_coordinates, operation in zip(cell_coordinates, operations):
            if cell_coordinates not in self.cells:
                raise Exception(f"Cell {cell_coordinates} does not exist")
            cell = self.cells[cell_coordinates]
            if operation == "+":
                new_cell.value += cell.value
            elif operation == "-":
                new_cell.value -= cell.value
            elif operation == "*":
                new_cell.value *= cell.value
            elif operation == "/":
                new_cell.value /= cell.value
            else:
                raise Exception(f"Unkown operation:{operation}")
        return new_cell


excel_sheet = ExcelSheet()
cell_one = excel_sheet.assign_value("1", "2", 3)
cell_two = excel_sheet.assign_value("1", "1", 3)
excel_sheet.assign_value("1", "2", 5)
cell_three = excel_sheet.perform_operations("1", "3", 0, ["12", "11"], ["+", "+"])
cell_four = excel_sheet.perform_operations("1", "4", 70, ["12", "11", "13"], ["+", "*", "-"])
print(excel_sheet)
