print("Python code pipeline")

# Quality control step
print("Start Running QC")

def check_quality(sequences, quality_scores, threshold=20):
    """
    Filters sequences using both average quality score
    and minimum quality score.
    """

    high_quality_sequences = []

    for seq, qual in zip(sequences, quality_scores):
        # Step 1: Calculate average quality score
        avg_quality = sum(qual) / len(qual)

        # Step 2: Calculate minimum quality score
        min_quality = min(qual)

        # Step 3: Keep sequence only if both checks pass
        if avg_quality >= threshold and min_quality > threshold:
            high_quality_sequences.append(seq)
        else:
            print(
                f"Removed: {seq} | Avg score: {avg_quality} | Min score: {min_quality}"
            )

    return high_quality_sequences


# Example data
sequences = [
    "ATCGATCGATCG",
    "GGGGTTTTCCCC",
    "ATATATATATAT"
]

quality_scores = [
    [30, 32, 31, 29, 30, 31, 30, 32, 31, 30, 29, 30],
    [10, 12, 15, 14, 13, 12, 11, 10, 12, 13, 11, 10],
    [25, 26, 24, 25, 26, 27, 25, 26, 24, 25, 26, 27]
]

# Run QC
filtered = check_quality(sequences, quality_scores)

print("\nHigh-quality sequences:")
for seq in filtered:
    print(seq)
