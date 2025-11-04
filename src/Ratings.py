from psychopy import visual, core, event
import pandas as pd
import os
import sys


def ratings(window, language, stories, file_path):
    win = window
    lang = language

    # Visual Elements
    box = visual.Rect(win=win, width=1, height=0.3, fillColor='white', lineColor='white', pos=(0, 0.25))
    story_text = visual.TextStim(win=win, text='', pos=(0, 0.25), height=0.03, wrapWidth=0.8, color='black')

    # Sliders
    slider1 = visual.Slider(
        win=win,
        ticks=(1, 2, 3, 4, 5),
        granularity=1,
        pos=(0, -0.05),
        size=(0.8, 0.05),
        style=['rating'],
        labelHeight=0,  # hide built-in labels
        color='black',
        fillColor='white',
        borderColor='black'
    )

    slider2 = visual.Slider(
        win=win,
        ticks=(1, 2, 3, 4, 5),
        granularity=1,
        pos=(0, -0.15),
        size=(0.8, 0.05),
        style=['rating'],
        labelHeight=0,
        color='black',
        fillColor='white',
        borderColor='black'
    )

    # Slider Labels
    label_people = visual.TextStim(win=win, text=['People', 'Ihmiset'][lang], pos=(-0.96, -0.05), height=0.03,
                                   color='black', anchorHoriz='left')
    label_scene = visual.TextStim(win=win, text=['Scene', 'Ympäristö'][lang], pos=([0.96, 0.98][lang], -0.05),
                                  height=0.03, color='black', anchorHoriz='right')

    label_self = visual.TextStim(win=win, text=['Self', 'Itse'][lang], pos=(-0.94, -0.15), height=0.03, color='black',
                                 anchorHoriz='left')
    label_others = visual.TextStim(win=win, text=['Others', 'Muut'][lang], pos=([0.96, 0.95][lang], -0.15), height=0.03,
                                   color='black', anchorHoriz='right')

    instr_txt = ["Use the sliders to rate the story. Then press ENTER.",
                 "Käytä liukusäätimiä arvioidaksesi tarinan, sitten paina ENTER"]

    instruction = visual.TextStim(
        win=win,
        text=instr_txt[lang],
        pos=(0, -0.3),
        height=0.03,
        color='black'
    )

    # Collect ratings
    responses = []
    for item in stories:
        slider1.reset()
        slider2.reset()
        story_text.text = item['story']

        while True:
            box.draw()
            story_text.draw()
            slider1.draw()
            slider2.draw()
            label_people.draw()
            label_scene.draw()
            label_self.draw()
            label_others.draw()
            instruction.draw()
            win.flip()

            keys = event.getKeys()

            if 'escape' in keys:
                win.close()
                core.quit()
                sys.exit(0)

            if 'return' in keys and slider1.getRating() is not None and slider2.getRating() is not None:
                break

        responses.append({
            'category': item['category'],
            'story': item['story'],
            'people_scene_rating': slider1.getRating(),
            'self_other_rating': slider2.getRating()
        })

    # Save or append results
    result_df = pd.DataFrame(responses)
    if os.path.exists(file_path):
        result_df.to_csv(file_path, mode='a', index=False, sep=';', header=False)
    else:
        result_df.to_csv(file_path, index=False, sep=';')
    print(f"Saved {len(responses)} responses to '{file_path}'")
