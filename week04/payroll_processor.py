from employee import Employee


class PayrollProcessor:
    def __init__(self):
        self.employees = []

    @property
    def employees(self):
        return list(self._employees)
    @employees.setter
    def employees(self, value):
        if not isinstance(value, list):
            raise ValueError("Employees must be a list.")
        for emp in value:
            if not isinstance(emp, Employee):
                raise ValueError("All items in employees must be Employee instances.")
        self._employees = value
    
    def load_from_file(self,filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split("\t")
                    if len(parts) != 4:
                        print(f"Skipping invalid line: {line}")
                        continue
                    try:
                        emp = Employee(parts[0], parts[1], parts[2], parts[3])
                        self._employees.append(emp)
                    except ValueError as e:
                        print(f"Error processing line: {line} - {e}")
        except FileNotFoundError:
            print(f"File not found: {filename}")

    
    def calculate_total_payroll(self):
        return sum(emp.calculate_gross_pay() for emp in self._employees)
    
    def get_employee_count(self):
        return len(self._employees)
    
    def calculate_average_pay(self):
        count = self.get_employee_count()
        return self.calculate_total_payroll() / count if count > 0 else 0
    
    def find_highest_paid_employee(self):
        return max(self._employees, key=lambda emp: emp.calculate_gross_pay(), default=None)
    
    def find_lowest_paid_employee(self):
        return min(self._employees, key=lambda emp: emp.calculate_gross_pay(), default=None)
       



    