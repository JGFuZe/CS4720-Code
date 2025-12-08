# CS4720
# Jonah Gallagher

# -----------------------------------------
# Coin-Row Dynamic Programming
# -----------------------------------------

def coinRowDP(values):
    """
    Solve the coin-row problem via bottom-up DP.

    Input:
        values: list of coin values (0-based indexing in Python list)

    Returns:
        (bestValue, chosenIndices, F)
        bestValue     = maximum total value achievable
        chosenIndices = list of chosen coin indices (1-based)
        F             = DP table where F[i] is best value using first i coins
    """
    n = len(values)

    # Build a 1-based version of values for easier DP (A[1..n])
    A = [0] + values

    # F[i] = best total value using the first i coins
    F = [0] * (n + 1)

    # choose[i] = True if coin i is taken in an optimal solution up to i
    choose = [False] * (n + 1)

    # Base cases
    if (n >= 1):
        F[1] = A[1]
        choose[1] = True

    # Bottom-up fill for i = 2..n
    for i in range(2, n + 1):
        # Option 1: skip coin i
        skipVal = F[i - 1]

        # Option 2: take coin i → cannot take i-1, so add F[i-2]
        takeVal = A[i] + F[i - 2]

        # Pick the better of the two
        if (takeVal > skipVal):
            F[i] = takeVal
            choose[i] = True
        else:
            F[i] = skipVal
            choose[i] = False

    # Reconstruct the chosen set of coins from choose[] and F[]
    chosenIndices = []
    i = n
    while (i >= 1):
        # If we decided to take coin i, it must match the DP relation
        if (choose[i] and (F[i] == A[i] + (F[i - 2] if i >= 2 else 0))):
            chosenIndices.append(i)
            i -= 2     # skip adjacent coin
        else:
            i -= 1     # move left without taking this coin

    chosenIndices.reverse()

    # Best value is F[n]
    bestValue = F[n]
    return (bestValue, chosenIndices, F)


# -----------------------------------------
# Main 
# -----------------------------------------

def main():
    # Given instance from Homework #7 Problem 1
    coins = [5, 1, 2, 10, 6]

    # Solve via DP
    bestValue, chosenIndices, F = coinRowDP(coins)

    # Print header
    print("Coin-Row Problem (Homework #7, Problem 1)")
    print("----------------------------------------")
    print("Coins (in a row):", coins)

    # Show DP table F[i]
    print("\nDP values F[i] = best value from first i coins:")
    for i in range(0, len(coins) + 1):
        print("F({}) = {}".format(i, F[i]))

    # Show chosen indices and values
    print("\nChosen coin indices (1-based):", chosenIndices)
    chosenValues = [coins[i - 1] for i in chosenIndices]
    print("Chosen coin values:", chosenValues)

    # Final maximum value
    print("\nMaximum total value =", bestValue)


if __name__ == "__main__":
    main()
