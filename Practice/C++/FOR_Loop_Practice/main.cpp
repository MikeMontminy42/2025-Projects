// Mike Montminy
// FOR loop practicing
// Start Date: 06/08/2025
// Most Recent Edit: 06/08/2025

#include <iostream>
#include <cmath>
using namespace std;

// OBJECTIVE: SUM of EVEN number that ARE divisibly by three upto (N)
int main() {

    int n;
    int sum = 0;
    cout << "ENTER A NUMBER BELOW: " << endl;
    cin >> n;
    while (n <= 0) {
        cout << "ERROR. INPUT MUST BE GREATER THAN ZERO. TRY ANOTHER NUMBER" << endl;
        cin >> n;
    }
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0 && i % 3 == 0) {
            sum += i;
            cout << i << endl;
        }
    }
    cout << "SUM OF ALL EVEN NUMBERS DIVISiBLE BY THREE FROM ZERO TO " << n << " is " << sum << endl;
    return 0;
}