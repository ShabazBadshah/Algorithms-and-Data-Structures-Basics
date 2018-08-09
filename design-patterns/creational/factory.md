# Factory Design Pattern

The factory design pattern is a pattern that helps with the *creation* of objects.
The crux of the factory pattern is that it will allow you to create an object without exposing the creation logic to the client. Essentially, instead of the programmer having to create the objects themselves, all that work is now delegated to the factory class that will create them for you; the programmer just specifies the type of object that they want, which is then returned. The object is created with a __single call__ to the factory method.

__*Note*:__ The classes being constructed by the Factory should always have a common superclass

---

## Example

``` Java

    public interface Pizza { ... }

    public class CheesePizza implements Pizza { ... }
    public class PineapplePizza implements Pizza { ... }

    public class PizzaFactory() {
        public Pizza makePizza(String typeOfPizza) {
            if (typeOfPizza == "Cheese") { return new CheesePizza(...); }
            if (typeOfPizza == "Pineapple") { return new PineapplePizza(...); }
            return null;
        }
    }

    PizzaFactory pf = new PizzaFactory();
    Pizza cheesePizza = pf.makePizza("Cheese");
```