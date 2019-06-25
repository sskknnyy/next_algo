#include <stdio.h>
#define N 110
int A[N][N][N], m, n, h;
int Q[N*N*N][4];
int B[6] = {0,0,0,0,-1,+1};
int C[6] = {-1,+1,0,0,0,0};
int D[6] = {0,0,-1,+1,0,0};

int check(int a, int b, int c) {
    if(a>0 && a<=h && b>0 && b<=n && c>0 && c<=m) {
        return 1;
    }
    else return 0;
}

void input() {
    int i, j, k;
    scanf("%d%d%d", &m, &n, &h);
    for (i=1; i<=h; i++) {
        for (j=1; j<=n; j++) {
            for (k=1; k<=m; k++) {
                scanf("%d", &A[i][j][k]);
            }
        }
    }
}


void run() {
    int i, j, k, q, temp, ch, rear, front;
    for (q=0; q<=5; q++) {
         temp = A[i+B[q]][j+C[q]][k+D[q]];
         ch = check(i+B[q], j+C[q], k+D[q]);
        if(temp == 0 && ch == 1) {
            rear++;
            Q[rear][0] = i + B[q];
            Q[rear][1] = j + C[q];
            Q[rear][2] = k + D[q];
            Q[rear][3] = Q[front][4] + 1;
            A[i+B[q]][j+C[q]][k+D[q]] = 1;
        }
    }

}


int main() {
    freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
    input();
    run();
}