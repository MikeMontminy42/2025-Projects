#include <iostream>

using namespace std;

int fibNum = 0;

int userInput(){
    cout << "ENTER AMOUNT OF FIBONACCI NUMBERS TO PRINT: ";
    cin >> fibNum;

    if (fibNum == 0) {
        cout << "INVALID. MUST BE A NUMBER GREATER THAN 0." << endl;
    }
}

int calculateFibonacci() {
    unsigned long long a = 0;
    unsigned long long b = 1;
    unsigned long long i = 1;
    unsigned long long nextFib = 0;

    while (i < fibNum) {
        cout << a << endl;
        nextFib = a + b;
        a = b;
        b = nextFib;
        i = i + 1;
    }
    return 0;
}

int main() {
    userInput();
    calculateFibonacci();
}