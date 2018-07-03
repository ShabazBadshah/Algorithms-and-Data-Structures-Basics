# Builder

The builder design pattern is a __creational__ design pattern. It helps with the creation of complex objects using setters to construct them *"piece by piece"* (similar to how we build legos in parts).

### Example

```
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
  
  public addCheese(Cheese cheese) { this.cheese = cheese; }
  public addDough(Dough dough) { this.dough = dough; }
  public addToppings(Toppings toppings) { this.toppings = toppings; }
  
  public buildPizza() {
    return new Pizza(this.cheese, this.dough, this.toppings);
  }
}
```

# Factory vs Builder
