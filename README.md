# RAGWorkshop
Basic RAG implementation with step by step instructions!

### Tech Prerequisites:
* Python
* VS Code (preferred)
* Git Bash (preferred)

### Other Prerequisites:
* Create account on: https://huggingface.co/
* Login at: https://huggingface.co/chat/


## RAG Overview 
First of all, lets discuss how RAG works.

“Retrieval Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response” -AWS

So what that really means is that instead of training or tuning your own LLM (which is very expensive and complicated) you can simply create a system that will send the pre-trained LLM your prompt + some relevant pieces of information so that it can have context specific to your domain.


-

# Setting Up Your Environment

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

## Test the complete application:

Now run:
```
python scripts/embedding/embedding_SOLUTION.py
```
You should see a file generate in the data outputs folder called "ftp_data.json"

To run the app, run:
```
chainlit run app/main_SOLUTION.py
```
To start your app!


