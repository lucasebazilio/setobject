#include <iostream>
using namespace std;

int main() {
    int linearProbes = 0, randomProbes = 0;
    int numInputs = 0;
    int totalLinearProbes = 0;
    int totalRandomProbes = 0;
    int totalProbes = 0;
    

    while (cin >> linearProbes >> randomProbes) {
        numInputs++;
        totalLinearProbes += linearProbes;
        totalRandomProbes += randomProbes;
        totalProbes += linearProbes + randomProbes;
    }

    double avgLinearProbes = 0.0, avgRandomProbes = 0.0, avgTotalProbes = 0.0;

    if (numInputs > 0) {
        avgLinearProbes = static_cast<double>(totalLinearProbes) / numInputs;
        avgRandomProbes = static_cast<double>(totalRandomProbes) / numInputs;
        avgTotalProbes = static_cast<double>(totalProbes) / numInputs;
    }
    cout << "L,R,T:" << endl;
    cout << avgLinearProbes << ',' << avgRandomProbes << ',' << avgTotalProbes << endl;
   /* cout << "Average number of linear probes: " << avgLinearProbes << endl;
    cout << "Average number of random probes: " << avgRandomProbes << endl;
    cout << "Average number of total probes: " << avgTotalProbes << endl; */

    return 0;
}
