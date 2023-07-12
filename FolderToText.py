import os
import re
from datetime import datetime
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog, messagebox, Radiobutton, IntVar

class LocalRepoScraper:
    def __init__(self, repo_paths, output_path, output_filename, selected_file_types=[], filter_files=True):
        self.repo_paths = repo_paths
        self.output_path = output_path
        self.output_filename = output_filename
        self.selected_file_types = selected_file_types
        self.filter_files = filter_files

    def fetch_all_files(self):
        files_data = []
        for file_path in self.repo_paths:
            # Check if file type is in selected file types
            if not self.filter_files or any(file_path.endswith(file_type) for file_type in self.selected_file_types):
                relative_path = os.path.basename(file_path)
                file_content = ""
                file_content += f"\n'''--- {relative_path} ---\n"
                try:
                    with open(file_path, 'rb') as f:  # Open file in binary mode
                        content = f.read()
                    try:
                        # Try decoding as UTF-8
                        content_decoded = content.decode('utf-8')
                    except UnicodeDecodeError:
                        # If decoding fails, replace non-decodable parts
                        content_decoded = content.decode('utf-8', errors='replace')
                    file_content += content_decoded
                except Exception as e:  # catch any reading errors
                    print(f"Error reading file {file_path}: {e}")
                    continue
                file_content += "\n'''"
                files_data.append(file_content)
                print(f"Processed file {file_path}: size {os.path.getsize(file_path)} bytes")  # Print file size
            else:
                print(f"Skipping file {file_path}: Does not match selected types.")
        return files_data

    def write_to_file(self, files_data):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{self.output_filename}_{timestamp}.txt"
        output_file_path = os.path.join(self.output_path, filename)
        with open(output_file_path, "w", encoding='utf-8') as f:
            f.write(f"*Local Files*\n")
            for file_data in files_data:
                f.write(file_data)
        return output_file_path

    def clean_up_text(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        cleaned_text = re.sub('\n{3,}', '\n\n', text)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

    def run(self):
        print("Fetching all files...")
        files_data = self.fetch_all_files()

        print("Writing to file...")
        filename = self.write_to_file(files_data)

        print("Cleaning up file...")
        self.clean_up_text(filename)

        print("Done.")
        return filename

class FolderToTextGUI:
    def __init__(self, master):
        self.master = master
        master.title("Folder to Text")

        self.repo_path_label = Label(master, text="Local Files:")
        self.repo_path_entry = Button(master, text="Browse...", command=self.browse_repo_path)

        self.file_types_label = Label(master, text="File Types (comma separated):")
        self.file_types_entry = Entry(master)

        self.output_path_label = Label(master, text="Output Path:")
        self.output_path_entry = Button(master, text="Browse...", command=self.browse_output_path)

        self.output_filename_label = Label(master, text="Output Filename:")
        self.output_filename_entry = Entry(master)

        self.filter_files = IntVar()
        self.filter_files.set(1)  # Set filtering to be on by default
        self.filter_files_label = Label(master, text="Filter Files:")
        self.filter_files_on = Radiobutton(master, text="On", variable=self.filter_files, value=1)
        self.filter_files_off = Radiobutton(master, text="Off", variable=self.filter_files, value=0)

        self.run_button = Button(master, text="Run", command=self.run)

        self.repo_path_label.grid(row=0, column=0, sticky="E")
        self.repo_path_entry.grid(row=0, column=1)

        self.file_types_label.grid(row=1, column=0, sticky="E")
        self.file_types_entry.grid(row=1, column=1)

        self.output_path_label.grid(row=2, column=0, sticky="E")
        self.output_path_entry.grid(row=2, column=1)

        self.output_filename_label.grid(row=3, column=0, sticky="E")
        self.output_filename_entry.grid(row=3, column=1)

        self.filter_files_label.grid(row=4, column=0, sticky="E")
        self.filter_files_on.grid(row=4, column=1, sticky="W")
        self.filter_files_off.grid(row=4, column=1)

        self.run_button.grid(row=5, column=1)

        self.repo_paths = ()
        self.output_path = ""

    def browse_repo_path(self):
        new_repo_paths = filedialog.askopenfilenames()
        if not new_repo_paths:
            return
        self.repo_paths += new_repo_paths  # Add new selected files to existing ones
        self.repo_path_label.config(text=f"Selected Files: {len(self.repo_paths)}")

    def browse_output_path(self):
        self.output_path = filedialog.askdirectory()
        if not self.output_path:
            return
        self.output_path_label.config(text=f"Output Path: {self.output_path}")

    def run(self):
        selected_file_types = [ftype.strip() for ftype in self.file_types_entry.get().split(',')]
        output_filename = self.output_filename_entry.get()
        if not output_filename:
            messagebox.showerror("Error", "Please enter an output filename.")
            return
        if not self.repo_paths:
            messagebox.showerror("Error", "Please select files.")
            return
        if not self.output_path:
            messagebox.showerror("Error", "Please select an output path.")
            return
        scraper = LocalRepoScraper(self.repo_paths, self.output_path, output_filename, selected_file_types, bool(self.filter_files.get()))
        scraper.run()

if __name__ == "__main__":
    root = Tk()
    gui = FolderToTextGUI(root)
    root.mainloop()
