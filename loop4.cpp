#include <iostream>

using namespace std;

int main()
{
    int x, sum;
    x = 1;
    sum = 0;
    float avg;
    for (int n = x; n <=20; n++) {
        cout << n <<endl;
        sum=sum+n;
        avg=(float)sum/n;
    }
    cout << "Jumlah = " << sum << endl;
    cout << "Rata-Rata = " << avg << endl;
    return 0;
}
