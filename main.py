import pandas as pd
import gradio as gr

# Read dataset
df = pd.read_csv("data.csv")

# Remove empty rows
df = df.dropna(subset=["title", "authors"])

# Search by author
def rag_chat(author_name):
    results = df[df["authors"].str.contains(author_name, case=False, na=False)]

    if results.empty:
     return "No books found."

    books = results["title"].tolist()

    return "Books:\n\n" + "\n".join(books)

# Gradio Interface
demo = gr.Interface(
fn=rag_chat,
inputs="text",
outputs="text",
title="Book Search System",
description="Enter an author's name to display their books."
)

demo.launch()