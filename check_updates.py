#!/usr/bin/python3

"""
Summary: Script for Check Switch Engine Updates-23.7.11.6v9 Workflow
Author: Bartosz Spiewak (github.com/bspiewa)
"""

from io import StringIO
from pathlib import Path

import pandas as pd
import requests

PAGE_URL = "https://supportdocs.extremenetworks.com/support/release-notes/product/switch-engine/"
RELEASES_FILENAME = "releases_log.txt"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    )
}

page = requests.get(PAGE_URL, headers=headers, timeout=5)
df = pd.read_html(StringIO(page.text))[0]
df["Last Update"] = pd.to_datetime(df["Last Update"], format="%b %Y")
df = df.rename(columns={"Document": "Software Version"})
df["Software Version"] = df["Software Version"].str.replace(" Release Notes", "")

latest_software = df[df["Last Update"] == df["Last Update"].max()]
latest_software = latest_software[["Software Version", "Last Update"]]
current_version = latest_software.to_string(index=False)

releases_file = Path(RELEASES_FILENAME)
releases_file.touch(exist_ok=True)
with open(releases_file, "r", encoding="utf-8") as f:
    last_check = f.read()
if last_check != current_version:
    with open(releases_file, "w", encoding="utf-8") as f:
        f.write(current_version)
        print(
            f"A new Switch Engine software was found:\n<br />{latest_software.to_html(index=False)}"
        )
else:
    print("No updates")
