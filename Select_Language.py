from psychopy import visual, core, event

def select_language(window):
    win = window
    lang_selected = None

    # Language selection prompt
    lang_prompt = visual.TextStim(
        win=win,
        text="Choose Language / Valitse kieli:",
        pos=(0, 0.3),
        height=0.05,
        color='white'
    )

    # English button
    eng_box = visual.Rect(win, width=0.4, height=0.15, pos=(-0.3, 0), fillColor='white')
    eng_text = visual.TextStim(win, text="English", pos=(-0.3, 0), color='black', height=0.04)

    # Finnish button
    fin_box = visual.Rect(win, width=0.4, height=0.15, pos=(0.3, 0), fillColor='white')
    fin_text = visual.TextStim(win, text="Suomi", pos=(0.3, 0), color='black', height=0.04)

    # Wait for user to click a language
    while lang_selected is None:
        lang_prompt.draw()
        eng_box.draw()
        eng_text.draw()
        fin_box.draw()
        fin_text.draw()
        win.flip()

        mouse = event.Mouse(win=win)
        if mouse.isPressedIn(eng_box):
            return 0
        elif mouse.isPressedIn(fin_box):
            return 1

        if 'escape' in event.getKeys():
            win.close()
            core.quit()
