# Simple bioinformatics pipeline example
print("Python code pipeline")

# Quality control section starts here
print("Start Running QC")

def check_quality(sequences, quality_scores, threshold=20):
    """
    Filters sequences using both average quality score
    and minimum quality score.
    """
    # Store sequences that pass quality control
    high_quality_sequences = []

    # Compare each sequence with its corresponding quality scores
    for seq, qual in zip(sequences, quality_scores):

        # Calculate average quality score for the full sequence
        avg_quality = sum(qual) / len(qual)

        # Calculate the lowest quality score in the sequence
        min_quality = min(qual)

        # Keep the sequence only if both QC conditions are satisfied
        if avg_quality >= threshold and min_quality > threshold:
            high_quality_sequences.append(seq)
        else:
            print(
                f"Removed: {seq} | Avg score: {avg_quality} | Min score: {min_quality}"
            )

    return high_quality_sequences


# Example DNA sequences used to test the QC function
sequences = [
    "ATCGATCGATCG",
    "GGGGTTTTCCCC",
    "ATATATATATAT"
]

# Example quality scores for each sequence
quality_scores = [
    [30, 32, 31, 29, 30, 31, 30, 32, 31, 30, 29, 30],
    [10, 12, 15, 14, 13, 12, 11, 10, 12, 13, 11, 10],
    [25, 26, 24, 25, 26, 27, 25, 26, 24, 25, 26, 27]
]

# Run the quality control function on the example data
filtered = check_quality(sequences, quality_scores)

# Print all sequences that passed the quality checks
print("\nHigh-quality sequences:")
for seq in filtered:
    print(seq)
