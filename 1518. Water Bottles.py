def sol(numBottles, numExchange):

    #if numBottles < numExchange:
    #    return numBottles

    #return numBottles - numBottles % numExchange + sol(int(numBottles / numExchange) + numBottles % numExchange, numExchange)

    return numBottles if numBottles < numExchange else numBottles - numBottles % numExchange + sol(int(numBottles / numExchange) + numBottles % numExchange, numExchange)


print(sol(9,3))