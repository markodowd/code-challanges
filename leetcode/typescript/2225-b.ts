function findWinners(matches: number[][]): number[][] {
  const win = new Map<number, number>() // Track how many times a player has won
  const loss = new Map<number, number>() // Track how many times a player has lost

  for (let [winner, loser] of matches) {
    // Check if the player has won before
    if (win.has(winner)) {
      win.set(winner, win.get(winner)! + 1) // increment the win count
    } else {
      win.set(winner, 1) // this is the first time the player has won so set to 1
    }

    // Check if the player has lost before
    if (loss.has(loser)) {
      loss.set(loser, loss.get(loser)! + 1) // increment the loss count
    } else {
      loss.set(loser, 1) // this is the first time the player has lost so set to 1
    }
  }

  // Filter out the players who have never lost (don't show up in the loss map)
  const playersWithNoLoss = Array.from(win.keys())
    .filter((player) => !loss.has(player))
    .sort((a, b) => a - b)

  // Filter out the players who have only lost once
  const playersWithOneLoss = Array.from(loss.keys())
    .filter((player) => loss.get(player) === 1)
    .sort((a, b) => a - b)

  return [playersWithNoLoss, playersWithOneLoss]
}
