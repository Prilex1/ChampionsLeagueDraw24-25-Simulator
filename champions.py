import random
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Define the pots with the teams
pot1 = ["Manchester City", "Bayern", "Real Madrid", "PSG", "Liverpool", "Inter", "B. Dortmund", "RB Leipzig", "Barcelona"]
pot2 = ["Bayer Leverkusen", "Atlético de Madrid", "Atalanta", "Juventus", "Benfica", "Arsenal", "Brujas", "Milan", "Shakhtar"]
pot3 = ["Feyenoord", "Sporting de Portugal", "PSV", "Celtic", "Salzburgo", "Young Boys", "Slavia Praga", "Dinamo Zagreb", "Estrella Roja"]
pot4 = ["Mónaco", "Aston Villa", "Bolonia", "Girona", "Stuttgart", "Sturm Graz", "Brest", "Sparta de Praga", "Ferencváros"]

# Map each team to its country
countries = {
    "Manchester City": "England", "Bayern": "Germany", "Real Madrid": "Spain", "PSG": "France", "Liverpool": "England",
    "Inter": "Italy", "B. Dortmund": "Germany", "RB Leipzig": "Germany", "Barcelona": "Spain",
    "Bayer Leverkusen": "Germany", "Atlético de Madrid": "Spain", "Atalanta": "Italy", "Juventus": "Italy",
    "Benfica": "Portugal", "Arsenal": "England", "Brujas": "Belgium", "Milan": "Italy", "Shakhtar": "Ukraine",
    "Feyenoord": "Netherlands", "Sporting de Portugal": "Portugal", "PSV": "Netherlands", "Celtic": "Scotland",
    "Salzburgo": "Austria", "Young Boys": "Switzerland", "Slavia Praga": "Czech Republic", "Dinamo Zagreb": "Croatia",
    "Estrella Roja": "Serbia",
    "Mónaco": "France", "Aston Villa": "England", "Bolonia": "Italy", "Girona": "Spain", "Stuttgart": "Germany",
    "Sturm Graz": "Austria", "Brest": "France", "Sparta de Praga": "Czech Republic", "Ferencváros": "Hungary"
}

# Define pots globally for accessibility in functions
pots = [pot1, pot2, pot3, pot4]

def can_add(team, rival, matches, countries):
    """Check if a rival can be added to a team's list of matches."""
    team_country = countries[team]
    rival_country = countries[rival]
    # Ensure no more than 2 matches against teams from the same country
    if sum(1 for r in matches[team] if countries[r] == team_country) >= 2:
        return False
    # Ensure no match against a team from the same country
    if team_country == rival_country:
        return False
    # Ensure the rival is not already in the list
    if rival in matches[team]:
        return False
    return True

def assign_rivals(team, matches, possible_rivals, countries):
    """Recursively assign rivals to a team."""
    random.shuffle(possible_rivals)
    for rival in possible_rivals:
        if can_add(team, rival, matches, countries):
            matches[team].append(rival)
            matches[rival].append(team)
            if len(matches[team]) == 8:
                return True
            if assign_rivals(team, matches, [r for r in possible_rivals if r != rival], countries):
                return True
            matches[team].remove(rival)
            matches[rival].remove(team)
    return False

def draw_matches(pots, countries):
    """Perform the draw for matches between teams."""
    teams = [team for pot in pots for team in pot]
    matches = {team: [] for team in teams}
    for i in range(8):  # Iterate over the 8 rounds needed for each team
        for pot in pots:
            for team in pot:
                if len(matches[team]) < 8:  # If the team doesn't have 8 rivals yet
                    possible_rivals = [r for p in pots for r in p if r != team and len(matches[r]) < 8]
                    if not assign_rivals(team, matches, possible_rivals, countries):
                        return {}
    return matches

def show_matches(team):
    """Display the matches for a specific team."""
    if team in matches:
        matches_text.delete(1.0, tk.END)
        matches_text.insert(tk.END, f"\nMatches for {team}:\n")
        for rival in matches[team]:
            home_away = random.choice(["vs", "@"])
            matches_text.insert(tk.END, f"{team} {home_away} {rival}\n")
    else:
        matches_text.delete(1.0, tk.END)
        matches_text.insert(tk.END, f"Team '{team}' not found.")

def retry_draw():
    """Retry the draw process until it is successful."""
    global matches
    global pots
    matches = draw_matches(pots, countries)
    while not matches:  # Retry until the draw is successful
        matches = draw_matches(pots, countries)
    update_buttons()
    messagebox.showinfo("Draw", "Draw completed successfully.")

def update_buttons():
    """Enable all team buttons after a successful draw."""
    for button in buttons.values():
        button.config(state=tk.NORMAL)

# Initialize the main window
root = tk.Tk()
root.title("Football Match Visualizer")

# Create the widgets
label = tk.Label(root, text="Select a team to view their matches:")
label.pack(padx=10, pady=5)

# Create a frame for the buttons in columns
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=5)

# Create frames for each column of buttons
frame_pot1 = tk.Frame(button_frame)
frame_pot1.pack(side=tk.LEFT, padx=10, pady=5)
frame_pot2 = tk.Frame(button_frame)
frame_pot2.pack(side=tk.LEFT, padx=10, pady=5)
frame_pot3 = tk.Frame(button_frame)
frame_pot3.pack(side=tk.LEFT, padx=10, pady=5)
frame_pot4 = tk.Frame(button_frame)
frame_pot4.pack(side=tk.LEFT, padx=10, pady=5)

# Create buttons for each team in their respective frame
buttons = {}
for team in pot1:
    button = tk.Button(frame_pot1, text=team, command=lambda t=team: show_matches(t))
    button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    buttons[team] = button

for team in pot2:
    button = tk.Button(frame_pot2, text=team, command=lambda t=team: show_matches(t))
    button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    buttons[team] = button

for team in pot3:
    button = tk.Button(frame_pot3, text=team, command=lambda t=team: show_matches(t))
    button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    buttons[team] = button

for team in pot4:
    button = tk.Button(frame_pot4, text=team, command=lambda t=team: show_matches(t))
    button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    buttons[team] = button

# Create a text area to display the matches
matches_text = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
matches_text.pack(padx=10, pady=10)

# Create menu with the option to retry the draw
menu = tk.Menu(root)
root.config(menu=menu)
options_menu = tk.Menu(menu)
menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Retry Draw", command=retry_draw)

# Perform the initial draw and update buttons
matches = draw_matches(pots, countries)
if not matches:
    messagebox.showerror("Error", "Initial draw failed. Retrying...")
    retry_draw()

# Start the main event loop
root.mainloop()
