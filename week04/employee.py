class Employee:
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        stripped = value.strip()
        if not stripped:
            raise ValueError("Name cannot be empty.")
        self._name = stripped

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        stripped = value.strip()
        if not stripped:
            raise ValueError("Employee ID cannot be empty.")
        self._employee_id = stripped

    @property
    def hourly_rate(self):
        return self._hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self._hourly_rate = value

    @property
    def hours_worked(self):
        return self._hours_worked
    
    @hours_worked.setter
    def hours_worked(self, value):
        value = float(value)
        if value < 0 or value > 168:
            raise ValueError("Hours worked must be between 0 and 168.")
        self._hours_worked = value

    def calculate_gross_pay(self):
        if self.hours_worked <= 40:
            return self.hours_worked * self.hourly_rate
        overtime = self.hours_worked - 40
        return (40 * self.hourly_rate) + (overtime * self.hourly_rate * 1.5)

        
    
    def __str__(self):
        return f"Employee: {self.name:<15}, ID: {self.employee_id:<10}, Hourly Rate: ${self.hourly_rate:<6.2f}, Hours Worked: {self.hours_worked:<6.1f}, Gross Pay: ${self.calculate_gross_pay():8.2f}"