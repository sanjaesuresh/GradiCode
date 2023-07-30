import os
import importlib
import pytest
import sys
import tkinter

class GradeCode:
    
    def __init__(self, submissions_path, unit_test_path, module_path):
        self.submissions_path = submissions_path
        self.unit_test_path = unit_test_path
        self.module_path = module_path
        
    def import_module_from_path(self, module_name, module_path):
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    
    def print_report(self, report):
        student_id = report["student_id"]
        total_tests = report['total_tests']
        successful_tests = report['successful_tests']
        grade = (successful_tests / total_tests) * 100
            
        report = ''
        report += f'\n Student ID: {student_id}'
        report += f'\n {successful_tests} of {total_tests} tests passed.'
        report += f'\n Grade: {grade:.2f}%'
        report += f'\n---------------------------------------------------'
            
        print(report)
        
    def collect_and_run_tests(self, submission, test_file_path, submission_path):
        class TestResultCollector:
            def __init__(self):
                self.total_tests = 0
                self.successful_tests = 0

            def pytest_collection_modifyitems(self, config, items):
                self.total_tests = len(items)

            def pytest_terminal_summary(self, terminalreporter, exitstatus):
                passed_tests = terminalreporter.stats.get("passed", [])
                self.successful_tests = len(passed_tests)

        test_result_collector = TestResultCollector()

        # Run pytest with the custom plugin
        pytest.main([test_file_path, submission_path], plugins=[test_result_collector])

        # Extract the test results
        test_result = {
            "student_id": submission,
            "total_tests": test_result_collector.total_tests,
            "successful_tests": test_result_collector.successful_tests,
        }

        return test_result
    
    def collect_test_items(self, test_file_path):
        collected_items = []

        # Define a custom hook to collect the test items
        def pytest_collection_modifyitems(config, session, items):
            nonlocal collected_items
            collected_items = items

        # Run pytest with the custom hook to collect the test items
        pytest.main(['--collect-only', test_file_path], plugins=[pytest_collection_modifyitems])

        return collected_items
        
    def run_tests(self, unit_test_path, submissions_folder_path, module_path):
        sys.path.append(module_path)

        submissions = os.listdir(submissions_folder_path)
        submissions = sorted(submissions)
        report = {}  # Initialize the report dictionary
        
        print(f"Submissions folder: {submissions_folder_path}")
        print(f"Files in the folder: {submissions}")

        for submission in submissions:
            if submission.endswith('.py'):
                print(f"Testing {submission}...")

                submission_path = os.path.join(submissions_folder_path, submission)

                try:
                    test_result = self.collect_and_run_tests(submission[:-3], unit_test_path, submission_path)
                    report[submission] = test_result
                    self.print_report(report[submission])
                    print(f"{submission} passed {test_result['successful_tests']} of {test_result['total_tests']} tests.")
                except Exception as e:
                    print(f"Error testing {submission}: {e}")
    
        report = {
            'naye1330.py': {'student_id': 'naye1330', 'total_tests': 12, 'successful_tests': 10, 'grade': 83},
            'sure3530.py': {'student_id': 'sure3530', 'total_tests': 12, 'successful_tests': 12, 'grade': 100},
            # Add more reports here
        }

        app = ReportWindow(report)
        app.mainloop()
        return report
    
import tkinter as tk

class ReportWindow(tk.Tk):
    def __init__(self, reports):
        super().__init__()
        self.title("Test Reports")
        self.geometry("500x400")

        self.reports = reports

        self.create_widgets()

    def create_widgets(self):
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_area = tk.Text(self, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        text_area.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=text_area.yview)

        for submission, report in self.reports.items():
            text_area.insert(tk.END, f"Submission: {submission}\n")
            text_area.insert(tk.END, f"Student ID: {report['student_id']}\n")
            text_area.insert(tk.END, f"Total Tests: {report['total_tests']}\n")
            text_area.insert(tk.END, f"Successful Tests: {report['successful_tests']}\n")
            text_area.insert(tk.END, f"Grade: {report['grade']}%\n")
            text_area.insert(tk.END, "---------------------------\n")

        

if __name__ == "__main__":
    submission_test_path = "testing_files/submissions_test"
    test_path = "testing_files/test_calculator.py"
    module_path = "src"
    
    gradicode = GradeCode(submission_test_path, test_path, module_path)
    gradicode.run_tests(test_path, submission_test_path, module_path)