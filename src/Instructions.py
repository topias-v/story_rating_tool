from psychopy import visual, event


def instructions(window, language):
    win = window
    
    # Instruction Screen
    # instruction_text --> English:0, Finnish:1
    instruction_text = [
        """
        You will be shown several short stories. After each story, you will rate it using two sliders:

        1. People vs. Scene:
           - Focus on how much the story emphasizes individuals, their actions or emotions (People) versus the environment, places, or surroundings (Scene).

        2. Self vs. Others:
           - Judge whether the story is primarily about the narrator’s own thoughts, feelings, or experiences (Self) or about other people (Others).

        Use your mouse to adjust the sliders, then press ENTER to continue.

        Press any key to begin.
        """,
        """
        Sinulle näytetään seuraavaksi lyhyitä tarinoita. Kunkin tarinan jälkeen arvioit sitä kahden liukusäätimen avulla:

        1. Ihmiset vs. Ympäristö:
            - Kuinka paljon tarina keskittyy ihmisiin, heidän tekoihinsa tai tunteisiinsa (Ihmiset) verrattuna ympäristöön, paikkoihin tai maisemiin (Ympäristö)?

        2. Minä vs. Muut:
            - Käsitteleekö tarina ensisijaisesti kertojan omia ajatuksia, tunteita tai kokemuksia (Minä) vai muita ihmisiä (Muut)?

        Säädä liukusäätimiä hiirellä ja paina ENTER jatkaaksesi.

        Paina mitä tahansa näppäintä aloittaaksesi.
        """
        ]

    intro = visual.TextStim(
        win=win,
        text=instruction_text[language],
        wrapWidth=1.2,
        height=0.03,
        color='white',
        pos=(0, 0)
    )

    intro.draw()
    win.flip()
    event.waitKeys()
