# CS4720
# Jonah Gallagher

# -----------------------------------------
# Compute Edit Distance using Bottom-Up DP
# Also returns the DP table for printing
# -----------------------------------------
def editDistance(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create DP table D[0..m][0..n]
    D = [[0] * (n + 1) for _ in range(m + 1)]

    # convert s1 prefix into empty string (delete all chars)
    for i in range(m + 1):
        D[i][0] = i

    # Base cases: convert empty string into s2 prefix (insert all chars)
    for j in range(n + 1):
        D[0][j] = j

    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # Cost 0 if chars match, else 1 for change operation
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            deleteCost = D[i - 1][j] + 1
            insertCost = D[i][j - 1] + 1
            changeCost = D[i - 1][j - 1] + cost

            D[i][j] = min(deleteCost, insertCost, changeCost)

    return D, D[m][n]


# -----------------------------------------
# Print DP Table
# -----------------------------------------
def printDPTable(s1, s2, D):
    m = len(s1)
    n = len(s2)

    # Header row
    header = "      "  # spacing for row labels
    header += "  ".join("∅ " + s for s in [""])[0:2]  # ignore, just structure
    header = "    | " + " | ".join(["∅"] + list(s2))
    print(header)
    print("-" * len(header))

    # Each DP row
    for i in range(m + 1):
        rowLabel = "∅" if i == 0 else s1[i - 1]
        row = f" {rowLabel}  | "
        row += " | ".join(f"{D[i][j]:2d}" for j in range(n + 1))
        print(row)
    print()


# -----------------------------------------
# Run one pair and print results
# -----------------------------------------
def runPair(s1, s2):
    print(f"\n=== Edit Distance: '{s1}' -> '{s2}' ===")
    D, dist = editDistance(s1, s2)
    printDPTable(s1, s2, D)
    print(f"Edit Distance = {dist}\n")


# -----------------------------------------
# Main
# -----------------------------------------
def main():

    # Required 5 pairs for the assignment
    testPairs = [
        ("sport", "sort"),
        ("sort", "short"),
        ("cat", "cut"),
        ("cat", "cats"),
        ("abc", "abc")
    ]

    # Run algorithm and print DP table for each
    for s1, s2 in testPairs:
        runPair(s1, s2)


if __name__ == "__main__":
    main()
