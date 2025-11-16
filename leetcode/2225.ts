// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function findWinners(matches: number[][]): number[][] {
  const win: { [key: number]: number } = {} // Track how many times a player has won
  const loss: { [key: number]: number } = {} // Track how many times a player has lost

  for (let [winner, loser] of matches) {
    // Check if the player has won before
    if (win[winner]) {
      win[winner]++ // increment the win count
    } else {
      win[winner] = 1 // this is the first time the player has won so set to 1
    }

    // Check if the player has lost before
    if (loss[loser]) {
      loss[loser]++ // increment the loss count
    } else {
      loss[loser] = 1 // this is the first time the player has lost so set to 1
    }
  }

  // Filter out the players who have never lost (don't show up in the loss object)
  const playersWithNoLoss = Object.keys(win)
    .filter((player) => !loss[player])
    .map((player) => parseInt(player))

  // Filter out the players who have only lost once
  const playersWithOneLoss = Object.keys(loss)
    .filter((player) => loss[player] === 1)
    .map((player) => parseInt(player))

  return [playersWithNoLoss, playersWithOneLoss]
}
