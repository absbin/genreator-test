ECHO ON
REM A batch script to execute a Python script
call "C:\Users\ABSBIN\Anaconda3\Scripts\activate.bat"
SET PATH=%PATH%; C:\Users\ABSBIN\Anaconda3
python mask_blured_wce.py
PAUSE