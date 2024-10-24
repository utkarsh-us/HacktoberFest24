import openpyxl
import pandas as pd

def remove_spaces_from_xlsx(file_path):
    # Load the workbook and select the active worksheet
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Iterate through all cells in the worksheet
    for row in sheet.iter_rows():
        for cell in row:
            if isinstance(cell.value, str):
                # Remove spaces from the cell value
                cell.value = cell.value.replace(" ", "")

    # Save the modified workbook
    workbook.save(file_path)

if __name__ == "__main__":
    file_path = '/home/linux/Downloads/phrases.xlsx'
    remove_spaces_from_xlsx(file_path)
    print("Spaces removed successfully.")