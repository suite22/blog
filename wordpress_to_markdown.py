from typing import Optional
import xml.etree.ElementTree as ET
import os
import datetime
import re
import html


def clean_content(content: Optional[str]) -> str:
    """Clean the HTML content and convert to markdown-friendly format"""
    if content is None:
        return ""

    # Unescape HTML entities
    content = html.unescape(content)

    # Remove CDATA wrappers if present
    content = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", content, flags=re.DOTALL)

    # Basic HTML to Markdown conversions could be added here
    # This is a simple version - you might want to use a proper HTML->Markdown converter
    content = content.strip()

    return content


def escape_yaml_string(s: str) -> str:
    """Escape string for YAML frontmatter"""
    # If string contains any of these characters, wrap it in quotes
    special_chars = ":{}[]!@#$%^&*()=+<>?,'"
    needs_quotes = any(c in s for c in special_chars)

    # Replace double quotes with single quotes
    s = s.replace('"', "'")

    # If string needs quotes and isn't already quoted
    if needs_quotes and not (s.startswith('"') and s.endswith('"')):
        return f'"{s}"'
    return s


def create_markdown_file(post: ET.Element) -> None:
    """Create a markdown file from a WordPress post"""
    # Extract post data
    title = post.find("title").text or "Untitled"
    date_str = post.find(
        "wp:post_date", namespaces={"wp": "http://wordpress.org/export/1.2/"}
    ).text
    content = post.find("{http://purl.org/rss/1.0/modules/content/}encoded").text or ""
    status = post.find(
        "wp:status", namespaces={"wp": "http://wordpress.org/export/1.2/"}
    ).text
    post_type = post.find(
        "wp:post_type", namespaces={"wp": "http://wordpress.org/export/1.2/"}
    ).text

    # Skip if not a regular post or if draft
    if post_type != "post" or status != "publish":
        return

    # Clean the content
    content = clean_content(content)

    # Parse the date
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    # Create filename
    # Remove special characters and spaces from title
    safe_title = re.sub(r"[^\w\s-]", "", title.lower())
    safe_title = re.sub(r"[-\s]+", "-", safe_title)

    filename = f"{date.strftime('%Y-%m-%d')}-{safe_title}.md"

    # Create posts directory if it doesn't exist
    os.makedirs("_posts", exist_ok=True)

    # Create markdown file with YAML front matter
    with open(os.path.join("_posts", filename), "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("layout: post\n")
        f.write(f"title: {escape_yaml_string(title)}\n")
        f.write(f'date: {date.strftime("%Y-%m-%d %H:%M:%S")}\n')

        # Add categories if present
        categories = post.findall('category[@domain="category"]')
        if categories:
            f.write("categories:\n")
            for category in categories:
                category_text = category.text or ""
                f.write(f"  - {escape_yaml_string(category_text)}\n")

        f.write("---\n\n")
        f.write(content)


def main() -> None:
    # Parse the XML file
    tree = ET.parse("_drafts/bengoertz.wordpress.2012-09-12.xml")
    root = tree.getroot()

    # Find all posts in the XML
    channel = root.find("channel")
    items = channel.findall("item")

    # Process each post
    for item in items:
        create_markdown_file(item)


if __name__ == "__main__":
    main()
