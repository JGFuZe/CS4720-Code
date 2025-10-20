# CS4720
# Jonah Gallagher

import random
import time
import os
import matplotlib.pyplot as plt

# -----------------------------------------
# Simple Item object for clarity
# -----------------------------------------
class Item:
    def __init__(self, index, value, weight):
        self.index = index      # Store index
        self.value = value      # Store value
        self.weight = weight    # Store weight


# -----------------------------------------
# Exact Recursive Knapsack
# Returns (chosenIndices, totalValue, totalWeight, stepCount)
# -----------------------------------------
def exactRec(i, currValue, currWeight, chosen, values, weights, capacity, n):
    # If overweight, this branch is infeasible → stop here
    if (currWeight > capacity):
        return ([], 0, 0, 1)

    # If we passed the last item, we have a complete subset, then return it
    if (i > n):
        return (chosen, currValue, currWeight, 1)

    # Choice 1: TAKE item i (build right branch)
    takeSet, takeV, takeW, stepsTake = exactRec(
        i + 1,
        currValue + values[i],
        currWeight + weights[i],
        chosen + [i],
        values, weights, capacity, n
    )

    # Choice 2: SKIP item i (build left branch)
    skipSet, skipV, skipW, stepsSkip = exactRec(
        i + 1,
        currValue,
        currWeight,
        chosen,
        values, weights, capacity, n
    )

    # Pick the better of the two by value
    if (takeV > skipV):
        return (takeSet, takeV, takeW, stepsTake + stepsSkip + 1)
    else:
        return (skipSet, skipV, skipW, stepsTake + stepsSkip + 1)


# Wrapper for the exact recursion (sets up arrays, calls exactRec)
def exactKnapsack(items, capacity):
    # Number of items
    n = len(items)

    # Build 1-based arrays for values and weights (nice with i..n)
    values = [0] + [it.value for it in items]
    weights = [0] + [it.weight for it in items]

    # Start recursion at item 1 with empty subset
    bestSet, bestV, bestW, steps = exactRec(1, 0, 0, [], values, weights, capacity, n)

    # Return tuple of results
    return (bestSet, bestV, bestW, steps)


# -----------------------------------------
# Greedy Knapsack (Highest Value First)
# Returns (chosenIndices, totalValue, totalWeight, stepCount)
# -----------------------------------------
def greedyKnapsack(items, capacity):
    # Sort items by value descending
    ordered = sorted(items, key=lambda it: it.value, reverse=True)

    # Init totals and tracking
    totalV = 0
    totalW = 0
    chosen = []
    steps = 0

    # Scan once through sorted list
    for it in ordered:
        # Count that we looked at an item
        steps += 1

        # If it fits, take it (update chosen, totals, steps)
        if (totalW + it.weight) <= capacity:
            chosen.append(it.index)
            totalW += it.weight
            totalV += it.value
            steps += 1

    # Return tuple of results
    return (chosen, totalV, totalW, steps)


# -----------------------------------------
# make random items for tests
# Values in [1,1000], Weights in [1,10000]
# -----------------------------------------
def makeRandomItems(n):
    # Build list of n items with random (value, weight)
    items = []
    for i in range(1, n + 1):
        v = random.randint(1, 1000)
        w = random.randint(1, 10000)
        items.append(Item(i, v, w))
    return items



# --------------- Scatterplot Functions (Save to file) ---------------

def saveTimePlot(xs, exactTimesMs, greedyTimesMs):
    os.makedirs("plots", exist_ok=True)  # make folder if needed
    plt.figure()
    plt.scatter(xs, exactTimesMs, label="Exact (ms)")
    plt.scatter(xs, greedyTimesMs, label="Greedy (ms)")
    plt.title("n vs Time")
    plt.xlabel("n")
    plt.ylabel("Time (milliseconds)")
    plt.grid(True)
    plt.legend()
    plt.savefig("plots/time_plot.png")
    plt.close()
    print("\nSaved: plots/time_plot.png")


def saveWeightPlot(xs, exactWeights, greedyWeights):
    os.makedirs("plots", exist_ok=True)
    plt.figure()
    plt.scatter(xs, exactWeights, label="Exact Weight")
    plt.scatter(xs, greedyWeights, label="Greedy Weight")
    plt.title("n vs Total Weight Selected")
    plt.xlabel("n")
    plt.ylabel("Total Weight")
    plt.grid(True)
    plt.legend()
    plt.savefig("plots/weight_plot.png")
    plt.close()
    print("Saved: plots/weight_plot.png")


def saveRatioPlot(xs, ratios):
    os.makedirs("plots", exist_ok=True)
    plt.figure()
    plt.scatter(xs, ratios, label="Exact / Greedy")
    plt.title("n vs Value Ratio")
    plt.xlabel("n")
    plt.ylabel("Exact/Greedy Ratio (>=1)")
    plt.grid(True)
    plt.legend()
    plt.savefig("plots/ratio_plot.png")
    plt.close()
    print("Saved: plots/ratio_plot.png")

# -----------------------------------------
# Main Function
# -----------------------------------------
def main():
    # Seed for repeatability in grading/testing
    random.seed(4720)

    # Print header
    print("Knapsack Experiments (W=10000)")
    columns = [
        ("n", 2, "{:>2d}"),
        ("trial", 5, "{:>5d}"),
        ("ExactTime(ms)", 12, "{:12.3f}"),
        ("GreedyTime(ms)", 13, "{:13.3f}"),
        ("ExactW", 6, "{:>6d}"),
        ("GreedyW", 7, "{:>7d}"),
        ("ExactV", 7, "{:>7d}"),
        ("GreedyV", 7, "{:>7d}"),
        ("Ratio(E/G)", 10, "{:10.3f}"),
    ]

    header = " | ".join(label.center(width) for label, width, _ in columns)
    separator = "-+-".join("-" * width for _, width, _ in columns)
    print(header)
    print(separator)

    xs = []                # n value per trial (for scatter plots)
    exactTimesMs = []      # exact solver time per trial in ms
    greedyTimesMs = []     # greedy solver time per trial in ms
    exactWeights = []      # exact solution weight per trial
    greedyWeights = []     # greedy solution weight per trial
    ratios = []            # exact / greedy value ratio per trial

    # Loop over n = 3..15
    for n in range(3, 16):

        # Do 5 random trials per n
        for trial in range(1, 6):

            # Generate random instance
            items = makeRandomItems(n)

            # Time the Exact solver
            startExact = time.perf_counter()
            Kx, Vx, Wx, Sx = exactKnapsack(items, 10000)
            exactTimeMs = (time.perf_counter() - startExact) * 1000.0

            # Time the Greedy solver
            startGreedy = time.perf_counter()
            Kg, Vg, Wg, Sg = greedyKnapsack(items, 10000)
            greedyTimeMs = (time.perf_counter() - startGreedy) * 1000.0

            # Compute value ratio (avoid div by zero)
            ratio = (Vx / Vg) if (Vg > 0) else float("inf")

            # Print per trial with formatting
            row_values = [n, trial, exactTimeMs, greedyTimeMs, Wx, Wg, Vx, Vg, ratio]
            row = " | ".join(fmt.format(val) for (_, _, fmt), val in zip(columns, row_values))
            print(row)

            # Accumulate data for plots
            xs.append(n)
            exactTimesMs.append(exactTimeMs)
            greedyTimesMs.append(greedyTimeMs)
            exactWeights.append(Wx)
            greedyWeights.append(Wg)
            ratios.append(ratio)

    # Save scatterplots as images
    saveTimePlot(xs, exactTimesMs, greedyTimesMs)
    saveWeightPlot(xs, exactWeights, greedyWeights)
    saveRatioPlot(xs, ratios)



# Standard entry point
if __name__ == "__main__":
    main()
