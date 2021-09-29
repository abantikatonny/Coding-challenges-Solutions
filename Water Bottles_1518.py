def water_bottle(numBottles, numExchange):

    # while numBottles>0:
        total = 0
        empty_bottle = 0

        while numBottles > 0:
            total += numBottles

            empty_bottle = numBottles + empty_bottle
            numBottles = empty_bottle // numExchange
            empty_bottle = empty_bottle % numExchange

        return total

print(water_bottle(5, 5))