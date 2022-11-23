#include <iostream>

using namespace std;

int main()
{
    for (int x = 1; x <=100; x++) {
        if (x % 2 == 1) {
            continue;
        }
        cout << "Nilai genap adalah " << x << endl;
    }
    return 0;
}
