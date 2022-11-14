function solution(n, money) {
  let dp = Array.from(Array(money.length + 1), () => Array(n + 1).fill(0));
  money.map((coin, index) => {
    for (i = 1; i <= n; i++) {
      dp[index + 1][i] += dp[index][i];
      if (i === coin) {
        dp[index + 1][i] += 1;
      } else if (i > coin) {
        dp[index + 1][i] += dp[index + 1][i - coin];
      }
    }
  });
  return dp.at(-1).at(-1)
}

solution(5, [1, 2, 5]);
