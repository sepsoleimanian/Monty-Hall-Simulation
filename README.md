# Monty Hall Simulation 🎲🚪

## 📌 Description

This project implements the famous **Monty Hall problem**, providing both a **command-line simulation** and an optional **interactive Streamlit dashboard**.  
You can simulate numerous iterations of the game to observe win percentages when switching vs. not switching doors.

The Monty Hall problem is a classic probability puzzle named after *Monty Hall*, the host of the TV show *Let’s Make a Deal*.  

**How it works:**
1. A contestant chooses one of three doors.
2. Behind one door is a 🚗 car, behind the other two are 🐐 goats.
3. The host (who knows what’s behind each door) opens another door that has a goat.
4. The contestant can either **stick with the original choice** or **switch to the other unopened door**.
5. The puzzle: *Is it better to switch or stay?*

---

## 📂 Project Structure
```
.
├─ README.md
├─ requirements.txt
└─ src
   ├─ monty_hall.py
   └─ app.py
```
- `README.md`: This descriptive file
- `requirements.txt`: Contains all the required modules and libraries needed to run the project
- `src/monty_hall.py`: Contains the Python program to simulate the Monty Hall game
- `src/app.py`: The Streamlit application file to display an interactive dashboard

## ⚙️ Requirements

- Python **3.7+**
- [Streamlit](https://streamlit.io/) (only required for the dashboard)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

You can play the Monty Hall game simulation by adding the `src` directory to the PYTHONPATH and running:

`python3 src/monty_hall.py`

To start the Streamlit dashboard, run: 

`streamlit run src/app.py`

## Results

On running the Streamlit application, you will see an input field where you can specify the number of games to simulate. The app will then perform a simulation for each game, both where the contestant switches doors and where they don't. Lastly, the dashboard will display the win percentages dynamically as two separate line charts - showing how the likelihood of winning changes based on your decision to switch or not to switch doors.
