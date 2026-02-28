import tkinter
import time
from tkinter import messagebox

canvasWidth = 750
canvasHeight = 500

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()

# Make bat and ball
bat = canvas.create_rectangle(300, 470, 450, 490, fill="dark turquoise")
ball = canvas.create_oval(350, 300, 370, 320, fill="deep pink")

windowOpen = True
score = 0

# Key controls
leftPressed = 0
rightPressed = 0
# on key press
def on_key_press(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1
# on key release
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
# move bat
def move_bat():
    move = batSpeed * rightPressed - batSpeed * leftPressed
    batLeft, batTop, batRight, batBottom = canvas.coords(bat)

    # Keep bat inside screen
    if batLeft + move >= 0 and batRight + move <= canvasWidth:
        canvas.move(bat, move, 0)

# Ball movement
ballMoveX = 4
ballMoveY = -4
# move ball
def move_ball():
    global ballMoveX, ballMoveY, score

    ballLeft, ballTop, ballRight, ballBottom = canvas.coords(ball)

    # Bounce off left/right walls
    if ballLeft <= 0 or ballRight >= canvasWidth:
        ballMoveX = -ballMoveX

    # Bounce off top
    if ballTop <= 0:
        ballMoveY = -ballMoveY

    # Paddle bounce
    if ballBottom >= 470:
        batLeft, batTop, batRight, batBottom = canvas.coords(bat)

        if ballRight > batLeft and ballLeft < batRight:
            ballMoveY = -ballMoveY

            score += 1
            # ncrease the speed a little each hit(go quicker)
            if ballMoveX > 0:
                ballMoveX += 0.3
            else:
                ballMoveX -= 0.3

            if ballMoveY > 0:
                ballMoveY += 0.3
            else:
                ballMoveY -= 0.3

    canvas.move(ball, ballMoveX, ballMoveY)
# check game over
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
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    canvas.coords(bat, 300, 470, 450, 490)
    canvas.coords(ball, 350, 300, 370, 320)
# close
def close():
    global windowOpen
    windowOpen = False
    window.destroy()

window.protocol("WM_DELETE_WINDOW", close)

# Main loop
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