---
title: "Installation Guide"
description: "To start using the ToDo CLI you first need to install it."
summary: ""
date: 2023-09-07T16:04:48+02:00
lastmod: 2023-09-07T16:04:48+02:00
draft: false
weight: 810
toc: true
seo:
  title: "" # custom title (optional)
  description: "" # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  noindex: false # false (default) or true
---

To start using the ToDo CLI you first need to install it.

## Prerequisites

- **Git** must be installed.
- **Curl** or **wget** must be installed.
- You need **sudo** privileges to install to /usr/bin/local.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/Amir-jpg-png/ToDo-CLI/refs/heads/main/install.sh | bash
```

or

```bash
wget -qO- https://raw.githubusercontent.com/Amir-jpg-png/ToDo-CLI/refs/heads/main/install.sh | bash
```

## What this command does

The command downloads the `install.sh` script from the repository and runs it.
The script will:

1. Clone the ToDo CLI repository.
2. Make the `todo` script executable.
3. Move it to `/usr/local/bin` so it can be run from anywhere.

## Verify Installation

After Installation run

```bash
todo --help
```

You should see the CLI help text.
