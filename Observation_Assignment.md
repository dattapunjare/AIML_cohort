
# 1.One Shot Promption

## 1.One Shot Promption
- One-shot prompting means giving the Model one example of the task, so it can understand the pattern and produce a similar answer.

Input :
''' Hello -> Bonjour
    Now translate : GoodBye '''

Output :
''' Goodbye → **Au revoir** 🇫🇷 '''

Observation : Only one example is given as demonstration at start of the chat. The model observes the given example, understands the pattern, and applies the same pattern to the new input.

## 2.Few Shot Promption
- Few-shot prompting means giving the model multiple examples of a task so that it can understand the pattern and apply it to a new input.
    
Input :
''' Hello-> Bonjour. Thanks-> Merci 
    Now translate: GoodBye '''

Output :
''' GoodBye → **Au revoir**'''

Observation :Provide multiple examples to the model. By observing these examples, the model understands the pattern better and applies it to the new input.

## 3.Zero-Shot Prompting
- Zero-shot prompting means giving the model a task without providing any examples. Gives only instruction or question . And only tell the model steps to achive answer.
    
Input :
''' if a train travels 60 km in 1.5 hours, what is its speed? '''

Output :
''' Speed = Distance ÷ Time
    60 ÷ 1.5 = 40
    Answer: 40 km/h 🚆'''

Observation : Zero-shot prompting does not provide any example to the AI. Its directly ask question to model. The model answer the question totally on the pre-trained learning knowledge 


## 4.Natural Language Query (Direct Answer)

Input :
''' what's the weatehr in nashik? '''

Output :
'''Right now in Nashik, it’s around 28°C with rain. 🌧️ The weather is breezy, with more showers possible this afternoon.'''

Observation : The model didn’t generate the weather details itself. insted it take from live weatehr api thats connect in background. 


## 5.Code Generation Request (Function Simulation)

Input :
''' write a python function get_wheather(city) and show how it would call it for nashik '''

Output :
'''Weather information for Nashik'''


## 6.Call the function for Pune

Input :
''' write a python function get_wheather(nashik) and show how it would call it for nashik '''

Output :
'''Getting weather for Nashik'''