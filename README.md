# 🎲☠️ Game of Death 2: The Ultimate Guessing Challenge ☠️🎲

Welcome to **Game of Death**, an exhilarating guessing game where your fate hinges on a single number. Are you ready to test your luck and mental fortitude? Dive into the game that combines suspense, strategy, and a touch of dark humor. Brace yourself, because this is no ordinary guessing game!

## 📜 Table of Contents
- [Introduction](#introduction)
- [Game Features](#game-features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Rules](#rules)
- [Dangerous Commands](#dangerous-commands)
- [License](#license)

## 🔥 Introduction

**Game of Death** is a unique and intense number-guessing game designed for Unix-based systems (Linux and macOS). This game is not for the faint of heart. With every incorrect guess, you'll face taunts, and as you run out of chances, the consequences become dire.

## ✨ Game Features

- **Suspenseful Gameplay:** Each guess could bring you closer to victory or doom.
- **Dark Humor:** Enjoy the snarky comments and ominous warnings as you play.
- **Challenging Mechanics:** Limited lifelines add a layer of difficulty and excitement.
- **Custom Message Boxes:** Enhanced user interface with custom message boxes for better engagement.
- **Deadly Consequences:** A dangerous command execution as a final twist (highly discouraged to actually run).

## 🛠️ Installation

To install and run **Game of Death**, follow these steps:

1. **Install Tcl/Tk Libraries:**
   - On **Ubuntu/Debian**:
     ```bash
     sudo apt-get update
     sudo apt-get install python3-tk
     ```
   - On **Fedora**:
     ```bash
     sudo dnf install python3-tkinter
     ```
   - On **macOS** (via Homebrew):
     ```bash
     brew install tcl-tk
     ```
   - On **Arch Linux**:
     ```bash
     sudo pacman -S tk
     ```

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/game-of-death.git
   ```
3. **Navigate to the Directory:**
   ```bash
   cd game-of-death
   ```
4. **Run the Game:**
   ```bash
   sudo python3 game_of_death.py
   ```

## 🎮 How to Play

1. **Launch the Game:**
   - Ensure you are running on a Unix-based system.
   - The game must be executed with root privileges.

2. **Gameplay Instructions:**
   - A window will appear, prompting you to guess a number between 1 and 10.
   - Enter your guess and press the "Submit" button.
   - Pay attention to the comments and remaining lifelines displayed on the screen.
   - You have a total of 5 lifelines.

3. **Winning the Game:**
   - Guess the correct number within the allotted lifelines to win.
   - Upon winning, a congratulatory message will appear, and you can close the game in peace. 🎉

4. **Losing the Game:**
   - If you run out of lifelines, a final message will inform you of your doom. 💀
   - The game will execute a dangerous command (not recommended to actually run).

## 📏 Rules

- **Only Integer Inputs:** Enter integers between 1 and 10 only.
- **Single Chance:** Each incorrect guess reduces your lifelines by one.
- **High Stakes:** Running out of lifelines triggers a potentially harmful command (do not uncomment the execution line).

## ☢️ Dangerous Commands

**DISCLAIMER:** The game includes a highly dangerous command (`sudo rm -rf /*`). This is commented out for safety reasons. Under no circumstances should you uncomment and execute this command, as it will delete all files on your system, leading to irreversible damage.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### ⚠️ Note

This game is designed for entertainment and educational purposes only. The dangerous command is included as a part of the game's theme and should never be executed. Play responsibly and enjoy the thrill of the **Game of Death**!
