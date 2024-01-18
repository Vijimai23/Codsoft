import tkinter as tk
import random

# Create the root window
        
root = tk.Tk()
root.geometry("600x400")
root.title("Rock-Paper-Scissor")

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        #Initializing scores is  0

        self.user_score = 0
        self.computer_score = 0

        #creating  main_frame 

        self.main_frame = tk.Frame(root,bg='yellow',highlightbackground='black',highlightthickness=5,width=500,height=300)
        self.main_frame.place(x=10,y=10)
        
        #creating user,computer label and result label

        self.user_label = tk.Label(self.main_frame, text="Your Score: 0",bg='yellow',font=("bold", 16))
        self.user_label.place(x=10,y=10)

        self.computer_label = tk.Label(self.main_frame, text="Computer Score: 0",bg='yellow',font=("bold", 16))
        self.computer_label.place(x=290,y=10)

        self.result_label = tk.Label(self.main_frame, text="",font=("bold", 16),bg='yellow')
        self.result_label.place(x=65,y=130)
        
        #creating buttons

        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.place(x=170,y=70)
        
        self.play_again=tk.Button(self.main_frame,text='Play Again',font=('bold',18),width=10,bg='lime green',command=self.play_again)
        self.play_again.place(x=10,y=200)

        self.exit=tk.Button(self.main_frame,text='Exit',font=('bold',18),width=10,bg='red',command=exit)
        self.exit.place(x=330,y=200)

        #creating choices
         
        self.choices = ["Rock", "Paper", "Scissors"]

        for choice in self.choices:
            button = tk.Button(self.buttons_frame, text=choice, command=lambda c=choice: self.play(c))
            button.pack(side=tk.LEFT)   
    
    #defining functions
            
    def play(self, user_choice):
        computer_choice = random.choice(self.choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or (user_choice == "Paper" and computer_choice == "Rock")
            or (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.update_scores()
        self.result_label.config(text=f"Computer chose {computer_choice},{result}")
        self.play_again.config(state=tk.NORMAL)

    #defining function to update the scores
        
    def update_scores(self):
        self.user_label.config(text=f"Your Score: {self.user_score}")
        self.computer_label.config(text=f"Computer Score: {self.computer_score}")

    #defining function to display the result
        
    def display_result(self, result):
        self.result_label.config(text=result)

    #defining function to reset the game
        
    def play_again(self):
        self.user_score = 0
        self.computer_score  = 0
        self.update_scores()
        self.result_label.config(text="")

    #defining function to exit the game

    def exit():
        root.destroy()

# Create an instance of the game
        
game = RockPaperScissorsGame(root)

root.mainloop()