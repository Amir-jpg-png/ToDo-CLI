---
title: "Version 1.3 - Release notes"
description: "Introducing version 1.3 of our Todo command line interface tool."
summary: "Use Typer instead of argvs + implemented uncheck option"
date: 2025-08-11T10:23:34+02:00
lastmod: 2025-08-11T10:23:34+02:00
draft: false
weight: 50
categories: []
tags: []
contributors: []
pinned: false
homepage: false
seo:
  title: "Todo CLI Version 1.3" # custom title (optional)
  description: "Introducing version 1.3 of our Todo command line interface tool." # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  noindex: false # false (default) or true
---

## Typer

Typer is a python library for building CLI tools it automatically does most of the checks, while also generating errors and responses to flags like the `--help` flag on its own.

This greatly increases the efficency and precision of our CLIs outputs such as error messages or help flag.

## Uncheck option

The uncheck option allows one to uncheck already completed tasks.

This is very helpful in cases like typos or when you have to revisit a specific task.
