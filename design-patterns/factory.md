# Factory Design Pattern

The factory design pattern is a pattern that helps with the *creation* of objects.
The crux of the factory pattern is that it will allow you to create an object without exposing the creation logic to the client. Essentially, instead of the programmer having to create the objects themselves, all that work is now delegated to the factory class that will create them for you.

Example:

    class CheesePizza():
        CheesePizza(...) {...}

    class PineapplePizza():
        PineapplePizza(...) {...}

    class PizzaFactory():

        '''
        The factory method can also take in the parameters that the objects require to 
        be created
        '''

        makePizza(typeOfPizza):
            if (typeOfPizza == "Cheese"):
                return new CheesePizza(...);
            elif (typeOfPizza == "Pineapple"):
                return new PineapplePizza(...); 
            else:
                return null
    }

    pf = new PizzaFactory()
    cheesePizza = pf.makePizza("Cheese")
