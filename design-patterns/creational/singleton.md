# Singleton

The singleton design pattern is a __creational__ design pattern. It only allows *__one__* instance of an object to exist at any given time, hence the name **single**ton.

---

## Example

``` Java
class Singleton {

  // Variable below is static because we only want ONE instance of this object at any point
  private static Singleton instance;
  
  // Constructor is ALWAYS private for a singleton class
  private Singleton() {}

  public static Singleton getInstance() {
    if (instance == null) {
      instance = new Singleton();
    }
    return instance;
  }

  public void doSomething() {}
}
```

---

## Why you shouldn't use Singleton

Why would we have this design pattern if we say that it shouldn't be used? Here are some of the prominent reasons:

- Introduces *global* state (i.e. a change of a singleton class can cause changes in many other areas of your code that you are not aware of)
- Increases coupling/tighter coupling (other classes or the singleton can become highly dependent on each other)
  - We want to always reduce coupling and allow our code to be more modular
- Harder to test and debug

Singletons are not necessarily bad, but are hard to manage. Singletons are solely created for a single reason which is *you only want one instance of an object*. Ultimately, singletons should be used with extreme caution.