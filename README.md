# Algo-Visualizer

> A real-time sorting-algorithm visualizer built with Python and pygame.

Algo-Visualizer renders an array of values as a bar chart and animates it being
sorted step by step. Bars are highlighted as they are compared and swapped, so
you can watch how each algorithm makes progress. Pick an algorithm from the menu
with a single key press and watch it run.

![demo](docs/demo.gif)

> No demo yet? The GIF above will appear once `docs/demo.gif` is added.
> See [`docs/README.md`](docs/README.md) for a one-minute guide to recording one.

## Implemented algorithms

| Key | Algorithm      |
| --- | -------------- |
| `1` | Bubble Sort    |
| `2` | Insertion Sort |
| `3` | Merge Sort     |
| `4` | Heap Sort      |
| `5` | Quick Sort     |
| `6` | Counting Sort  |
| `7` | Radix Sort     |

### Roadmap

- Bucket Sort (planned, not yet implemented)

## Getting started

### Prerequisites

- Python 3.8+
- A graphical display (pygame opens a window, so this won't run on a headless server)

### Installation

```bash
git clone https://github.com/AjaxAueleke/algo-visualizer.git
cd algo-visualizer
pip install -r requirements.txt
```

### Run it

```bash
python app.py
```

A window titled **"Algorithm Visualizer"** opens with the menu.

## Controls

| Input              | Action                                                      |
| ------------------ | ----------------------------------------------------------- |
| `1` – `7`          | Start the matching sort (see the table above)               |
| `Esc`              | Return to the menu (only while no sort is running)          |
| Resize the window  | The bars rescale to fit the new width                       |
| Close the window   | Quit the program                                            |

The data set is loaded from [`array.txt`](array.txt) (the first 100 of its 1,000
integers are visualized).

## Tech stack

- **Language:** Python 3
- **Graphics / event loop:** [pygame](https://www.pygame.org/) 2.1.2

## Project structure

```
algo-visualizer/
├── app.py            # Main visualizer — menu + the 7 sorts (entry point)
├── array.txt         # Data set of 1,000 integers (first 100 are visualized)
├── first_q.py        # Standalone quick-sort sandbox (SPACE to run, Esc to quit)
├── second_q.py       # Counting-sort + a range-query CLI utility
├── requirements.txt  # Python dependencies
├── docs/             # Documentation assets (demo GIF lives here)
└── LICENSE
```

## License

Released under the [MIT License](LICENSE).
