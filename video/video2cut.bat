ECHO ON
REM A batch script to execute a Python script
call "C:\Users\ABSBIN\Anaconda3\Scripts\activate.bat"
SET PATH=%PATH%; C:\Users\ABSBIN\Anaconda3
python cut_video_time_format_hms.py
PAUSE