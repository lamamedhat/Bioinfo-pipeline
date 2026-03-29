print("Python code pipeline") 

def check_quality(sequences, quality_scores, threshold=20):
    """
    Variant QC: uses minimum quality instead of average
    """

    high_quality_sequences = []

    for seq, qual in zip(sequences, quality_scores):
        min_quality = min(qual)
        if min_quality > threshold:
            high_quality_sequences.append(seq)
        else:
            print(f"Removed (low min quality): {seq} | Min score: {min_quality}")

    return high_quality_sequences



# EXAMPLE 
sequences = [
    "ATCGATCGATCG",
    "GGGGTTTTCCCC",
    "ATATATATATAT"
]

quality_scores = [
    [30, 32, 31, 29, 30, 31, 30, 32, 31, 30, 29, 30],  # High quality
    [10, 12, 15, 14, 13, 12, 11, 10, 12, 13, 11, 10],  # Low quality
    [25, 26, 24, 25, 26, 27, 25, 26, 24, 25, 26, 27]   # Good quality
]

filtered = check_quality(sequences, quality_scores)

print("\nHigh-quality sequences:")
for seq in filtered:
    print(seq)
