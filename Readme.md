# BookTracker

## Deskripsi
Aplikasi ini terinspirasi dari hobi saya yang suka membaca novel. Saya sering lupa judul buku yang pernah saya baca, kapan saya menyelesaikannya, dan seberapa saya menyukainya. Oleh karena itu, BookTracker hadir untuk membantu mencatat, menyimpan, dan mengelola daftar bacaan saya, baik fiksi maupun non-fiksi.
Aplikasi ini dibangun menggunakan bahasa Python dengan pendekatan OOP (Object-Oriented Programming) dan dilengkapi antarmuka GUI berbasis `tkinter`. Data buku disimpan dalam format JSON sehingga mudah dipindahkan atau dibagikan.

-------------------------------------------------------------------------------------------------------------------------------------------------

## Cara Menjalankan

1. **Persyaratan Sistem**
- Python 3.6 atau lebih baru.
- Tidak membutuhkan library tambahan karena hanya menggunakan tkinker dan json (sudah termasuk di Python).

2. **Langkah-langkah Menjalankan**
   
a. **clone atau Download Proyek**
Jika menggunakan Git :
git clone https://github.com/username/BookTracker.git
cd BookTracker
atau bisa download zip, kemudian ekstrak di folder lokal. 

b.**Jalankan aplikasi**
- Buka terminal di folder proyek.
- Jalankan perintah : python main.py
Jika menggunakan VScode, cukup buka file main.py dan klik run.

3. **Fungsi Aplikasi**
- Tambah buku : Mengisi informasi buku yang telah dibaca.
- Hapus buku : Menghapus buku dari daftar.
- Semua data tersimpan di file data/books.json secara otomatis.

4.**Catatan Tambahan**
- Jika file books.json belum ada, aplikasi akan membuatnya secara otomatis saat pertama kali dijalankan.
- Format penyimpanan bersifat JSON, sehingga mudah dipindahkan atau dibaca secara manual.

