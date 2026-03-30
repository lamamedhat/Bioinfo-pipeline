# Bioinformatics Pipeline

This project implements a simple bioinformatics pipeline for performing quality control on DNA sequences. The pipeline evaluates each sequence using both average and minimum quality scores, and filters out low-quality sequences.

The goal of this pipeline is to demonstrate basic quality control steps commonly used in bioinformatics workflows, ensuring that only reliable sequence data is retained for downstream analysis.


## Dependencies

- Python 3.x

## Installation

1. Install Python (version 3 or higher) from [python.org](https://www.python.org/)
2. Clone the repository:
```bash 
git clone https://github.com/lamamedhat/Bioinfo-pipeline.git
cd Bioinfo-pipeline
``` 

## Usage

```python
# Example input data
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

# Run quality control
filtered_sequences = check_quality(sequences, quality_scores)

print(filtered_sequences)

```

## Run

Run the pipeline from the command line:

```bash
python src/pipeline.py
```

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
