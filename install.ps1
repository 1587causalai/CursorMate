# CursorFocus Installation Script
# Author: RenjiYuusei
# Description: This script installs CursorFocus in the Downloads folder

# Set error action preference
$ErrorActionPreference = "Stop"

# Define installation path
$installPath = "$env:USERPROFILE\Downloads\CursorFocus"

# Create function to show status messages
function Write-Status {
    param($Message)
    Write-Host "==> $Message" -ForegroundColor Cyan
}

# Check if Python is installed
Write-Status "Checking Python installation..."
try {
    python --version
} catch {
    Write-Host "Python is not installed. Please install Python 3.10 or later from https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
}

# Create installation directory if it doesn't exist
Write-Status "Creating installation directory..."
if (Test-Path $installPath) {
    Write-Host "Directory already exists. Cleaning up..." -ForegroundColor Yellow
    Remove-Item -Path $installPath -Recurse -Force
}
New-Item -ItemType Directory -Path $installPath | Out-Null

# Download and extract ZIP file
Write-Status "Downloading CursorFocus..."
$zipUrl = "https://github.com/RenjiYuusei/CursorFocus/archive/refs/heads/main.zip"
$zipPath = Join-Path $installPath "cursorfocus.zip"
Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath
Write-Host "Downloaded ZIP file" -ForegroundColor Green

Write-Status "Extracting files..."
Expand-Archive -Path $zipPath -DestinationPath $installPath
Move-Item -Path "$installPath\CursorFocus-main\*" -Destination $installPath
Remove-Item -Path "$installPath\CursorFocus-main" -Recurse
Remove-Item -Path $zipPath
Write-Host "Extracted files successfully" -ForegroundColor Green

# Get Gemini API key from user
Write-Status "Setting up Gemini API..."
Write-Host "Please enter your Gemini API key (get one from https://makersuite.google.com/app/apikey):" -ForegroundColor Yellow
$apiKey = Read-Host

# Create .env file with user's API key
Write-Status "Creating .env file..."
$envContent = @"
GEMINI_API_KEY=$apiKey
"@
Set-Content -Path (Join-Path $installPath ".env") -Value $envContent
Write-Host "Created .env file with your API key" -ForegroundColor Green

# Install required packages
Write-Status "Installing required packages..."
Set-Location $installPath
python -m pip install -r requirements.txt

Write-Status "Installation completed successfully!"
Write-Host @"

CursorFocus has been installed to: $installPath

To start using CursorFocus:
1. Navigate to the installation directory:
   cd "$installPath"

2. Run the setup script:
   python setup.py

For more information, please visit:
https://github.com/RenjiYuusei/CursorFocus
"@ -ForegroundColor Green

# Ask user if they want to open the installation folder
Write-Host "`nWould you like to open the CursorFocus folder? (Y/N)" -ForegroundColor Yellow
$openFolder = Read-Host
if ($openFolder -eq 'Y' -or $openFolder -eq 'y') {
    Start-Process explorer.exe -ArgumentList $installPath
} 