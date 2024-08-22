# SubtitleConverter_PyQt
 Work in progress

### Requirements:
* [Python](http://www.python.org/)
* [PySide6](https://pypi.org/project/PySide6/)
* Libraries: [srt](https://github.com/cdown/srt)
## How To install on Windows and Linux:

* On Linux systems, open your favorite terminal or console.<br>
On Windows, after opening the Start menu, type  **cmd** or **Command Prompt** on your keyboard to find the terminal.
* In terminal type required **commands**, and after each command hit **Enter** taster
<br>&nbsp;
#### Create virtual environment on top of an existing Python installation:
```sh
python -m venv Python_projects
```
#### Activate virtual enviroment:
 (Linux)
```sh
source Python_projects/bin/activate
```
(Windows)
```sh
call Python_projects\Scripts\activate
```
#### Download source code using git:  
```sh
git clone https://github.com/padovaSR/SubtitleConverter_PyQt.git
```
Git software can be downloaded here: <https://git-scm.com/downloads>

#### Install requirements:

```sh
cd SubtitleConverter_PyQt
pip install -r requirements.txt
```
#### Rename or copy file **SubtitleConverter.py**:
```sh
cat SubtitleConverter.py > SubtitleConverter.pyw
```
#### Run the file:
```sh
python SubtitleConverter.pyw
```
**To deactivate virtual enviroment execute command:**
```sh
deactivate
``` 