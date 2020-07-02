package dsAlgo.design_ds;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

enum Coin {

    CENT(1), NICKEL(5), DIME(10), QUARTER(25), HALF_DOLLAR(50);

    private final int centValue;

    Coin(int centValue) {
        this.centValue = centValue;
    }

    public int getLevelCode() {
        return this.centValue;
    }
}

class NotEnoughCoinException extends Exception {
    public NotEnoughCoinException(String errMsg) {
        super(errMsg);
    }
}

public class CoinPurse {
    private String cpName;
    private int total_value;
    private HashMap<Coin, Integer> coinCountMap;

    public CoinPurse(String name) {
        this.cpName = name;
        this.total_value = 0;
        this.coinCountMap = new HashMap<Coin, Integer>();
    }

    public String getName() {
        return this.cpName;
    }

    public int getTotalValue() {
        return this.total_value;
    }

    public void addCoin(Coin coin, Integer numOfCoins) {
        this.coinCountMap.compute(coin, (k, v) -> (v == null) ? numOfCoins : v + numOfCoins);

    }

    public void removeCoin(Coin coin, Integer numOfCoins) throws NotEnoughCoinException {
        if (this.coinCountMap.getOrDefault(coin, 0) < numOfCoins)
            throw new NotEnoughCoinException("Not enough coins for: " + coin);

    }

    public void coinConsolidate() {

    }

    public HashSet<Integer> getExactChangeOptions() {
        HashSet<Integer> exctChngOptions = new HashSet<Integer>();

        return exctChngOptions;
    }

    // Iterator

}