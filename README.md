# RAGWorkshop
Basic RAG implementation with step by step instructions!

### Tech Prerequisites:
* Python
* VS Code (preferred)
* Git Bash (preferred)

### Other Prerequisites:
* Create account on: https://huggingface.co/
* Login at: https://huggingface.co/chat/
* Remember your username and password!!

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

Create a .env file in your working directory (RAGWorkshop) with the following content:
```
HUGGINGFACE_EMAIL="INSERT_EMAIL_HERE"
HUGGINGFACE_PASSWD="INSERT_PASSWORD_HERE"
```


## Test the complete application:

Now run:
```
python scripts/embedding/embedding_SOLUTION.py
```
You should see a file generate in the data outputs folder called "ftp_data_SOLUTION.json"

To run the app, run:
```
chainlit run app/main_SOLUTION.py
```
To start your app!



## RAG Overview 
First of all, lets discuss how RAG works.

“Retrieval Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response” -AWS

So what that really means is that instead of training or tuning your own LLM (which is very expensive and complicated) you can simply create a system that will send the pre-trained LLM your prompt + some relevant pieces of information so that it can have context specific to your domain.

You might know that the way LLMs process words and text (tokens technically) is through numerical representations of that text. 

![Words as numbers/embeddings](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*uTbwIj8HPBndJT3Ql9fIOA.png)

You can see here that these words are being represented as long lists of numbers. Well, those numbers actually bear significance. That list of numbers is called a vector, which is the same kind of vector we learn about in something like physics or calc. 3, however instead of being 1, 2, or 3 dimensional, these vectors are often hundreds of dimensions. 

Think of words as locations on a map. Instead of storing words as just text, we convert them into coordinates (vectors), which help us find similar words based on meaning.

Because we obviously can't visualize a vector in 300+ dimensions, below you can see a simplified 2D representation of how LLMs encode words into vectors based on semantic meaning. 

![Words as vectors](https://www.nlplanet.org/course-practical-nlp/_images/word_embeddings.png)

You can see that words that have similar meanings, result in similar vectors. How the vectors are decided/calculated and how the model decides what words should have similar vectors is outside the scope of this course but in short it relies on the training that the LLM went through reading countless large bodies of text and determining semantic relationships and patterns. 

It is important to note that the "word to vector" piece of LLMs is just a small component of the process and is basically its own model. For our purposes, we are going to be taking advantage of just this component called and Embedding Model.

A simplified LLM architecture diagram can be seen below:

![Simple LLM Architecture](https://www.deepchecks.com/wp-content/uploads/2023/12/transformer-architecture.jpg)

Zooming in on that embedding model component, we can see that the models sole purpose is to convert text into these vectors. You can see below that we could in theory compute these vectors on important text ahead of time and store them into what is essentially a coordinate plane as seen below:

![Embedding Model Diagram](https://miro.medium.com/v2/resize:fit:1400/1*-AL-kK8HzK5lw84xr1cSvw.png)

Now here's where everything ties together. 

If we were to precompute a bunch of information and store it into a database or coordinate plane then when we ask question about that data that an LLM would not otherwise be able to answer, we could then vectorize our user question, and check in our coordinate plane to see if there are any datapoints that are similar to the user's question vector. 

This kind of semantic retrieval is already quite useful as an alternative search algorithm, but in the context of domain specific LLMs we can make even more use of this by passing in our original question + some fetched pieces of information all into the LLM as input so that the LLM can then give you evidence backed responses.

A complete diagram of this process is show below:

![RAG Diagram](https://cdn.prod.website-files.com/651c34ac817aad4a2e62ec1b/655664de69b30a6d00f0960c_gaJkRvUmWHsWtnAGlNtjQJYhSzHvUwZHvV7nDU3kQJ6EyEI1C4v6HRysXIw28UlXK3QT4yU0rgTD7v1cUgbl5nB71emE5vqz9Y0VlvLjg10BgaLcOvI4Zauu9AKU6EKWN5rIwIKPs8CSYd0CiX2Gg5g.png)

The process of computing vectors for hand selected pieces of information ahead of time is far less computationally expensive and complex than training or tuning an entire model on specific data. As such, it is an approach that a lot of companies have been opting for recently in order to have chat bots which can answer specific questions about company data that are not widely publicized, internal, or confidential. 

