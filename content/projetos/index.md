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
      - date
    sort: []
    image: note.image
    cardSize: 200
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
      - property: date
        direction: DESC
      - property: file.name
        direction: ASC

```
