import pandas as pd
import os

# Load TSV
publications = pd.read_csv("publications.tsv", sep="\t", header=0)

# Escape for YAML
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in text)

# Generate markdown
for row, item in publications.iterrows():

    # filename: YYYY-MM-DD-url_slug.md
    md_filename = f"{item.pub_date}-{item.url_slug}.md"
    html_filename = f"{item.pub_date}-{item.url_slug}"

    # YAML front matter
    md = f"""---
title: "{item.title}"
collection: publications
permalink: /publication/{html_filename}
date: {item.pub_date}
venue: '{html_escape(item.venue)}'
"""

    if len(str(item.paper_url)) > 5:
        md += f"paperurl: '{item.paper_url}'\n"

    md += "---\n\n"

    # Page content: currently empty
    md += ""  # you can add a summary here if you want

    # Write .md
    with open(f"../_publications/{md_filename}", "w") as f:
        f.write(md)
