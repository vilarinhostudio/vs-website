---
title: Produtos
draft: true
comments: false
---

```base
filters:
  and:
    - file.ext == "md"
    - file.inFolder("produtos")
    - file.name != "index"
views:
  - type: cards
    name: Image Cards
    order:
      - title
    image: note.cover

```
