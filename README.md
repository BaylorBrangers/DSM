# DSM Clustering Example

This repository demonstrates how to embed DSM diagnostic criteria using the Mental‑RoBERTa model and visualize the resulting embeddings with UMAP.

## Requirements

Install the Python dependencies:

```bash
pip install -r Backend/requirements.txt
```

## Usage

Place a CSV file containing DSM criteria in the following format:

| disorder_name | criteria_text |
|---------------|---------------|
| Example Disorder | List of symptom criteria ... |

Run the clustering script:

```bash
python Backend/cluster_dsm.py path/to/dsm5_criteria.csv --output plot.png
```

This will generate a scatter plot of the disorders in `plot.png`. If `--output` is omitted, the plot is displayed interactively.

The `--text-column` and `--label-column` options can be used if your CSV uses different column names.
