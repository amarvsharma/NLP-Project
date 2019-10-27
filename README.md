# NLP-Project
NLP Research Project with UCI Professor Ian Harris

*this is only a snippet of the code for demonstration purposes*

 - Utilized Google's Natural Language Processing (NLP) service, DialogFlow, to automate writing Python function declarations
 - Configured DialogFlow to detect Intents and Entities (aka keywords) in coding challenges (codingbat.com)
 - Integrated DialogFlow's API with Python code to create custom func. declarations based on API results

For example: if a given problem was:
 "Given a string and an int n, return a string made of the first and last n chars from the string."

My DialogFlow project would then detect 'a string' 'an int n' and 'return a string' as keywords.
From the attached Python script, I would call on the DialogFlow api to detect those keywords and I would then store them. After that I would a create a function declaration for this specific problem.

For example, the problem above would creates something similar to this declaration: 
def string1(s1: str, n: int) -> str:

