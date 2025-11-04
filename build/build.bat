@echo off
cd ..

echo Building Story Rating Tool executable
pyinstaller --onefile --noconsole ^
    --name "StoryRatingTool" ^
    --specpath build ^
    --add-data "%CD%\src;src" ^
    --hidden-import psychopy.visual.backends.pygletbackend ^
    --hidden-import psychopy.visual.window ^
    --hidden-import psychopy.visual.textstim ^
    --hidden-import psychopy.visual.rect ^
    --hidden-import psychopy.visual.slider ^
    --hidden-import psychopy.visual.shape ^
    --hidden-import psychopy.visual.line ^
    --hidden-import psychopy.event ^
    --hidden-import psychopy.core ^
    src\Main.py

echo Cleaning PyInstaller temporary files...
if exist "build\StoryRatingTool" rd /s /q "build\StoryRatingTool"
if exist "build\StoryRatingTool.spec" del /q "build\StoryRatingTool.spec"

echo ============================================
echo Build complete!
echo Executable created in: dist\StoryRatingTool.exe
echo ============================================
start dist
