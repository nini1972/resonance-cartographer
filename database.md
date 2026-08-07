---
layout: default
title: The Database: A Topological Map
permalink: /database/
description: Mapping 2,772 equation entries across three levels of cosmic logic.
---

## The Database

## A Topological Map of Cosmic Logic

The foundation of The Resonance Cartographer is a structured dataset of 87 concept records containing 2,772 equation entries. Instead of treating the material as a linear reading list, the project maps it across three levels of physical description and looks for variables that persist between them.

## The Three Levels

The dataset mirrors a conceptual progression from fundamental ingredients to complex systems:

1. **Level 1: Fundamental physics.** Particles, thermodynamics, quantum fields, neutrinos, and dark matter.
2. **Level 2: Advanced frameworks.** Competing descriptions of spacetime and gravity, including non-commutative geometry and asymptotic safety.
3. **Level 3: Emergence and intelligence.** Self-organizing macro-structures, cosmic networks, and integrated information, $\Phi$.

The current map contains 46 Level 1 records, 26 Level 2 records, and 15 Level 3 records.

## The Topological Graph

The [`build_reverse_time.py`](https://github.com/nini1972/resonance-cartographer/blob/main/build_reverse_time.py) script builds a NetworkX graph from the equation data. Concepts become nodes; mathematical symbols extracted from each equation become connected symbol nodes.

The graph traces symbols that appear at every level. Concept nodes are colored by level: blue for Level 1, green for Level 2, and red for Level 3. Gold nodes mark the variables that persist through all three levels.

![Reverse-time graph of concepts and seed crystals](assets/images/reverse_time_graph.png)

*Figure: The reverse-time graph. Gold nodes are seed crystals; text labels are intentionally hidden in the generated visualization to keep the full network readable.*

## The 57 Seed Crystals

The graph filter identifies 57 seed crystals: symbols that appear in Levels 1, 2, and 3. The full reproducible list is stored in [`seed_crystals.json`](https://github.com/nini1972/resonance-cartographer/blob/main/seed_crystals.json).

Examples include:

- **$\Lambda$**: the cosmological constant.
- **$G_{\mu\nu}$ and $g_{\mu\nu}$**: geometric quantities from general relativity.
- **$\hbar$ and $k_B$**: bridges between quantum mechanics and thermodynamics.
- **$\Phi$**: a recurring scalar symbol whose physical meaning depends on the equation's context.

The recurrence of a symbol is a graph-theoretic observation, not evidence that every use has the same physical meaning. The purpose of the map is to identify promising connections for closer mathematical review.

## Data Provenance

The underlying records are available in [`equations.jsonl`](https://github.com/nini1972/resonance-cartographer/blob/main/equations.jsonl). Each JSONL record supplies a concept, level, and equation list. The graph and seed-crystal files can be regenerated locally by running:

```powershell
python build_reverse_time.py
```

[Back to the project home]({{ '/' | relative_url }})
