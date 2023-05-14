import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QLineEdit


class Table(QWidget):
    def __init__(self, n, m):
        super().__init__()
        self.n = n
        self.m = m
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # add the column labels
        for j in range(self.m):
            label = QLabel(f'O{j+1}', self)
            self.grid.addWidget(label, 0, j+1)

        # add the row labels and cells
        self.table = []
        for i in range(self.n):
            row = []
            label = QLabel(f'D{i+1}', self)
            self.grid.addWidget(label, i+1, 0)
            for j in range(self.m):
                cell = QLineEdit()
                row.append(cell)
                self.grid.addWidget(cell, i+1, j+1)
            self.table.append(row)

        self.init_button = QPushButton('Initialize', self)
        self.init_button.clicked.connect(self.initialize_table)
        self.grid.addWidget(self.init_button, self.n + 1, 0, 1, self.m+1)

        self.row_min_button = QPushButton('Calculate row min', self)
        self.row_min_button.clicked.connect(self.calculate_row_min)
        self.grid.addWidget(self.row_min_button, self.n + 2, 0, 1, self.m+1)

        self.row_max_button = QPushButton('Calculate row max', self)
        self.row_max_button.clicked.connect(self.calculate_row_max)
        self.grid.addWidget(self.row_max_button, self.n + 3, 0, 1, self.m+1)

        self.row_avg_button = QPushButton('Calculate row avg', self)
        self.row_avg_button.clicked.connect(self.calculate_row_avg)
        self.grid.addWidget(self.row_avg_button, self.n + 4, 0, 1, self.m+1)

        self.row_l_button = QPushButton('Calculate row l', self)
        self.row_l_button.clicked.connect(self.calculate_row_l)
        self.grid.addWidget(self.row_l_button, self.n + 5, 0, 1, self.m+1)

        self.result_label = QLabel(self)
        self.grid.addWidget(self.result_label, self.n + 6, 0, 1, self.m+1)

        self.l_value_edit = QLineEdit(self)
        self.l_value_edit.setText('0')
        self.grid.addWidget(self.l_value_edit, self.n + 7, 0, 1, self.m+1)

        self.laplace_button = QPushButton('Calculate Laplace', self)
        self.laplace_button.clicked.connect(self.calculate_laplace)
        self.grid.addWidget(self.laplace_button, self.n + 8, 0, 1, self.m+1)

        self.savage_button = QPushButton('Calculate Savage', self)
        self.savage_button.clicked.connect(self.calculate_savage)
        self.grid.addWidget(self.savage_button, self.n + 9, 0, 1, self.m+1)

        # Update the result_label row in the grid
        self.grid.addWidget(self.result_label, self.n + 10, 0, 1, self.m+1)

    def calculate_laplace(self):
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                value = self.table[i][j].text()
                if value == '':
                    value = '0'
                row.append(int(value))
            row_avg = sum(row) / self.m
            result.append(row_avg)
        max_laplace = max(result)
        max_laplace_row = result.index(max_laplace) + 1
        self.result_label.setText(f'Maximum of Laplace values: {max_laplace}, corresponding to row {max_laplace_row}')

    def calculate_savage(self):
        regrets = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                value = self.table[i][j].text()
                if value == '':
                    value = '0'
                row.append(int(value))
            regrets.append(row)

        max_regrets = []
        for i in range(self.n):
            max_regret = float('-inf')
            for j in range(self.m):
                regret = max(regrets[row][j] for row in range(self.n)) - regrets[i][j]
                max_regret = max(max_regret, regret)
            max_regrets.append(max_regret)

        min_max_regret = min(max_regrets)
        min_max_regret_row = max_regrets.index(min_max_regret) + 1
        self.result_label.setText(f'Minimum of maximum regrets: {min_max_regret}, corresponding to row {min_max_regret_row}')


    def initialize_table(self):
        for i in range(self.n):
            for j in range(self.m):
                value = random.randint(-100, 100)
                self.table[i][j].setText(str(value))

    def calculate_row_min(self):
        result = []
        row_num = -1
        max_min_value = float('-inf')
        for i in range(self.n):
            row = []
            for j in range(self.m):
                value = self.table[i][j].text()
                if value == '':
                    value = '0'
                row.append(int(value))
            row_min = min(row)
            result.append(row_min)
            if row_min > max_min_value:
                max_min_value = row_min
                row_num = i
        self.result_label.setText(f'Maximum of minimums of each row: {max(result)}, corresponding to row {row_num+1}')

    def calculate_row_max(self):
        result = []
        row_num = -1
        max_max_value = float('-inf')
        for i in range(self.n):
            row = []
            for j in range(self.m):
                value = self.table[i][j].text()
                if value == '':
                    value = '0'
                row.append(int(value))
            row_max = max(row)
            result.append(row_max)
            if row_max > max_max_value:
                max_max_value = row_max
                row_num = i
        self.result_label.setText(f'Maximum of maximums of each row: {max(result)}, corresponding to row {row_num+1}')

    def calculate_row_avg(self):
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                value = self.table[i][j].text()
                if value == '':
                    value = '0'
                row.append(int(value))
            row_avg = sum(row) / self.m
            result.append(row_avg)
        max_avg = max(result)
        max_avg_row = result.index(max_avg) + 1
        self.result_label.setText(f'Maximum of averages of each row: {max_avg}, corresponding to row {max_avg_row}')

    def calculate_row_l(self):
        result = []
        a = self.l_value_edit.text()
        if a == '':
            a = '0.5'
        else:
            a = float(a)
        for i in range(self.n):
            row = []
            for j in range(self.m):
                value = self.table[i][j].text()
                if value == '':
                    value = '0'
                row.append(int(value))
            row_max = max(row)
            row_min = min(row)
            l = row_max * a + row_min * (1 - a)
            result.append(l)
        max_l = max(result)
        max_l_row = result.index(max_l) + 1
        self.result_label.setText(f'Maximum of l values for each column: {max_l}, corresponding to row {max_l_row}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    n = int(input('Enter n: '))
    m = int(input('Enter m: '))
    window = Table(n, m)
    window.show()
    sys.exit(app.exec_())
