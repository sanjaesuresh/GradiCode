import tkinter as tk
from tkinter import * 
from tkinter import filedialog as fd
from tkinter.ttk import *
from gradeCode import GradeCode

def createGUI():
    root = tk.Tk()
    root.title("GradiCode")
    root.config(bg="#171810")
    
    logo_image = PhotoImage(file="pictures/GradiCode.png")
    logo = logo_image.subsample(2,2)
    logo_label = tk.Label(root, image = logo)
    logo_label.grid(row=0, column=3, rowspan=2, sticky="ew")
    logo_label.config(bg="#171810")
    
    label_zip_file = tk.Label(root, text="Zip File:")
    label_zip_file.grid(row=3, column=2, sticky="e")
    label_zip_file.config(bg="#171810")
    entry_zipfile_path = tk.Label(root, borderwidth=2, relief="sunken")
    entry_zipfile_path.grid(row=3, column=3, sticky="nswe")
    button_browse_zip = tk.Button(root, text="Browse", highlightbackground="#171810", command = lambda : open_folder(entry_zipfile_path))
    button_browse_zip.grid(row=3, column=4)

    label_testing_file = tk.Label(root, text="JUnit Testing File:")
    label_testing_file.grid(row=4, column=2, sticky="e")
    label_testing_file.config(bg="#171810")
    testing_file_path = tk.Label(root, borderwidth=2, relief="sunken")
    testing_file_path.grid(row=4, column=3, sticky="nswe")
    testing_file_path.config(bg="#171810")
    button_browse_testing = tk.Button(root, text="Browse", highlightbackground="#171810", command = lambda : open_unittest(testing_file_path))
    button_browse_testing.grid(row=4, column=4)

    addConstraintLabel = tk.Label(root, text="Add Constraints:")
    addConstraintLabel.grid(row=5, column=2, sticky="e")
    addConstraintLabel.config(bg="#171810")
    entry_constraints_path = tk.Label(root, borderwidth=2, relief="sunken")
    entry_constraints_path.grid(row=5, column=3, sticky="nswe")
    entry_constraints_path.config(bg="#171810")
    button_browse_constraints = tk.Button(root, text="Browse", highlightbackground="#171810", command = lambda : open_txt(entry_constraints_path))
    button_browse_constraints.grid(row=5, column=4)
    
    addConstaintFormatLabel=tk.Label(root, text="Constraints Format: Keyword, Function Name, Limit, Points Deducted")
    addConstaintFormatLabel.grid(row=6, column=3)
    addConstaintFormatLabel.config(bg="#171810")
    
    button_process = tk.Button(root, text="Process Grades", fg='red', highlightbackground="#171810", command = lambda :
                            process_grades(entry_zipfile_path, testing_file_path, entry_constraints_path))
    button_process.grid(row=7, column=3)
    
    root.mainloop()

def open_folder(label):
    folder_path = fd.askdirectory(title='Choose Class Submission Folder')
    label.config(text= folder_path)
    return folder_path

def open_txt(label):
    txt_path = fd.askopenfile(mode ='rb', title='Choose Constraint TXT File', filetypes = (("Text Files", "*.txt*"),))
    label.config(text = txt_path)
    return txt_path
        
def open_unittest(label):
    test_path = fd.askopenfile(mode='rb', title="Choose Unit Test File")
    label.config(text = test_path)
    return test_path

def process_grades(entry_zipfile_path, testing_file_path, entry_constraints_path):
    submission_test_path = "testing_files/submissions_test"
    test_path = "testing_files/test_calculator.py"
    module_path = "src"
    
    gradicode = GradeCode(submission_test_path, test_path, module_path)
    gradicode.run_tests(test_path, submission_test_path, module_path)
    
if __name__ == "__main__":
    createGUI()
    