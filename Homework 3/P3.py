# CS4720
# Jonah Gallagher

def restrictedHanoi(disks, sourcePeg, middlePeg, destinationPeg, movesLog):
    # Stop recursion when there are no disks left to move
    if (disks == 0):
        return

    # Move the top (disks - 1) stack toward the destination through recursion
    restrictedHanoi((disks - 1), sourcePeg, middlePeg, destinationPeg, movesLog)

    # Record the move from the source peg onto the middle peg
    movesLog.append((sourcePeg, middlePeg))

    # Shift the smaller stack off the destination peg back toward the source
    restrictedHanoi((disks - 1), destinationPeg, middlePeg, sourcePeg, movesLog)

    # Record the move from the middle peg to the destination peg
    movesLog.append((middlePeg, destinationPeg))

    # Return the smaller stack onto the destination peg to rebuild the tower
    restrictedHanoi((disks - 1), sourcePeg, middlePeg, destinationPeg, movesLog)


def main():
    # Number of disks to solve with
    diskCount = 3

    # Holds the chronological list of moves
    movesLog = []

    # Run the recursive solver to populate the move log
    restrictedHanoi(diskCount, "A", "B", "C", movesLog)

    # Print the sequence of moves
    print("Restricted Tower of Hanoi Moves:")

    # Counter used when enumerating the moves
    moveNumber = 1

    # Iterate through each recorded move
    for move in movesLog:
        # Unpack the start and end pegs for the move
        startPeg, endPeg = move

        # Print the numbered move statement
        print(f"Move {moveNumber}: {startPeg} -> {endPeg}")

        # Increment the move counter
        moveNumber += 1

    # Count the recorded moves for validation
    totalMoves = len(movesLog)


    # Display the total number of moves executed
    print(f"\nTotal Moves Recorded:\t{totalMoves}")

if __name__ == "__main__":
    main()
