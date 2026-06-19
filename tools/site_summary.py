"""
Site Summary Tool - generates structured summaries for site entries.
"""

SITE_DATA = {
    "name": "Init Portal HTH",
    "url": "https://init-portal-hth.com",
    "keywords": ["hth", "portal", "init", "dashboard", "entry"],
    "tags": ["web", "portal", "tool", "hth"],
    "description": (
        "A centralized entry point providing quick access to core "
        "services and information. Designed for efficiency and ease of use."
    ),
    "language": "en",
    "category": "portal"
}

def format_keywords(keywords, max_len=40):
    """Format keywords list into a readable string, truncated if too long."""
    joined = ", ".join(keywords)
    if len(joined) > max_len:
        return joined[:max_len-3] + "..."
    return joined

def format_tags(tags):
    """Format tags as a comma-separated string."""
    return ", ".join(tags)

def build_summary(data):
    """Build a structured summary dictionary from site data."""
    return {
        "site_name": data["name"],
        "url": data["url"],
        "keywords": format_keywords(data["keywords"]),
        "tags": format_tags(data["tags"]),
        "description": data["description"],
        "language": data["language"],
        "category": data["category"]
    }

def print_summary(summary):
    """Print a formatted summary block."""
    print("=" * 50)
    print("SITE SUMMARY")
    print("=" * 50)
    print(f"Name:        {summary['site_name']}")
    print(f"URL:         {summary['url']}")
    print(f"Keywords:    {summary['keywords']}")
    print(f"Tags:        {summary['tags']}")
    print(f"Language:    {summary['language']}")
    print(f"Category:    {summary['category']}")
    print("-" * 50)
    print(f"Description: {summary['description']}")
    print("=" * 50)

def to_markdown(summary):
    """Convert summary to Markdown format string."""
    lines = [
        f"# {summary['site_name']}",
        "",
        f"**URL:** [{summary['url']}]({summary['url']})",
        "",
        f"**Keywords:** {summary['keywords']}",
        "",
        f"**Tags:** {summary['tags']}",
        "",
        f"**Language:** {summary['language']}  |  **Category:** {summary['category']}",
        "",
        "## Description",
        "",
        summary['description'],
        ""
    ]
    return "\n".join(lines)

def main():
    summary = build_summary(SITE_DATA)
    print_summary(summary)
    print("\n--- Markdown version ---\n")
    print(to_markdown(summary))

if __name__ == "__main__":
    main()