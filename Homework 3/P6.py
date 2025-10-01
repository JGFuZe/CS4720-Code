# CS4720
# Jonah Gallagher

import random
import time

def maxHRDiffSlow(hrReadings):
    # Init vars
    maxDiff = 0

    # Get length of heart rate reading array
    readingCount = len(hrReadings)

    # For each reading
    for i in range(readingCount):

        baseValue = hrReadings[i]

        # For each reading after i'th element
        for j in range((i + 1), readingCount):
            comparisonValue = hrReadings[j]

            # Test Difference
            diff = abs(comparisonValue - baseValue)

            # If difference is larger
            if (diff > maxDiff):

                # Set max
                maxDiff = diff

    # Return max
    return maxDiff

def maxHRDiffFast(hrReadings):
    # Uses only minimum and maximum readings to compute the maximum difference
    minValue = min(hrReadings)
    maxValue = max(hrReadings)

    # Return the abs value of the difference
    return abs(maxValue - minValue)

def main():
    # Seed for reproducibility during testing
    random.seed(4720)

    # Generate simulated heart rate readings between 50 and 150
    hrReadings = []
    for _ in range(10000):
        hrReadings.append(random.randint(50, 150))

    # Slow algorithm timing
    startSlowTime = time.perf_counter()
    slowResult = maxHRDiffSlow(hrReadings)
    slowTime = (time.perf_counter() - startSlowTime)

    # Fast algorithm timing
    startFast = time.perf_counter()
    fastResult = maxHRDiffFast(hrReadings)
    fastTime = (time.perf_counter() - startFast)

    # Print Results
    print("Heart Rate Difference Results:")
    print(f"Slow Function Result:\t{slowResult}")
    print(f"Fast Function Result:\t{fastResult}")
    print(f"Slow Function Time:\t{(slowTime * 1000):.3f} ms")
    print(f"Fast Function Time:\t{(fastTime * 1000):.3f} ms")

    # Test if the result of both fast and slow fuctions produce the same result
    if (slowResult == fastResult):
        print("Validation:\t\tBoth functions returned the same value.")
    else:
        print("Validation:\t\tFunctions returned different values!")


if __name__ == "__main__":
    main()
