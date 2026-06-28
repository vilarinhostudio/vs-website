---
title: Arquitetura
draft: false
---

```base
filters:
  and:
    - file.ext == "md"
    - file.inFolder("projetos")
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
    sort:
      - property: data
        direction: DESC
      - property: file.name
        direction: ASC
  - type: table
    name: Por Local 2
    groupBy:
      property: local
      direction: ASC
    sort:
      - property: data
        direction: DESC
      - property: file.name
        direction: ASC

```
