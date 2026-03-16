# <ins>**Poker Advice Bot**</ins>
#### Video Demo:  <URL HERE>

#### Description:
This is a terminal-based Poker Texas Hold'em assistant built in Python. It calculates our equity i.e. the mathematical win probabilty against a specified number of opponents and compares it against our pot odds to provide real-time betting advice (CALL or FOLD) across all streets of the game(Preflop, Flop, Turn, and River).

It has a continuos game loop and also logs the history of every hand played, the advice given, and the final results into a readable text file for post-game analysis.

#### Features:
- **Monte Carlo Simulation:** Initialy I debated on calculating the probabilty of hands using mathematical formulas but upon further study I discovered a much more practical method, called the Monte Carlo simulation. Using the treys library we run a simulation of 1000 games given that we get the same hole cards every game. Based on this a win percentage is calculated. This is our equity.
- **Pot Odds Calculation:** The programme calculates the pot odds mathematically and then compares it with equity. This comparison is the heart of the programme and will determine what the appropriate advice is.
- **Continuous Game Loop:** The programme doesn't simply end after one round of game but instead remembers the game state. When one hand ends, the deck resets, the round increments, and a new hand begins without needing to restart the program.
- **Session Logging:** It also generates a readable .txt log file that tracks hole cards, community cards, player actions, pot sizes, and the final evaluated hand rank (e.g., "Flush", "Straight", etc).

#### Project Structure:
- `project.py`: The main application. It contains the game loop, user input validation, the simulator engine, the get_advice calculator, and the file I/O logging system.
- `test_project.py`: The pytest suite. It contains unit tests for the core logic functions, including string manipulation (card_to_str), mathematical evaluation (get_advice), and edge-case error handling (parser).
- `requirements.txt`: Lists the external dependencies required to run the program.
- `pokerlogs.txt`: Generated automatically after the first hand is played, storing the ongoing history of the user's sessions.

#### Design Choices:
- **The treys Library:** Evaluating a 7-card poker hand from scratch is computationally expensive and complex. I chose to use the external treys library because it uses integer representation for cards and bitwise operations, making it incredibly fast. This allowed me to run 1,000 simulations instantly on the Flop, Turn, and River without noticeable delay for the user.
- **The Game Loop Architecture:** Initially, the code for Preflop, Flop, Turn, and River was completely separate. I redesigned this into a "Game Loop" system. By defining the streets in a list of dictionaries ([{"street": "flop", "n": 3}, ...]), the program iterates through the phases, reusing the same simulator and advice functions. This drastically reduced code repetition and made the program easily scalable.
- **Plain Text Logging over CSV:** While I initially considered a CSV format for the logs, a standard spreadsheet format is difficult to read for a narrative game like poker. I opted for a custom plain-text formatting system. The program uses a global logs variable to store a readable summary of the hand phase-by-phase, and writes to the file once at the end of the round to optimize performance.

#### Usage
1. Install the required libraries by typing this line in your terminal pip install -r requirements.txt
2. To run the program type python project.py in the terminal
3. Enter your cards using standard notation (e.g., Ah, Kd for Ace of Hearts and King of Diamonds). Note that this uses 'T' for 10 and not '10', so a 10 of hearts would be '10h'
4. Follow the terminal prompts and receive impeccable advice at the end.
   
#### TODO
- [x] Build the core Monte Carlo simulator
- [x] Implement the continuous game loop
- [x] Add a game logging system
- [ ] Consider opponents raising
- [ ] Add advice for raises and specific bet sizing (3x raise)
- [ ] Implement implied odds
- [ ] Build a graphical user interface (GUI)
