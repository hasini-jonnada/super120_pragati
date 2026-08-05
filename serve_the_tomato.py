def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

def solve():
    N = int(input().strip())
    input().strip()  # 'shuffled'
    shuffled = [input().strip() for _ in range(N)]
    input().strip()  # 'original'
    original = [input().strip() for _ in range(N)]

    lcs_len = lcs(shuffled, original)
    print(N - lcs_len)

if __name__ == "__main__":
    solve()
