# Game of Crowns 👑

**Game of Crowns** is an open‑source, fully test‑driven re‑implementation of LinkedIn’s daily logic puzzle Queens.The objective is to place crowns (👑) on an *n × n* grid so that every row, column and coloured region contains exactly one crown, while **no two crowns touch, even diagonally**. The project focuses on clean, idiomatic Python, algorithmic clarity, and expandable architecture.

## Table of Contents
1. [Features](#features)
2. [Rules Recap](#rules-recap)
3. [Quick Start](#quick-start)
4. [Project Structure](#project-structure)
5. [Testing](#testing)
6. [Roadmap](#roadmap)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgements](#acknowledgements)

## Features
- Emphasises a clean **object-oriented design**, using **immutability** where appropriate to enforce consistency and prevent unintended state mutation—even in adversarial or tampering scenarios. Fully playable **logic puzzle engine** based on the Queens puzzle mechanics.
- Fully playable **logic puzzle engine** based on the Queens puzzle mechanics.
- Implements **all core rule checks**, including adjacency and regional constraints.
- Includes a growing **test suite** to ensure correctness of validation logic.
- Clean and modular design, easy to extend with puzzle generation or UI components.

## Rules Recap
The implementation follows the standard rules of the *Queens* puzzle:

1. Each **row** and **column** must contain **exactly one** crown.

2. Each **coloured region** must also contain exactly one crown.

3. Crowns **may not touch** any other crown—horizontally, vertically or diagonally.

## Quick Start
### Prerequisites
- Python ≥ 3.10
### Running the Code
You can run the game logic or test it locally using Python:
```bash
git clone https://github.com/riccardocatervi/game-of-crowns.git
cd game-of-crowns
```
Open the source files in your preferred editor to explore or extend the implementation.

## Project Structure
<pre><code>
game-of-crowns
├── game_of_crowns
│   ├── __init__.py
│   ├── Board.py
│   ├── Cell.py
│   ├── CellState.py
│   ├── GameController.py
│   ├── GameState.py
│   ├── PuzzleIO.py
│   ├── Region.py
│   └── RegionID.py
│
├── tests
│   ├── __init__.py
│   ├── test_board.py
│   ├── test_cell.py
│   ├── test_game_controller.py
│   ├── test_puzzle_io.py
│   └── test_region.py
│ 
├── LICENSE
├── puzzle_sample.json
└── README.md
</code></pre>

- The `game_of_crowns/` directory contains the implementation of the puzzle's internal logic—effectively the "engine under the hood".
- The `tests/` directory holds the test cases validating that each module behaves correctly.
- `puzzle_sample.json` provides a static puzzle instance until the puzzle generator is developed.

## Testing
The entire test suite was **initially produced with the assistance of a Large Language Model** and subsequently r**eviewed and refined by the author** to ensure accuracy and idiomatic Python. Tests are run with **pytest** and can be executed using:
```bash
pytest -q
```

## Roadmap

| Milestone               | Status     | Notes                                                         |
|-------------------------|------------|---------------------------------------------------------------|
| Core logic ✓            | **Done**   | Validation of crowns placement according to puzzle rules      |
| Puzzle generator ⏳     | *Planned*  | Procedural generation of valid and uniquely solvable boards   |
| Graphical / web UI ⏳   | *Planned*  | Interactive interface for playing and testing puzzles         |
  
## Contributing

Pull requests are welcome! Please open an issue before starting substantial changes.

1. Fork the project and create your branch (`git checkout -b feature/idea`).
2. Ensure all tests pass (`pytest`).
3. Submit a pull request with a clear explanation of your changes.

## License
Distributed under the **MIT License**. See `LICENSE` for details.

This project is an **educational and non-commercial reimplementation** of the puzzle concept known as *Queens*, originally developed and published by the LinkedIn News Games team. All rights to the original game mechanics, visual design, and branding remain with **LinkedIn Corporation**.

This repository was created purely for the purpose of practicing Python programming, testing, and puzzle logic design, and is in no way affiliated with or endorsed by LinkedIn.

## Acknowledgements

- LinkedIn News Games team for the original Queens concept.
- OpenAI LLMs for assistance in test generation.
- *pytest* for simple and expressive testing tools.













