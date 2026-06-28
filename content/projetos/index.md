---
title: Arquitetura
draft: false
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
    sort: []
    image: note.cover
  - type: board
    name: Por Local
    groupBy:
      property: local
      direction: ASC
    order:
      - file.name
      - data
      - local
    sort:
      - property: data
        direction: DESC
      - property: file.name
        direction: ASC

```
