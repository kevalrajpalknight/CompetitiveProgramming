#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    string S, J;
   while (t--) {
        cin>>S>>J;
        int count = 0;
        for (int i=0; i<J.size(); i++) {
            for (int j=0; j<S.size(); j++){
                if (J[i] == S[j]){
                    count++; break;
                }
            }

        }
        cout << count << endl;
   }
    
    return 0;
}
