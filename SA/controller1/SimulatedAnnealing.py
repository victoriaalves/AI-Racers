import random
import math


decreaseRate = 0.1
parametersAmplitude = 100
numberOfParameters = 10
currentBestScore = 0.0

iterations = 10
energy = 0.0


def randomState():

    newState = random.sample(range(parametersAmplitude), numberOfParameters)
    
    return newState

def decreaseTemperature(temperature, byRate):

    return temperature - byRate

def randomNeighboor(currentNeighboor):

    newNeighboor = []
    perturbation = random.uniform(-0.9, 0.9)
    for element in currentNeighboor:
        
        newNeighboor.append(element + perturbation)

    return newNeighboor

def evaluate(solution, controller):

    score = controller.run_episode(solution)

    return score

def showTemperature(temperature):
    if temperature >= 7.5:
        print("  \n\033[1;4mTemperature:\033[0m", "\033[38;5;214m" , temperature, "\033[0m")
    elif temperature > 4 and temperature < 7.5:
        print("  \n\033[1;4mTemperature:\033[0m", "\033[93m" , temperature, "\033[0m")
    else: 
        print("  \n\033[1;4mTemperature:\033[0m", "\033[34m" , temperature, "\033[0m")

def run(controller, weights):

    #currentState = randomState()
    currentState = weights
    currentBestScore = controller.run_episode(currentState)
    betterSolutionWasFound = True

    temperature = 9

    while(True):
        temperature = decreaseTemperature(temperature, 0.1)
        showTemperature(temperature)
        if temperature <= 0.5:
            return currentState
        
        for _ in range(1, iterations):
            #print("Current state: ", currentState)
            candidate = randomNeighboor(currentState)
            #print("Candidate: ", candidate)
            candidateScore = evaluate(candidate, controller)
            energy = candidateScore - currentBestScore
            if betterSolutionWasFound == True:
                print("  \033[1;4mCurrent score:\033[0m ", "\033[92m", currentBestScore, "\033[0m")
                print("\033[1;4mCandidate score:\033[0m ", candidateScore)
                betterSolutionWasFound = False
            else:
                print("  \033[1;4mCurrent score:\033[0m ", currentBestScore)
                print("\033[1;4mCandidate score:\033[0m ", candidateScore)
            

            if energy > 0:
                print("         \033[1;4mEnergy:\033[0m", energy, "\033[1;42mFOUND BETTER SOLUTION\033[0m")
                betterSolutionWasFound = True
                currentState = candidate
                currentBestScore = candidateScore
            else:
                x = random.uniform(0.0,1.0)
                if x <= math.exp(energy/temperature):
                    print("         \033[1;4mEnergy:\033[0m", energy, "\033[1;41mCHOSE WORSE SOLUTION\033[0m")
                    #print("Random: ", x)
                    #print("Delta: ", math.exp(energy/temperature))
                    currentState = candidate
                    currentBestScore = candidateScore
    return currentState