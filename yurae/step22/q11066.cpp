#include <stdio.h>

void solve(){
	int dp[510][510] = {};
	int arr[510] = {};
	int n;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &arr[i]);
		if(i>0){
			arr[i] = arr[i] + arr[i-1];
		}
	}

	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			dp[i][j] = 1000000000;
		}
	}

	dp[0][0] = 0;
	for(int i=1; i<n; i++){
		dp[i][i] = 0;
		int low = 0;
		if(i>1) low = arr[i-2];
		dp[i-1][i] = arr[i] - low;
		dp[i][i-1] = arr[i] - low;
	}

	for(int i=n-1; i>=0; i--){
		for(int j=i+1; j<n; j++){
			for(int k=i; k<j; k++){
				int low = i>0? arr[i-1]:0;
				int curr = dp[i][k] + dp[k+1][j] + arr[j] - low;
				if(curr < dp[i][j]){
					dp[i][j] = curr;
				}
			}
		}
	}
	printf("%d\n", dp[0][n-1]);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i=0; i<t; i++){
		solve();
	}
}
