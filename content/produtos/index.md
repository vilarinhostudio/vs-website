---
title: Produtos
draft: true
---

```base
filters:
  and:
    - file.ext == "md"
    - file.inFolder("content/projetos")
    - file.name != "index"
views:
  - type: cards
    name: Image Cards
    order:
      - file.name
      - local
      - data
    image: note.cover

```
