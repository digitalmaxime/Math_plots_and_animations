#include <iostream>
using namespace std;

namespace show {
    void print(int mat[2][2], int M, int N) {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                cout << mat[i][j] << " ";
            }
            cout << endl;
        }
    }
}


