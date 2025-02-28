# RAGWorkshop
Basic RAG implementation with step by step instructions!

### Tech Prerequisites:
* Python
* VS Code
* Bash

### Other Prerequisites:
* Create account on: https://huggingface.co/
* Login at: https://huggingface.co/chat/


Make sure you are in the appropriate directory:
ex: /c/Users/josep/Documents/RAGWorkshop

ex ls:
```
$ ls

__pycache__/  app/  chainlit.md  data/  README.md  requirements.txt  scripts/  test/
```

Create and activate virtual environment.
```
python -m venv .venv
source .venv/Scripts/activate 
#.venv/Scripts/activate for powershell or command prompt
#.venv/Scripts/activate.bat otherwise
```
You should see a little (.venv) tag in your terminal now.


Run the following for installation requirements
```
pip install -r requirements.txt
```

Now run:
```
chainlit run app/main_SOLUTION.py
```
To start your app!
