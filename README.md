## Project Title

Defeat the Evil Wizard — Python OOP Battle Game

---

## Author

**Magali Bogarin**

GitHub: https://github.com/mbogarin

---

## Project Description

This project is a turn-based command-line battle game built in Python using object-oriented programming (OOP) principles. The player creates a hero character and fights against an Evil Wizard using attacks, special abilities, healing mechanics, and strategic decision-making.

The goal of the project is to apply advanced OOP concepts such as inheritance, class interactions, and method overriding while building a fully functional interactive game loop.

### Why These Technologies?

Python was used because it allows clear implementation of OOP concepts and game logic in a simple and readable way. This made it ideal for practicing class design, inheritance, and real-time decision-based gameplay.

### Challenges Faced

- Designing multiple character classes with unique abilities
- Managing turn-based game flow and enemy AI behavior
- Handling multiple states (frozen, blocking, evading) correctly
- Balancing gameplay logic and randomness in attacks
- Keeping the code organized across many interacting classes

### Future Improvements

- Add multiplayer (player vs player mode)
- Add a leveling system and experience points
- Introduce inventory items and weapons
- Add graphical interface using Pygame or a web version
- Improve enemy AI with more complex behavior patterns

---

## Table of Contents

- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Game Features](#game-features)
- [Roadmap](#roadmap)
- [Collaborators](#collaborators)

---

## Installation & Setup

```bash
git clone https://github.com/mbogarin/defeat-evil-wizard-game.git
```

```bash
cd defeat-evil-wizard-game
python evil-wizard-game.py
```

---

## Usage

1. Choose your character class:
    - Warrior
    - Mage
    - Archer
    - Paladin

2. Enter your character name

3. Choose actions during battle:
    - Attack
    - Use special ability
    - Heal
    - View stats
4. Defeat the Evil Wizard before your health reaches zero

---

## Game Features

- Turn-based combat system
- Four playable character classes
- Two unique abilities per class
- Randomized attack damage system
- Healing system with max health cap
- Status effects (freeze, block, evade)
- Evil Wizard regeneration + counter-attacks
- Victory and defeat conditions

### How to Run the Game:

```bash
evil-wizard-game.py
```

### Character Classes:

Players can choose from four unique classes:

- Warrior – high melee damage with risk-based abilities

- Mage – powerful magic attacks and crowd control

- Archer – ranged damage with evasion mechanics

- Paladin – defensive tank with shields and healing abilities

### Combat System:

- Turn-based battle system

- Randomized attack damage

- Special abilities per character

- Healing mechanic with max health cap

### Defensive Mechanics:

- Evade (avoid next attack)

- Divine Shield (block next attack)

- Freeze (skip opponent turn)

All defensive states reset after use for balanced gameplay.

### Evil Wizard AI:

- Attacks after player actions

- Regenerates health each turn

- Can be frozen to skip a turn

### OOP Concepts Used:

- Inheritance (Character → Warrior/Mage/Archer/Paladin)

- Method overriding

- Encapsulation of combat logic

- Centralized damage handling (`take_damage()` system)

- State management (evade, block, freeze)

---

## Roadmap

- Add difficulty levels
- Expand character skill trees
- Add sound effects and animations
- Convert to GUI-based game
- Add story/campaign mode

---

## Collaborators

Currently this project was developed independently.
Future collaborators can be listed here:

### Credits

Classmates and mentors at Coding Temple
