# story_rating_tool
A PsychoPy based tool to rate stories in two dimensions, People vs. Scene &amp; Self vs. Other.

## Requirements
- Tested only on Windows.
- You need to install PsychoPy to run the code --> https://www.psychopy.org/download.html 
- To build the tool, pyinstaller needs to be installed.

## Running the Program
- You can run the executable in the dist folder without any installations. Note that launching it might take even 2-5min as PsychoPy is slow to start.
- Tool can be ran also by running Main.py.

### Data output
All ratings are automatically saved to C:\StoryRatings\ </br>
Unique csv file is created with timestamp, e.g.: </br>
story_focus_ratings_YYYYMMDD_HHMMSS

## Building the Executable
(Windows only) </br>
To build the tool, pyinstaller needs to be installed. </br>
1. Open a PowerShell inside the story_rating_tool/build/ folder.
2. Run: ./build.bat
3. Build takes some time, after ready new exe appear in: story_rating_tool/dist/StoryRatingTool.exe

## Author
Topias Vesanen </br>
Aalto University </br>



### References
Peirce, J. W., Gray, J. R., Simpson, S., MacAskill, M. R., Höchenberger, R., Sogo, H., Kastman, E., Lindeløv, J. (2019). 
PsychoPy2: experiments in behavior made easy. Behavior Research Methods. doi:10.3758/s13428-018-01193-y.</br>

Rinne, P., Lahnakoski, J. M., Saarimäki, H., Tavast, M., Sams, M., & Henriksson, L. (2024). 
Six types of loves differentially recruit reward and social cognition brain areas. Cerebral Cortex, 34(8), bhae331. 
https://doi.org/10.1093/cercor/bhae331 </br>

Rinne, P., Lahnakoski, J. M., Saarimäki, H., Tavast, M., Sams, M., & Henriksson, L. (2024). 
Supplementary material for: Six types of loves differentially recruit reward and social cognition brain areas. 
Cerebral Cortex. Available as “Supplementary data” on the article page. 
