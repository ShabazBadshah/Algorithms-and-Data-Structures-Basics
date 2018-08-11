# Builder

The builder design pattern is a __creational__ design pattern. It helps with the creation of complex objects using setters to construct them *"piece by piece"* (similar to how we build legos in parts).

---

## Example

``` Java
public class Pizza {
  private final String cheese;
  private final String dough;
  private final String topping;

  private Pizza(PizzaBuilder builder) {
    this.cheese = builder.cheese;
    this.dough = builder.dough;
    this.topping = builder.topping;
  }
  
  public static class PizzaBuilder {  
    private final String cheese;
    private final String dough;
    private final String topping;

    public PizzaBuilder(String cheese) {
      this.cheese = cheese;
    }

    public PizzaBuilder addCheese(String cheese) {
      this.cheese = cheese;
      return this;
    }

    public PizzaBuilder addDough(String dough) {
      this.dough = dough;
      return this;
    }

    public PizzaBuilder addToppings(String topping) {
      this.topping = topping;
      return this;
    }

    public Pizza build() {
      return new Pizza(this);
    }
  }

}

public class Main {
  public static void main(String[] args) {
    Pizza p = Pizza.PizzaBuilder('cheese')
                .addDough('plain')
                .addToppings('olives')
                .build();
  }
}
```

## Factory vs Builder

|  Factory | Builder |
|  ------- | ------- |
|  creates entire object with a single call | creates object in pieces |
|  creates the same object every time | can create several variations of the object |
|  *avoid construction pollution* | *avoid construction pollution* |
