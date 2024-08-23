@echo off
:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.x and try again.
    exit /b 1
)

:: Create a virtual environment
echo Creating virtual environment...
python -m venv env

:: Activate the virtual environment
echo Activating virtual environment...
call env\Scripts\activate

:: Install the required packages
echo Installing required packages...
pip install --upgrade pip
pip install -r requirements.txt

echo Setup complete. To activate the environment, run:
echo env\Scripts\activate

pause
