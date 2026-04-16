from payroll_processor import PayrollProcessor
from payroll_report import PayrollReport    

def main():
    processor = PayrollProcessor()
    processor.load_from_file("employees.txt")
    report = PayrollReport(processor)

    while True:
        print("\nView Employee List (1), Payroll Summary (2), Generate Report File (3), Exit (4)")
        choice = input("Enter your choice: ")

        if choice == "1":
            report.display_all_employees()
        elif choice == "2":
            report.display_payroll_summary()
        elif choice == "3":
            report.generate_report_file("payroll_report.txt")
        elif choice == "4":
           break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()