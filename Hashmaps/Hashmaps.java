// Import the HashMap class
import java.util.HashMap;
import java.util.HashSet;

public class Hashmaps {
  public static void main(String[] args) {
    // Create a HashMap object called capitalCities
    HashMap<String, String> capitalCities = new HashMap<String, String>();

    // Add keys and values (Country, City)
    capitalCities.put("England", "London");
    capitalCities.put("Germany", "Berlin");
    capitalCities.put("Norway", "Oslo");
    capitalCities.put("USA", "Washington DC");
    System.out.println(capitalCities);

    // Access an element
    System.out.println(capitalCities.get("England"));

    // Remove an element 
    capitalCities.remove("England");
    System.out.println(capitalCities);

    // To remove all the items
    // capitalCities.clear();

    // To get the size
    capitalCities.size();

    // Print keys
    for (String i : capitalCities.keySet()) {
        System.out.println(i);
    }

    // Print values
    for (String i : capitalCities.values()) {
        System.out.println(i);
    }

    // Print keys and values
    for (String i : capitalCities.keySet()) {
        System.out.println("key: " + i + " value: " + capitalCities.get(i));
    }

  // Below is for HashSets (that stores Strings, but can be changed to store integers)
  HashSet<String> cars = new HashSet<String>();
  cars.add("Lambo");
  cars.add("Ferarri");
  cars.add("McLaren");
  cars.add("Porsche");
  cars.add("McLaren");

  System.out.println(cars);
  // Note: even though McLaren is added twice, it only appears once in the set
  
  // contains() checks if an element exists in the set
  cars.contains("Lambo"); // Returns True
  
  cars.size() // Returns 4 -- because it contains 4 unique elements

  // Looping through set
  for (String i : cars){
    System.out.println(i);
  }

  cars.remove("Porsche");
  cars.clear(); // Removes all items from set
  }
}
