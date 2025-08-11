---
title: "Colors"
description: "Adding colored output to our CLI using ANSI escape codes."
summary: "Ad prommissed we added colored terminal output to make our CLI more user-friendly. A versioning system wasn't introduced yet but this can count as version 1.1"
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

---

### ANSI Escape Codes

Our CLI uses [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) to change text color in the terminal.  
Here are some examples.

<pre style="background:black;color:white;padding:0.75em;">
<span style="color:red">No tasks found yet!</span>
<span style="color:green">Task create api_controller was added!</span>
<span style="color:orange">Please enter a valid id!</span>
</pre>

---
