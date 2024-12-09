## project structure
```txt
devautomation/
├── services/
│   ├── __init__.py
│   ├── config_loader.py
│   ├── git_manager.py
│   ├── build_manager.py
│   ├── test_manager.py
│   ├── mr_manager.py
├── main.py
├── config.json
├── requirements.txt
```
## create executable
`pyinstaller --onefile --name devautomation main.py`

`--onefile`: Combines all files into a single executable.

`--name`: Specifies the name of the executable.

`main.py`: The entry point for your application.

### add external file if needed, bundle it with `--add-data` flag   
`pyinstaller --onefile --add-data "path/to/config.json;." --name automation_project main.py`
- On Windows: Use `;` to separate paths.
- On Linux/macOS: Use `:` to separate paths.