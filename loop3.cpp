#include <iostream>

using namespace std;

int main()
{
    int x;
    for (x = 100; x >= 1; x--) {
        cout << x <<endl;
        if (x == 55) {
            break;
        }
    }
    return 0;
}
