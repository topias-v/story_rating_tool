from psychopy import visual, event, core


def ask_continue(window, language):
    
    win = window
    
    prompt_txt = ["Do you want to review more stories?", "Haluatko arvioida lisää tarinoita?"]
    yes = ["Yes", "Kyllä"]
    no = ["No", "En"]
    
    prompt = visual.TextStim(win, text=prompt_txt[language], pos=(0, 0.3), height=0.05, color='white')
    yes_box = visual.Rect(win, width=0.4, height=0.15, pos=(-0.3, 0), fillColor='white')
    yes_label = visual.TextStim(win, text=yes[language], pos=(-0.3, 0), color='black', height=0.04)
    no_box = visual.Rect(win, width=0.4, height=0.15, pos=(0.3, 0), fillColor='white')
    no_label = visual.TextStim(win, text=no[language], pos=(0.3, 0), color='black', height=0.04)
    
    mouse = event.Mouse(win=win)
    while True:
        prompt.draw()
        yes_box.draw(), yes_label.draw()
        no_box.draw(), no_label.draw()
        win.flip()
        
        if mouse.isPressedIn(yes_box):
            return True
        elif mouse.isPressedIn(no_box):
            return False
            
        if 'escape' in event.getKeys():
            win.close()
            core.quit()
