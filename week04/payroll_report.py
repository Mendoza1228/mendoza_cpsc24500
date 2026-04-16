class PayrollReport:
    def __init__(self, processor):
        self.processor = processor

    def display_all_employees(self):
        print("\n ***** Employee List *****")
        for emp in self.processor.employees:
            print(emp)

    def display_payroll_summary(self):
        p = self.processor
        highest = p.find_highest_paid_employee()
        lowest = p.find_lowest_paid_employee()

        print("\n ***** Payroll Summary *****")
        print(f"Total Employees: {p.get_employee_count()}")
        print(f"Total Payroll: ${p.calculate_total_payroll():.2f}")
        print(f"Average Pay: ${p.calculate_average_pay():.2f}")
        print(f"Highest Paid Employee: {highest.name} (${highest.calculate_gross_pay():.2f})" if highest else "No employees found.")
        print(f"Lowest Paid Employee: {lowest.name} (${lowest.calculate_gross_pay():.2f})" if lowest else "No employees found.")

    def generate_report_file(self, filename):
        
        with open(filename, 'w') as f:
            f.write("PAYROLL REPORT\n" + "="*50 + "\n")
            for emp in self.processor.employees:
                f.write(str(emp) + "\n")
            f.write("\nSUMMARY\n")
            f.write(f"Total Payroll: ${self.processor.calculate_total_payroll():.2f}\n")
        print(f"Report generated successfully: {filename}")

               