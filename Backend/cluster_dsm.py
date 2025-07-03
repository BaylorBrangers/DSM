import argparse
import pandas as pd
from sentence_transformers import SentenceTransformer
import umap
import matplotlib.pyplot as plt


def load_texts(csv_path: str, text_column: str = "criteria_text"):
    """Load the DSM criteria from a CSV file."""
    df = pd.read_csv(csv_path)
    if text_column not in df.columns:
        raise ValueError(f"Column '{text_column}' not found in {csv_path}")
    return df


def embed_texts(texts, model_name="mental-roberta-base"):
    """Embed texts using a SentenceTransformer model."""
    model = SentenceTransformer(model_name)
    return model.encode(texts, show_progress_bar=True)


def run_umap(embeddings, neighbors=10, min_dist=0.05):
    """Reduce embeddings to 2D using UMAP."""
    reducer = umap.UMAP(n_neighbors=neighbors, min_dist=min_dist, metric="cosine")
    return reducer.fit_transform(embeddings)


def plot_embeddings(coords, labels, out_path=None):
    """Plot the 2D coordinates with disorder labels."""
    plt.figure(figsize=(10, 8))
    plt.scatter(coords[:, 0], coords[:, 1], s=20)
    for i, label in enumerate(labels):
        plt.annotate(label, (coords[i, 0], coords[i, 1]), fontsize=8)
    plt.title("UMAP projection of DSM diagnostic descriptions")
    if out_path:
        plt.savefig(out_path, bbox_inches="tight")
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(description="Embed DSM text and plot UMAP clusters")
    parser.add_argument("csv", help="Path to CSV with DSM criteria")
    parser.add_argument("--text-column", default="criteria_text", help="Column containing criteria text")
    parser.add_argument("--label-column", default="disorder_name", help="Column for disorder labels")
    parser.add_argument("--model", default="mental-roberta-base", help="SentenceTransformer model")
    parser.add_argument("--output", help="Path to save plot (optional)")
    args = parser.parse_args()

    df = load_texts(args.csv, args.text_column)
    texts = df[args.text_column].tolist()
    labels = df[args.label_column].tolist() if args.label_column in df.columns else ["" for _ in texts]

    embeddings = embed_texts(texts, args.model)
    coords = run_umap(embeddings)
    plot_embeddings(coords, labels, args.output)


if __name__ == "__main__":
    main()
