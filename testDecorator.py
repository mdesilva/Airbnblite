from SessionService import SessionService

SessionService = SessionService()

@SessionService.decorator
def betweenPrints(callerName):
    print("This is in between the print statements and was called by " + callerName)