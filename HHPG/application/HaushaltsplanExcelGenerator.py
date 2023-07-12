import openpyxl

class HaushaltsplanExcelBuilder:
    def __init__(self):
        self.workbook = openpyxl.Workbook()
        self.worksheet = self.workbook.active
        self.row_index = 2

    def add_header(self):
        self.worksheet['A1'] = 'Projekt Name'
        self.worksheet['B1'] = 'Einnahmen'
        self.worksheet['C1'] = 'Ausgaben'

    def add_haushaltsposten(self, haushaltsposten):
        self.worksheet.cell(row=self.row_index, column=1, value=haushaltsposten.name)
        self.row_index += 1

        for projekt in haushaltsposten.projekte:
            self.worksheet.cell(row=self.row_index, column=2, value=projekt.einnahmen)
            self.worksheet.cell(row=self.row_index, column=3, value=projekt.ausgaben)
            self.row_index += 1

    def get_workbook(self):
        return self.workbook


class HaushaltsplanExcelGenerator:
    def __init__(self, haushaltsplan):
        self.haushaltsplan = haushaltsplan

    def generate_excel(self, file_name):
        builder = HaushaltsplanExcelBuilder()
        builder.add_header()

        for haushaltsposten in self.haushaltsplan.haushaltsposten:
            builder.add_haushaltsposten(haushaltsposten)

        workbook = builder.get_workbook()
        workbook.save(file_name)
