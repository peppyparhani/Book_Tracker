import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror, askyesno
import tkinter.simpledialog as sd 
from book import Novel, NonFiction
from book_manager import BookManager

class BookTrackerGUI :
    def __init__(self, root):
        self.root = root
        self.root.title ("📚 BookTracker - Catatan Buku")
        self.root.configure (bg="#fdfdfd")

        self.manager = BookManager()

        title_label = tk.Label(
            root,
            text="📖 Daftar Buku Kamu",
            font = ("Helvetica", 16, "bold"),
            bg = "#fdfdfd",
            fg = "#4a4a4a"
        )
        title_label.pack(padx=(20, 10))

        self.listbox = tk.Listbox(
            root,
            width=60,
            height=10,
            bg = "#fafafa",
            fg ="#444444",
            font=("Helvetica", 10),
            highlightthickness=1,
            highlightbackground="#cccccc",
            selectbackground="#d5e8ff"
        )
        self.listbox.pack(pady=10)

        btn_frame = tk.Frame (root, bg="#fdfdfd")
        btn_frame.pack(pady=10)


        btn_add = tk.Button(
            btn_frame,
            text="➕ Tambah Buku",
            command=self.add_book,
            bg = "#e3f2fd",
            fg = "#1e88e5",
            activebackground="#bbdefb",
            width=18,
            font=("Helvetica", 10, "bold")
        )
        
        btn_add.grid(row=0,column=0, padx=5)

        btn_refresh = tk.Button(
        btn_frame,
        text="🔄 Refresh",
        command=self.refresh_books,
        bg="#fce4ec",
        fg="#d81b60",
        activebackground="#f8bbd0",
        width=18,
        font=("Helvetica", 10, "bold")
        )
        btn_refresh.grid(row=0, column=1, padx=5)

        btn_delete = tk.Button(
            btn_frame,
            text ="🗑️ Hapus Buku",
            command=self.delete_book,
            bg="#fff3cd",
            fg="#ff6f00",
            width=18,
            font=("Helvetica", 10, "bold")
        )
        btn_delete.grid(row=0, column=2, padx=5)
    def refresh_books (self):
        self.listbox.delete(0, tk.END)
        for book in self.manager.get_books():
            display = f"{book.book_type()} | {book.title} | Penulis {book.author} | ⭐ {book.rating}/5"
            self.listbox.insert(tk.END, display)
    
    def add_book(self):
        try:
            book_type = sd.askstring ("Jenis buku", "Jenis buku (Novel / Non-Fiksi :)")
            if not book_type:
                return
            title = sd.askstring("Judul buku", " Masukkan Judul Buku :")
            author = sd.askstring("Penulis", "Masukkan Nama Penulis")
            genre = sd.askstring("Genre", "Masukkan Genre Buku :")
            date = sd.askstring("Tanggal", "Masukkan Tanggal (YYYY-MM-DD)")
            rating = sd.askfloat("Rating", "Masukkan Rating (1-5) :")

            if all([book_type, title,author,genre,date,rating]) :
                if book_type.lower() == "novel" :
                    book = Novel (title, author, genre, date, rating)
                else :
                    book = NonFiction (title, author, genre, date, rating)

                self.manager.add_book(book)
                showinfo("Sukses", "Buku berhasil ditambahkan!! 🎉")
                self.refresh_books()

            else :
                showwarning("Peringatan", "Mohon Lengkapi Semua Data.")
        except Exception as e :
            showerror("Error", f"Terjadi kesalahan : {e}")

    def delete_book(self) :
        selected_index = self.listbox.curselection()
        if not selected_index :
            showwarning("Peringatan", "Pilih Buku Yang Ingin Dihapus.")
            return
        
        index = selected_index[0]
        book = self.manager.get_books()[index]
        confirm = askyesno("Konfirmasi Hapus", f"Apakah Yakin Ingin Menghapus : \n{book.title} oleh {book.author}?")
        if confirm:
            self.manager.remove_book(index)
            self.refresh_books()
            showinfo("Berhasil", "Buku Berhasil Dihapus.")