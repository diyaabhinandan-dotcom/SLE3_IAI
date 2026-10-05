# SLE-3: C4 Architecture Report — Weighted Path Search System
---

## 📌 Project Overview

This repository contains the **SLE-3 assignment** — a complete C4 architecture description of the **Weighted Path Search System** that was implemented and profiled in SLE-2.

The system finds the cheapest path from a start node to a goal node in a weighted directed graph using two search strategies:

- **Dijkstra's Algorithm** — uniform cost search (optimal)
- **Greedy Best-First Search** — heuristic search (fast but suboptimal)

---

## 🎯 What I Have Done

1. **Designed the system** — 8-node weighted graph with an admissible heuristic table.
2. **Implemented both algorithms** — `dijkstra_engine.py` and `greedy_engine.py`.
3. **Divided the system into 7 containers** — Input, Controller, Heuristic, Dijkstra Engine, Greedy Engine, Memory, Result.
4. **Drew 4 C4 diagrams** — Context, Container, Component, Code.
5. **Documented design decisions** — why Dijkstra and Greedy are separate containers.
6. **Generated the report** — `SLE3_25UAM015_Diya_Telnade.docx` / `.pdf`.
7. **Used PlantUML** — all diagrams are code-generated for version control.

---

## 📂 File Structure

| File | Purpose |
|------|---------|
| `common.py` | Shared graph, heuristic, START, GOAL |
| `input_module.py` | Level 2: Input Module |
| `search_controller.py` | Level 2: Search Controller |
| `heuristic_module.py` | Level 2: Heuristic Module |
| `dijkstra_engine.py` | Level 2/3/4: Dijkstra Engine |
| `greedy_engine.py` | Level 2/3/4: Greedy Engine |
| `memory.py` | Level 2: Visited / Cost Memory |
| `result_module.py` | Level 2: Result Module |
| `main.py` | Entry point — wires everything |
| `SLE3_25UAM015_Diya_Telnade.docx` | Report (Word) |
| `SLE3_25UAM015_Diya_Telnade.pdf` | Report (PDF) |
| `SLE3_Context.png` | Context diagram |
| `SLE3_Container.png` | Container diagram |
| `SLE3_Component.png` | Component diagram |
| `SLE3_Code.png` | Code-level diagram |

---