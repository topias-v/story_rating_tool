from psychopy import visual, core
from Select_Stories import select_stories
from Select_Language import select_language
from Instructions import instructions
from Ratings import ratings
from Ask_Continue import ask_continue
from datetime import datetime
import os


def main():

    result_dir = "C:\\StoryRatings"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # Create unique file name for this session
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_file = os.path.join(result_dir, f"story_focus_ratings_{timestamp}.csv")
    
    # Pop up file explorer to select stories file
    stories = select_stories()

    # Create PsychoPy Window
    win = visual.Window(
        fullscr=False,
        color='darkgrey',
        units='height'
    )

    # Show Language Screen
    lang = select_language(win)

    # Show Instruction Screen
    instructions(win, lang)
    
    # Loop ratings until user quits or all stories rated
    while True:
        batch = []
        for category in list(stories.keys()):
            if stories[category]:
                story_text = stories[category].pop(0)
                batch.append({'category': category, 'story': story_text})
                
        if not batch:  # No more stories in any category
            break
        
        # Show Rating Screen
        ratings(win, lang, batch, save_file)
        
        if not any(stories[col] for col in stories):
            break
    
        if not ask_continue(win, lang):
            break

    # Show Ending Screen
    thanks = ["Thank you for your reviews!", "Kiitos arvioistasi!"]
    thank_you = visual.TextStim(
        win=win,
        text=thanks[lang],
        pos=(0, 0),
        height=0.05,
        color='white'
    )
    thank_you.draw()
    win.flip()
    core.wait(3)
    
    win.close()
    core.quit()
    

if __name__ == "__main__":
    main()
    