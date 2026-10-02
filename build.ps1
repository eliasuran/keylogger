uv run pyinstaller --onefile keylogger.py; Move-Item -Path dist\keylogger.exe -Destination .; Remove-Item -Recurse -Force dist, build, keylogger.spec
