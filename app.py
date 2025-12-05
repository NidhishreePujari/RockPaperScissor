import tkinter as tk
import random

choices = {
    "Rock": "👊 Rock",
    "Paper": "✋ Paper",
    "Scissors": "✌️ Scissors"
}

user_score = 0
comp_score = 0

win_msgs = ["🔥 You crushed it!", "💯 Victory!", "😎 Too easy!", "🚀 You win!"]
lose_msgs = ["😢 You lost!", "💀 Computer wins!", "🤖 Better luck next time!", "📉 Not your round!"]


# Game Logic
def play(user_choice):
    global user_score, comp_score

    computer_choice = random.choice(list(choices.keys()))

    user_label.config(text=f"You: {choices[user_choice]}")
    comp_label.config(text=f"Computer: {choices[computer_choice]}")

    # Determine winner
    if user_choice == computer_choice:
        result_label.config(text="⚖️ It's a Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        user_score += 1
        score_label.config(text=f"Score → You: {user_score} | Computer: {comp_score}")
        result_label.config(text=random.choice(win_msgs))
    else:
        comp_score += 1
        score_label.config(text=f"Score → You: {user_score} | Computer: {comp_score}")
        result_label.config(text=random.choice(lose_msgs))


# Reset Function
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_label.config(text="You:")
    comp_label.config(text="Computer:")
    result_label.config(text="Result:")
    score_label.config(text="Score → You: 0 | Computer: 0")


# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x420")
root.config(bg="#222222")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), fg="white", bg="#222222")
title.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0",font=("Arial", 14, "bold"), fg="#00FF9C", bg="#222222")
score_label.pack(pady=5)

user_label = tk.Label(root, text="You:", font=("Arial", 14), fg="white", bg="#222222")
user_label.pack()

comp_label = tk.Label(root, text="Computer:", font=("Arial", 14), fg="white", bg="#222222")
comp_label.pack()

result_label = tk.Label(root, text="Result:", font=("Arial", 16, "bold"), fg="#00FF9C", bg="#222222")
result_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#222222")
button_frame.pack(pady=20)

for i, choice in enumerate(choices.keys()):
    btn = tk.Button(button_frame, text=choices[choice], width=12, font=("Arial", 12),
                    bg="#333333", fg="white",
                    command=lambda c=choice: play(c))
    btn.grid(row=0, column=i, padx=10)

reset_btn = tk.Button(root, text="Reset Game", width=15, font=("Arial", 12, "bold"),
                      bg="#444444", fg="white", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
