def run(keyboard,layout,keycodes,mouse,time):

    keyboard.press(keycodes.GUI)
    keyboard.release_all()

    time.sleep(0.2)

    layout.write("term")
    
    keyboard.press(keycodes.ENTER)
    keyboard.release_all()

    time.sleep(0.2)

    layout.write("echo -hello from MalPico!- ")
    
    keyboard.press(keycodes.ENTER)
    keyboard.release_all()