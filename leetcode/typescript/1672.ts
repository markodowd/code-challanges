const calculateCustomerWealth = (account: number[]): number =>
  account.reduce((sum, balance) => sum + balance, 0)

function maximumWealth(accounts: number[][]): number {
  return accounts.reduce((max, account) => {
    const wealth = calculateCustomerWealth(account)

    return Math.max(max, wealth)
  }, 0)
}
