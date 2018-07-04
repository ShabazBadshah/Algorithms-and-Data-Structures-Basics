# Builder

The builder design pattern is a __creational__ design pattern. It helps with the creation of complex objects using setters to construct them *"piece by piece"* (similar to how we build legos in parts).

### Example

``` Java
class Pizza {
  private Cheese cheese;
  private Dough dough;
  private Toppings toppings;
  
  Pizza(cheese, dough, toppings) {
    this.cheese = cheese;
    this.dough = dough;
    this.toppings = toppings;
  }
}

class PizzaBuilder() {
  private Cheese cheese;
  private Dough dough;
  private Toppings toppings;
  
  public addCheese(Cheese cheese) { 
    this.cheese = cheese;
    return this;
  }
  public addDough(Dough dough) { 
    this.dough = dough;
    return this;
  }
  public addToppings(Toppings toppings) { 
    this.toppings = toppings;
    return this;
  }
  
  public Pizza buildPizza() {
    return new Pizza(this.cheese, this.dough, this.toppings);
  }
}

class Main {
  public static void main(String[] args) {
    PizzaBuilder pizzaBuilder = new PizzaBuilder();
    Pizza pizza = pizzaBuilder
                    .addCheese(new Cheese('mozzarella'))
                    .addDough(new Dough('plain'))
                    .addToppings(new Toppings('olives'))
                    .buildPizza();
  }
}

```

# Factory vs Builder

|  Factory | Builder |
|  ------ | ------ |
|  creates entire object with a single call | creates object in pieces |
|  creates the same object every time | can create several variations of the object |
|  avoid construction pollution |  |