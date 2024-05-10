#evitar "numeros magicos"

LOW_RACE_VALUE = 6
MEDIUM_RACE_VALUE = 15
HIGH_RACE_VALUE = 20
VERY_HIGH_RACE_VALUE = 30

LOW_DISCOUNT = 0.90
MEDIUM_DISCOUNT = 0.85
HIGH_DISCOUNT = 0.80

MEDIUM_DEDUCTION = 3.10
HIGH_DEDUCTION = 6

def feeCharged(distance, time, valuePerKm, valuePerMinute):
    try:
        parameters = {
            "distance": distance,
            "time": time,
            "valuePerKm": valuePerKm,
            "valuePerMinute": valuePerMinute
        }

        for name, value in parameters.items():
            if type(value) not in [int, float]:
                raise ValueError(f"'{name}' precisar ser um número.")
            if value < 0:
                raise ValueError(f"'{name}' não pode ser negativo.")

        receValue = (distance * valuePerKm) + (time * valuePerMinute)

        finalValue = 0
        if receValue <= LOW_RACE_VALUE:
            finalValue = receValue * LOW_DISCOUNT
        elif LOW_RACE_VALUE < receValue <= MEDIUM_RACE_VALUE:
            finalValue = receValue * MEDIUM_DISCOUNT
        elif MEDIUM_RACE_VALUE < receValue <= HIGH_RACE_VALUE:
            finalValue = receValue - MEDIUM_DEDUCTION
        elif HIGH_RACE_VALUE < receValue <= VERY_HIGH_RACE_VALUE:
            finalValue = receValue * HIGH_DISCOUNT
        else:
            finalValue = receValue - HIGH_DEDUCTION

        return finalValue

    except ValueError as e:
        print(f"Erro: {e}")
        return -1
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return -1

def calcOfTotalTrips(distancesList, timeList, fixKmValue, fixMinuteValue):
    totalTrips = 0
    totalTax = 0

    if len(distancesList) != len(timeList):
        raise ValueError("A lista de KM e a lista de Tempo devem ter a mesma quantidade.")

    for currentTrip in range(len(timeList) - 1):
        currentKm = distancesList[currentTrip]
        currentTime = timeList[currentTrip]
        tax = feeCharged(currentKm, currentTime, fixKmValue, fixMinuteValue)

        if(tax > -1):
            totalTrips += 1
            totalTax += tax

    if(totalTrips > 0):
        return totalTax / totalTrips
    else:
        return 0


distancesList = [10, 20, 15, 0, 30]
timeList = [30, 40, 25, 0, 50]
valuePerKm = 0.5
valuePerMinute = 0.1

try:
    tax = calcOfTotalTrips(distancesList, timeList, valuePerKm, valuePerMinute)
    print("Taxa média das viagens:", tax)
except ValueError as e:
    print(f"Erro: {e}")
    




