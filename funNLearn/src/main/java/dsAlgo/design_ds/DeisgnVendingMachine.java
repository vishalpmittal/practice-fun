/**
 * Tag: OOPS, class design
 * 
 * 
 * Design the main classes that sustain the implementation of the functionalities of a typical vending machine.
 * 
 * 
 */

 import java.util.*;

enum CCType {
    AMEX("amex"), DISCOVER("discover"), VISA("visa");
    private String value;

    CCType(String value){
        this.value = value;
    }
    
    public String getValue(){
        return this.value;
    }
}

enum Coin {
    NICKLE(5), DIME(10), QUARTER(25);
    private int value;
    Coin(int value){
        this.value = value;
    }
    
    public int getValue(){
        return this.value;
    }
}

enum Bill {
    ONE(1), TWO(2), TEN(10);

    private int value;

    Bill(int value){
        this.value = value;
    }
    
    public int getValue(){
        return this.value;
    }
}

interface Payment{
    boolean charge(int amount);
    public int cancelPurchase();
}

class CreditCard implements Payment{
    String ccName;
    String ccNum;
    int ccExpMonth;
    int ccExpYear;
    int ccCVV;
    CCType creditCardType;
    
    public boolean charge(int amount){
        return true;
    }
    
    public int cancelPurchase(){
        return 0;
    };
}

class CashPayment implements Payment{
    List<Integer> coins;
    List<Integer> bills;
    int total; 
    
    public boolean charge(int amount){
        // if (this.total < amount){
        //     return false;
        // }
        return true;
    }
    
    public void add_coin(int value){
        // add to coin list
        // increment total 
    }
    
    public void add_bill(int value){
        // add to bills list
        // increment total 
    }
    
    public int getCurrentValue(){
        // return total;
    }
    
    public int cancelPurchase(){
        // dispenses all coins 
        // dispenses all bills 
        // return total;
    }
}

class Item{
    String name;
    String description;
    Double price;
}

interface VendingMachineInterface {
    // supplier method
    void clearUp(int row, int col);
    void addItems(Item item, int row, int col, int amountOfItems, double pricePerItem);
    void updateMoney(List<Coin>, List<Bill>);
    void addMoney(List<Coin>, List<Bill>);
    void removeMoney(List<Coin>, List<Bill>);
    HashMap<Item, Integer> getInventory();   // { coke: 6, lays: 8 }
    HashMap<Bill, Integer> getBills();   // {1: 5, 2: 6, 10: 7 }
    HashMap<Bill, Integer> getCoin();    // {5: 2, 10: 6, 25: 7 }
    int getTotalMoneyInVM();     // calls getBills, getCoin, do a total, return 
    
    // user methods
    void selectItem();
    void displayTotalPrice();
    void acceptCoin();
    void acceptBills();
    void acceptCreditCard();
    void canelTransaction();
    void purchaseItem();
    void dispenseItem();
    void returnChange();
}

class SodaVendingMachine implements VendingMachineInterface{
    final int ROWS;
    final int COLUMNS;
    
    int [][] itemsType;     // [[coke, pepsi], [lays, kitkat]....]     
    int [][] itemsCount;     // [[4, 2], .....]
  
    // implement the interface methods

    // temperature
    void incrementTemperature(){}
}

class ChipsVendingMachine implements VendingMachineInterface{
    // implement the interface methods
}
    
class ElectronicsVendingMachine implements VendingMachineInterface{
    // implement the interface methods    
}
