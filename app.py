from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector # Import MySQL connector
import random # Import random module
import re # Import regular expressions
from random import randint # Import randint from random
from mysql.connector import Error # Import Error from mysql.connector

app = Flask(__name__) # Create Flask application instance

# Connect to MySQL database
mydb = mysql.connector.connect( 
  host="localhost",
  user="user",
  password="password",
  database="char"
)

 # Define chatbot responses
patterns_responses = {
    'hello': ["Chatbot: Hello, How can I assist you?", 'Chatbot: Hello, What is your Name?', "Chatbot: Hello, How are you?"],
    'name_reply': ["Chatbot: Nice to meet you, {0}!", "Chatbot: Hello, {0}!", "Chatbot: How can I assist you today, {0}?"],
    'how_are_you': ["Chatbot: I'm just a chatbot, but I'm here to help you! How can I assist you today?", "Chatbot: I'm here and ready to assist you!"],
    'help_query': ["Chatbot: I'm here to assist you. What do you need help with?", "Chatbot: I'm always here to help. How can I assist you today?"],
    'game': ["Chatbot: So, Let's play Hayang and Kulob Game! Type: <<< go >>>"],
    'go': ["Chatbot: Let's Go. \n Enter your Choice 'Hayang' or 'Kulob': "],
    #'palindrome': ["Chatbot: A palindrome is a word, sentence, verse, or even number that reads the same backward or forward."],
    'age': ["Chatbot: I'm ageless! But I was created recently. How old are you?", "Chatbot: I don't have an age, but I was programmed not too long ago. How about you?"],
    'where_from': ["Chatbot: I'm from the world of programming! Where are you from?", "Chatbot: I was created in the digital realm. How about you?"],
    'default': ["Chatbot: I'm not sure I understand. Can you ask me something else?", "Chatbot: I'm a bit confused. Could you rephrase that?"],
    'bye': ["Chatbot: Goodbye! Have a great day!"]
}

def create_file():
    with open("history.txt", 'w') as f:
        f.write('----------------------------------\n\n<<<< H I S T O R Y >>>>\n\n----------------------------------\n')
create_file()

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

#################################################################################################
#Game Logic Hayang and Kulob
@app.route('/hayang_kulob', methods=['POST', "GET"]) # Define route for the game
def hayang_kulob_game():

#     p1_choice = request.form.get('user-input') # Get player 1 choice
#          # Assign choice for the player 2
#     if (c2 == 1):
#         c2_choice = "Hayang"
#         print("CPlayer2: Hayang")   
#     else:
#         c2_choice = "Kulob"
#         print("CPlayer2: Kulob")

# # Assign choice for the player 3
#     if (c3 == 1):
#         c3_choice = "Hayang"
#         print("CPlayer3: Hayang")
#     else:
#         c3_choice = "Kulob"
#         print("CPlayer3: Kulob")

#  # To determine the winner of the game
#     if (p1_choice == "Hayang" and c2_choice == "Kulob" and c3_choice == "Kulob") or \
#        (p1_choice == "Kulob" and c2_choice == "Hayang" and c3_choice == "Hayang"):
#         result = "Chatbot: You Win!"

#     elif (p1_choice == "Kulob" and c2_choice == "Hayang" and c3_choice == "Kulob") or \
#          (p1_choice == "Hayang" and c2_choice == "Kulob" and c3_choice == "Hayang"):
#         result = "Chatbot: Computer Player 2 Wins!"

#     elif (p1_choice == "Kulob" and c2_choice == "Kulob" and c3_choice == "Hayang") or \
#          (p1_choice == "Hayang" and c2_choice == "Hayang" and c3_choice == "Kulob"):
#         result = "Chatbot: Computer Player 3 Wins!"

#     else:
#         result = "Chatbot: No Winners. Try again!"


#     if p1_choice is None:
#         return render_template('index.html', result="Invalid request. Please enter 'Hayang' or 'Kulob'.")
    

    c2 = random.randint(1, 2) # Random choice for player 2
    c3 = random.randint(1, 2) # Random choice for player 3

    p1_choice = input("Enter your Choice 'Hayang' or 'Kulob': ") # Get player 1 choice
    while p1_choice not in ['Hayang', 'Kulob']: # Validate choice of the player 1
        print("Invalid choice. Please enter 'Hayang' or 'Kulob'.")
        p1_choice = input("Enter your Choice 'Hayang' or 'Kulob': ")
    print(f"RPlayer 1: {p1_choice}")
    


    # while p1_choice not in ['Hayang', 'Kulob']: # Validate choice of the player 1
    #     return render_template('index.html', result="Invalid choice. Please enter 'Hayang' or 'Kulob'.")


 # Assign choice for the player 2
    if (c2 == 1):
        c2_choice = "Hayang"
        print("CPlayer2: Hayang")   
    else:
        c2_choice = "Kulob"
        print("CPlayer2: Kulob")

# Assign choice for the player 3
    if (c3 == 1):
        c3_choice = "Hayang"
        print("CPlayer3: Hayang")
    else:
        c3_choice = "Kulob"
        print("CPlayer3: Kulob")

 # To determine the winner of the game
    if (p1_choice == "Hayang" and c2_choice == "Kulob" and c3_choice == "Kulob") or \
       (p1_choice == "Kulob" and c2_choice == "Hayang" and c3_choice == "Hayang"):
        result = "Chatbot: You Win!"

    elif (p1_choice == "Kulob" and c2_choice == "Hayang" and c3_choice == "Kulob") or \
         (p1_choice == "Hayang" and c2_choice == "Kulob" and c3_choice == "Hayang"):
        result = "Chatbot: Computer Player 2 Wins!"

    elif (p1_choice == "Kulob" and c2_choice == "Kulob" and c3_choice == "Hayang") or \
         (p1_choice == "Hayang" and c2_choice == "Hayang" and c3_choice == "Kulob"):
        result = "Chatbot: Computer Player 3 Wins!"

    else:
        result = "Chatbot: No Winners. Try again!"

#############################################################################################################################

# Write game history to history.txt and can append if there is latest game
    with open('history.txt', 'a') as file:
        file.write(f"\nPlayer 1: | {p1_choice}\nPlayer 2: | {c2_choice}\nPlayer 3: | {c3_choice}\n>>> {result} <<<\n")
        
    return result

    #return render_template('index.html', result=result, p1_choice=p1_choice, c2_choice=c2_choice, c3_choice=c3_choice)

# Define the route to view history in the history.txt
def view_history():
    try:
        with open('history.txt', 'r') as file:
            history = file.read()
            return history
    except FileNotFoundError:
        return "No history found."

@app.route('/view_history', methods=['GET'])
def view_history_route():
    history = view_history()
    return history

# Define route for lotto page
@app.route("/lotto")
def lotto():
    return render_template("lotto.html")

@app.route("/savelot", methods=["GET", "POST"])
def savelot():
    if request.method == "POST":
        number1 = request.form.get('number1')

        iden = randint(0000000000, 1000000000) # Generate to create a random numbers for Identification Code

        cursor = mydb.cursor()
        sql = "INSERT INTO lotto (iden, taya) VALUES (%s, %s)"
        val = (iden, number1)
        cursor.execute(sql, val)
        mydb.commit()
        
        cursor.close()

        return render_template("lotto.html", message=f"Identification Code: {iden}")

    return render_template('lotto.html')

#generate of posible lotto result
def generate_lucky_numbers():
    numbers = random.randint(000, 999)
    return numbers

# Function to generate lotto possible results 
def result():
        cursor = mydb.cursor()

        result = generate_lucky_numbers() # Function to generate a random results

        sql1= "INSERT INTO results (resulta) VALUES (%s)"
        val= (result,)
        cursor.execute(sql1, val)
        mydb.commit()

        sql2 = "SELECT resulta FROM results ORDER BY id DESC LIMIT 1" # Fetch the inserted result
        cursor.execute(sql2)
        fetched_result = cursor.fetchone()[0]
        output = f"The possible winning result is: {fetched_result}"
        cursor.close()

        return output

### lucky number
# Define route for identifying the results of the lotto
@app.route("/iden", methods=["POST"])
def iden():
    user_input = request.form.get('userInput') # Get user input
    
    if user_input:
        cursor = mydb.cursor(dictionary=True) # Create cursor

# Query to SELECT the two table using (JOIN QUERY) and to know who is the winner
        cursor.execute("""
            SELECT lotto.Id AS lotto_id, lotto.iden, lotto.taya, results.resulta
            FROM lotto
            JOIN results ON lotto.taya = results.resulta
            WHERE lotto.iden = %s
        """, (user_input,))
        
        result = cursor.fetchone() # To Fetch the results
        
        if result:
            lotto_id = result['lotto_id']
            iden = result['iden']
            taya = result['taya']
            resulta = result['resulta']
            
            if taya == resulta:
                message = f"Identification Code: {iden}. Your bet: {taya}. Winning result: {resulta}. YOU WIN"
            else:
                message = f"Identification Code: {iden}. Your bet: {taya}. Winning result: {resulta}. YOU LOSE"
        else:
            message = "No Winning Result."
        
        cursor.close()
        return render_template("lotto.html", message=message) # Render template with message
    
    return render_template("lotto.html", message="Input Identification Code.") # # Prompt for input


############################################################################################################################
# Define route for chat functionality
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = match_pattern(user_input)
    return jsonify({'response': response})

# Function to preprocess user input
def preprocess_input(user_input):
    tokens = user_input.lower().split()
    filtered_tokens = [token.strip('.,!?') for token in tokens]
    return tokens, filtered_tokens

def match_pattern(user_input): # Function to match user input to patterns
    tokens, filtered_tokens = preprocess_input(user_input)

    if 'name' in filtered_tokens:
        match = re.search(r'my\s+name\s+is\s+(\w+)', user_input, re.IGNORECASE)
        if match:
            name = match.group(1)
            return f"Chatbot: Hello {name}!"
        else:
            return "I didn't catch your name."
    elif 'hello' in filtered_tokens:
        return random.choice(patterns_responses['hello'])
    elif 'how' in filtered_tokens and 'you' in filtered_tokens:
        return random.choice(patterns_responses['how_are_you'])
    elif 'help' in filtered_tokens or 'assist' in filtered_tokens:
        return random.choice(patterns_responses['help_query'])
    elif 'how' in filtered_tokens and 'old' in filtered_tokens:
        return random.choice(patterns_responses['age'])
    elif 'where' in filtered_tokens and 'from' in filtered_tokens:
        return random.choice(patterns_responses['where_from'])
    elif 'bye' in filtered_tokens:
        return random.choice(patterns_responses['bye'])
    elif 'play' in filtered_tokens and 'game' in filtered_tokens:
        #return "ok"
        # return redirect(url_for('hayang_kulob_game'))
        return random.choice(patterns_responses['game'])
    elif 'go' in filtered_tokens:
        #return "Enter your Choice 'Hayang' or 'Kulob': "
        return hayang_kulob_game()
    elif 'view' in filtered_tokens and 'history' in filtered_tokens:
        return view_history()
    # elif 'palindrome' in filtered_tokens:
    #     return random.choice(patterns_responses['palindrome'])
    elif 'give' in filtered_tokens and "numbers" in filtered_tokens:
        return result()
    
    # elif playgame == 'on' and 'kulob':
    #     return 'kulob ako'
    

    else:
        return random.choice(patterns_responses['default'])

if __name__ == "__main__":
    app.run(debug=True)