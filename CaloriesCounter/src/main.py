# ******************************************************************************
# * @file main.py
# * @author Pablo Joaquim
# * @brief The entry point
# *
# * @copyright NA
# *
# ******************************************************************************

# ******************************************************************************
# * import modules
# ******************************************************************************
import logging
import signal

# ******************************************************************************
# * Objects Declarations
# ******************************************************************************

# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************
running = True

class Food:
    def __init__(self, foodName, calories):
        self.foodName = "dummy"
        self.calories = calories

    def addCalories(self, calories):
        self.calories += calories

    def getCalories(self):
        return self.calories
    
    def setFoodName(self, name):
        self.foodName = name

    def getFoodName(self):
        return self.foodName
    
foods = []

# ******************************************************************************
# * Function Definitions
# ******************************************************************************

# ******************************************************************************
# * @brief The handler for the termination signal handler
# ******************************************************************************
def sigintHandler(signum, frame):
    global running
    running = False
    print('Signal handler called with signal', signum)
    raise RuntimeError("Terminating...")


# ******************************************************************************
# * @brief The main entry point
# ******************************************************************************
if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigintHandler)

    # These parameters are for the werkzeug embedded web server of Flask
    # If we're using gunicorn (WSGI production web server) these parameters are not applied
    try:
        foodsIdx = 0
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    # If the entry in the list is not available create a new one
                    if(len(foods) <= foodsIdx):
                        foods.append(Food("",0))
                    
                    # Check for the name of the food
                    if (line.startswith("#")):
                        foods[foodsIdx].setFoodName(line)
                    else:
                        # Obtain the calories string and convert it to integer
                        currCalories = int(line)
                        # Add the calories to the current calories counter
                        foods[foodsIdx].addCalories(currCalories)
                else:
                    # Increment the index
                    foodsIdx += 1

        foodWinnerCalories = 0
        foodWinnerName = ""
        
        for foodsIdx in range(len(foods)):
            if(foodWinnerCalories <= foods[foodsIdx].getCalories()):
                foodWinnerCalories = foods[foodsIdx].getCalories()
                foodWinnerName = foods[foodsIdx].getFoodName()
            print(foods[foodsIdx].getCalories(), flush=True)
            print(foods[foodsIdx].getFoodName(), flush=True)
            
        print("And the food with the higher calories is:" + foodWinnerName + " with " + str(foodWinnerCalories) + " calories", flush=True)

    except RuntimeError:
        print("Finishing...", flush=True)
