import os
import re
import sys
from datetime import datetime as dt
from pathlib import Path
from typing import NoReturn

TEMPLATE: str = """
Title: {title}
Date: {year}-{month:02d}-{day:02d} {hour}:{minute:02d}
Category: 
Tags:
Description:
Status: Draft

<section markdown="1">
## Subtitle
</section>
"""


def generate_entry(title: str) -> NoReturn:
    """

    Args:
        title:

    Returns:

    """

    today: dt = dt.today()
    slug: str = re.sub("[^a-zA-Z0-9\-]", "", title.lower().strip().replace(" ", "-"))

    # Will attempt to make the year's directory. Does not throw an error if it exists.
    Path(f"content/{today.year}").mkdir(exist_ok=True)
    new_entry: str = f"content/{today.year}/{slug}.md"

    if Path(new_entry).exists():
        print(f"Error: entry [{Path(new_entry)}] already exists. Not overwriting!")
        return

    content: str = TEMPLATE.strip().format(
        title=title,
        year=today.year,
        month=today.month,
        day=today.day,
        hour=today.hour,
        minute=today.minute,
        slug=slug,
    )
    with open(new_entry, "w") as w:
        w.write(content)
    print(f"Article ready for editing: {Path(new_entry)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        generate_entry(sys.argv[1])
    else:
        print("Need an article title to generate a new entry. It's the only argument.")
