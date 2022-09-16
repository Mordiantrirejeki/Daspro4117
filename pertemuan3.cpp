#include <iostream>

using namespace std;

int main()
{

    //Fungsi cin digunakan untuk mengambil input data dari teks yang dituliskan.
    //Di Dalam perintah Cin membutuhkan variabel untuk menyimpan data yang diinputkan.

    cout << "--------------------------------------------------------------------- \n\n";
    cout << "\t\tHallo, saya lagi belajar Cin \n \n" << endl;
    // \t untuk memberikan tab

    string nama, nim;
    int umur;
    float tb;
    char jk;

    cout << "\tMasukan Nama           : ";
    getline (cin, nama);
    //getline berfungsi untuk menambahkan spasi antar kata

    cout << "\tMasukan NIM            : ";
    cin >> nim;

    cout << "\tMasukan Umur           : ";
    cin >> umur;

    cout << "\tTinggi Badan           : ";
    cin >> tb;

    cout << "\tJenis Kelamin          : ";
    cin >> jk;
    cout << "\n";

    cout << "\tSelamat Datang " << nama << ", kamu harus semangat !!!" << endl;
    cout << "\tNIM anda adalah " << nim << "." << endl;
    cout << "\tUsia anda sekarang " << umur << " tahun." << endl;
    cout << "\tSaat ini tinggi badan anda " << tb << " cm." << endl;
    cout << "\tJenis Kelamin anda " << jk << ".\n" << endl;

    cout << "---------------------------------------------------------------------";
    return 0;
}
