#Campstone Husnul Adib

def menu_campstone():
    print('============================')
    print('Selamat Datang di Aplikasi Campstone - Data Mahasiswa');
    print('Mohon Pilih Menu di Bawah Ini:');
    print('Ketik 1: Untuk Melihat Data Mahasiswa');
    print('Ketik 2: Untuk Membuat Data Mahasiswa Baru');
    print('Ketik 3: Untuk Mengubah Data Mahasiswa');
    print('Ketik 4: Untuk Menghapus Data Mahasiswa');
    print('Ketik 5: Untuk Keluar Aplikasi');
    print('============================')

    user_input = input("Masukkan pilihan Anda: ");

    if(user_input=='1'):
        view_data()
    elif(user_input=='2'):
        create_data()
    elif(user_input=='3'):
        replace_data()
    elif(user_input=='4'):
        delete_data()
    elif(user_input=='5'):
        exit_app()
    else:
        print('Pilihan yang anda masukkan salah!')
        print('Anda baru saja mengetik angka ',user_input)
        print('Pilihlah angka 1-5 untuk memberi perintah')
        print('Kembali ke menu utama')
        menu_campstone()

data_mahasiswa={'123':'adib'}
print(data_mahasiswa)
def view_data():
    print('============================')
    print('Pilih 1 untuk menampilkan seluruh data mahasiswa')
    print('Pilih 2 untuk menampilkan data berdasarkan NIM')
    print('Pilih 3 untuk kembali ke menu utama')

    input_viewdata = input("Masukkan pilihan Anda: ");
    
    if (input_viewdata =='1'):
        if len(data_mahasiswa) != 0:
            print('Ada Data Mahasiswa')
            print(data_mahasiswa)
            view_data()
        else:
            print('Tidak Ada Data')
            view_data
    
    if (input_viewdata =='2'):
        search_nim = input("Masukkan NIM Anda: ")
        for nim, nama in data_mahasiswa.items():  
            if nim == search_nim:
                print(nama)
                view_data()
            else:
                print('NIM tidak ditemukan')
                view_data()
    
    if (input_viewdata=='3'):
        menu_campstone()

def create_data():
    print('============================')
    print('Pilih 1 untuk membuat data mahasiswa')
    print('Pilih 2 untuk kembali ke menu utama')
    
    input_createdata = input("Masukkan pilihan Anda: ");

    if (input_createdata=='1'):
        nim = str(input("Masukkan NIM : "));
        if(nim in data_mahasiswa):
            print("NIM sudah terdaftar");
            print('kembali ke menu utama?:')
            input_simpan = str(input('Y/N = '))
            if input_simpan == 'Y':
                menu_campstone()
            else:
                create_data()
        else:
            nama = str(input("Masukkan nama : "));
            print('Apakah Anda mau menyimpan data')
            input_simpan = str(input('Y/N = '))
            if input_simpan == 'Y':
                data_mahasiswa[nim] = nama;
                data_mahasiswa.update(data_mahasiswa)
                print('Data berhasil tersimpan')
                create_data()

    if (input_createdata=='2'):
        menu_campstone()
    
    else:
        create_data()

def replace_data():
    print('============================')
    print('Pilih 1 untuk membuat memperbaharui data')
    print('Pilih 2 untuk kembali ke menu utama')

    input_replace_data = input("Masukkan pilihan Anda: ");
    if (input_replace_data=='1'):
        nim = str(input("Masukkan NIM : "));
        if(nim not in data_mahasiswa):
            print("NIM Tidak Ditemukan");
        elif (nim in data_mahasiswa):
            print(data_mahasiswa.get(nim))
            opsi_replace= str(input('Apakah Anda Tetap Ingin Mengubah Data?(Y/N)= '))
            if opsi_replace== 'Y':
                nama = str(input("Masukkan Nama Terbaru : ")); 
                print('Apakah Anda yakin akan memperbaharui data')
                input_simpan = str(input('Y/N = '))
                if input_simpan == 'Y':
                    data_mahasiswa[nim] = nama;
                    data_mahasiswa.update(data_mahasiswa)
                    print('Data berhasil diperbaharui')
                    replace_data()
            elif opsi_replace== 'N':
                print('Anda dialihkan ke menu sebelumnya')
                replace_data()

    
    if (input_replace_data=='2'):
        menu_campstone()
    
    else:
        print('Pilihan tidak Dikenali')
        print('Anda dialihkan ke menu sebelumnya')
        replace_data()    

def delete_data():
    print('============================')
    print('Pilih 1 untuk membuat menghapus data')
    print('Pilih 2 untuk kembali ke menu utama')

    input_delete_data = input("Masukkan pilihan Anda: ");
    if (input_delete_data =='1'):
        nim = str(input("Masukkan NIM : "));
        if(nim not in data_mahasiswa):
            print("NIM Tidak Ditemukan");
        elif (nim in data_mahasiswa):
            cetak_nim =data_mahasiswa.get(nim)
            print(cetak_nim)
            opsi_delete= str(input('Apakah Anda Tetap Ingin Menghapus Data?(Y/N)= '))
            if opsi_delete== 'Y':
                del data_mahasiswa[nim]
                print('Data berhasil dihapus')
                delete_data()
            elif opsi_delete== 'N':
                print('Anda dialihkan ke menu sebelumnya')
                delete_data()
    
    if ( input_delete_data=='2'):
        menu_campstone()

    else:
        print('Pilihan tidak Dikenali')
        print('Anda dialihkan ke menu sebelumnya')
        delete_data()

def exit_app():
    print('Apakah Anda Yakin Ingin Keluar?')
    opsi_exit=str(input('Y/N?= '))
    if opsi_exit=='Y':
        exit()
    else:
        menu_campstone()

menu_campstone()