import tkinter
import time
from tkinter import messagebox

canvasWidth = 750
canvasHeight = 500

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()

# Score display
scoreText = canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 20), text="Score: 0")

# Make bat and ball
bat = canvas.create_rectangle(300, 470, 450, 490, fill="dark turquoise")
ball = canvas.create_oval(350, 300, 370, 320, fill="deep pink")

windowOpen = True
score = 0

# Key controls
leftPressed = 0
rightPressed = 0

def on_key_press(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1

def on_key_release(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0

window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)

# Bat movement
batSpeed = 25

def move_bat():
    move = batSpeed * rightPressed - batSpeed * leftPressed
    batLeft, batTop, batRight, batBottom = canvas.coords(bat)

    if batLeft + move >= 0 and batRight + move <= canvasWidth:
        canvas.move(bat, move, 0)

# Ball movement
ballMoveX = 4
ballMoveY = -4

def move_ball():
    global ballMoveX, ballMoveY, score

    ballLeft, ballTop, ballRight, ballBottom = canvas.coords(ball)

    if ballLeft <= 0 or ballRight >= canvasWidth:
        ballMoveX = -ballMoveX

    if ballTop <= 0:
        ballMoveY = -ballMoveY

    if ballBottom >= 470:
        batLeft, batTop, batRight, batBottom = canvas.coords(bat)

        if ballRight > batLeft and ballLeft < batRight:
            ballMoveY = -ballMoveY

            score += 1
            canvas.itemconfig(scoreText, text="Score: " + str(score))  # UPDATE SCORE

            if ballMoveX > 0:
                ballMoveX += 0.3
            else:
                ballMoveX -= 0.3

            if ballMoveY > 0:
                ballMoveY += 0.3
            else:
                ballMoveY -= 0.3

    canvas.move(ball, ballMoveX, ballMoveY)

def check_game_over():
    ballLeft, ballTop, ballRight, ballBottom = canvas.coords(ball)

    if ballTop > canvasHeight:
        print("Your score was", score)
        again = messagebox.askyesno(message="Play again?")
        if again:
            reset()
        else:
            close()

def reset():
    global score, ballMoveX, ballMoveY, leftPressed, rightPressed
    score = 0
    canvas.itemconfig(scoreText, text="Score: 0")  # RESET SCORE DISPLAY

    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4

    canvas.coords(bat, 300, 470, 450, 490)
    canvas.coords(ball, 350, 300, 370, 320)

def close():
    global windowOpen
    windowOpen = False
    window.destroy()

window.protocol("WM_DELETE_WINDOW", close)

def main_loop():
    while windowOpen:
        move_bat()
        move_ball()
        check_game_over()
        window.update()
        time.sleep(0.02)

reset()
main_loop()
#----------final version-----------
#----------do not delete!----------
#----------made by Marcus----------
