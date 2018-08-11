# Strategy

The strategy design pattern is a __behavioural__ design pattern. This patterns allows you to change the class/algorithm used at runtime. You use a different *"strategy"* based on some condition.

## Example

``` Java
public interface EnemyStrategy {
  public void damagePlayer();
}

public class SimpleEnemyStrategy implements EnemyStrategy {
  public void damagePlayer() {
    System.out.println("Simple damage done!");
  }
}

public class AdvancedEnemyStrategy implements EnemyStrategy {
  public void damagePlayer() {
    System.out.println("Advanced damage done!");
  }
}

public class Enemy () {
  EnemyStrategy enemyStrategy;

  public Enemy(EnemyStrategy enemyStrategy) {
    this.enemyStrategy = enemyStrategy;
  }

  public void setNewEnemyStrategy(EnemyStrategy newEnemyStrategy) {
    this.enemyStrategy = newEnemyStrategy;
  }

  public void showDamage() {
    this.enemyStrategy.damagePlayer();
  }

}

public class Main {
  public static void main(String[] args) {

    SimpleEnemyStrategy simpleEnemy = new SimpleEnemyStrategy();
    AdvancedEnemyStrategy advancedEnemy = new AdvancedEnemyStrategy();
    Enemy enemy = new Enemy(simpleEnemy);
    enemy.showDamage() // Prints "Simple damage done!"
    enemy.setNewEnemyStrategy(advancedEnemy);
    enemy.showDamage() // Prints "Advanced damage done!"
  }
}

```