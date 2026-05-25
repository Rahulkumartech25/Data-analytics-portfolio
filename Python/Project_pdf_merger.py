import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter


class PdfMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("500x380")
        self.root.resizable(False, False)

        self.pdf_files = []
        self._build_ui()

    def _build_ui(self):
        frame = tk.Frame(self.root, padx=12, pady=12)
        frame.pack(fill=tk.BOTH, expand=True)

        title = tk.Label(frame, text="PDF Merger", font=("Segoe UI", 16, "bold"))
        title.pack(pady=(0, 10))

        button_frame = tk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))

        add_button = tk.Button(button_frame, text="Add PDF Files", command=self.add_files, width=14)
        add_button.pack(side=tk.LEFT, padx=(0, 6))

        remove_button = tk.Button(button_frame, text="Remove Selected", command=self.remove_selected, width=14)
        remove_button.pack(side=tk.LEFT, padx=(0, 6))

        clear_button = tk.Button(button_frame, text="Clear All", command=self.clear_files, width=10)
        clear_button.pack(side=tk.LEFT)

        list_frame = tk.Frame(frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.file_listbox = tk.Listbox(list_frame, selectmode=tk.EXTENDED, height=10)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        output_frame = tk.Frame(frame)
        output_frame.pack(fill=tk.X, pady=(10, 6))

        output_label = tk.Label(output_frame, text="Output file:")
        output_label.pack(side=tk.LEFT)

        self.output_entry = tk.Entry(output_frame)
        self.output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(8, 0))
        self.output_entry.insert(0, "Merged.pdf")

        merge_button = tk.Button(frame, text="Merge PDFs", command=self.merge_pdfs, bg="#4CAF50", fg="white", padx=10, pady=6)
        merge_button.pack(pady=(6, 4))

        self.status_label = tk.Label(frame, text="Select PDF files to merge.", anchor=tk.W)
        self.status_label.pack(fill=tk.X, pady=(4, 0))

    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF Files", "*.pdf")],
        )

        if not files:
            return

        for file_path in files:
            if file_path not in self.pdf_files:
                self.pdf_files.append(file_path)
                self.file_listbox.insert(tk.END, file_path)

        self.status_label.config(text=f"{len(self.pdf_files)} file(s) selected.")

    def remove_selected(self):
        selected_indices = list(self.file_listbox.curselection())
        if not selected_indices:
            self.status_label.config(text="No selected file to remove.")
            return

        for index in reversed(selected_indices):
            self.file_listbox.delete(index)
            del self.pdf_files[index]

        self.status_label.config(text=f"{len(self.pdf_files)} file(s) remaining.")

    def clear_files(self):
        self.file_listbox.delete(0, tk.END)
        self.pdf_files.clear()
        self.status_label.config(text="All files cleared.")

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("No files", "Please add one or more PDF files to merge.")
            return

        output_name = self.output_entry.get().strip()
        if not output_name:
            messagebox.showwarning("Output name", "Please enter a valid output file name.")
            return

        try:
            writer = PdfWriter()
            for pdf_path in self.pdf_files:
                writer.append(pdf_path)

            writer.write(output_name)
            self.status_label.config(text=f"Merged {len(self.pdf_files)} files into '{output_name}'.")
            messagebox.showinfo("Success", f"PDFs merged successfully into '{output_name}'.")
        except Exception as exc:
            messagebox.showerror("Merge failed", f"Could not merge PDFs:\n{exc}")
            self.status_label.config(text="Merge failed. See error message.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PdfMergerApp(root)
    root.mainloop()

