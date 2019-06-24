#include <stdio.h>
#define N 8

int n, A[N][N], L[N][N], S[N][N], R[N][N];

void input() {
    int i, j;
    scanf("%d",&n);
    for (i=1; i<=n; i++) {
        for (j=1; j<=n; j++) {
            scanf("%d", &A[i][j]);
        }
    }
}

void run() {
    int i, j, temp;
    for(i=1; i<=n; i++) {
        // L
        for (j=1; j<=n; j++) {
            temp = (L[i][j-1]>S[i-1][j]) ? L[i][j-1] : S[i-1][j];
            L[i][j] = temp + A[i][j];
        }
        // R
        for (j=n; j>=1; j--) {
            temp = (R[i][j+1]>S[i-1][j]) ? R[i][j+1] : S[i-1][j];
            R[i][j] = temp + A[i][j];
        }
        // S
        for (j=1; j<=n; j++) {
            S[i][j] = (L[i][j] > R[i][j]) ? L[i][j] : R[i][j];
        }
    }
}

void print() {
    int i, j;
    for (i=1; i<=n; i++) {
        for (j=1; j<=n; j++) {
            printf("%4d",S[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    printf("%d", S[n][n]);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    input();
    run();
    print();
    return 0;
}