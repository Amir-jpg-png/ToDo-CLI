---
title: "Colors"
description: "Adding colored output to our CLI using ANSI escape codes."
summary: "We added colored terminal output to make our CLI more user-friendly."
date: 2025-08-11T00:30:35+02:00
lastmod: 2025-08-11T00:30:35+02:00
draft: false
weight: 50
categories: ["Development"]
tags: ["CLI", "ANSI Colors", "Python"]
contributors: []
pinned: false
homepage: false
seo:
  title: "Colors in Our CLI"
  description: "We included functionality for colored terminal output in our CLI."
  canonical: ""
  noindex: false
---

## Colors in Our CLI

As mentioned in our earlier roadmap post, we’ve now added **colored terminal output** to the CLI tool.  
The main reason is to make important messages easier to see at a glance — errors in red, successes in green, warnings in yellow.

---

### ANSI Escape Codes

Our CLI uses [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) to change text color in the terminal.  
Here are some examples, but rendered in HTML so you can see the effect right here in the browser:

<pre style="background:black;color:white;padding:0.75em;">
<span style="color:red">This is red</span>
<span style="color:green">This is green</span>
<span style="color:orange">This is yellow</span>
</pre>

---

### What’s Happening Under the Hood

In the CLI, we output these colors using sequences like:

```text
\033[31mThis is red\033[0m
\033[32mThis is green\033[0m
\033[33mThis is yellow\033[0m
```
