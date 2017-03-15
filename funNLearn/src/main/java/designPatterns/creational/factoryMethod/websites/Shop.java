package designPatterns.creational.factoryMethod.websites;

import designPatterns.creational.factoryMethod.pages.CartPage;
import designPatterns.creational.factoryMethod.pages.ItemPage;
import designPatterns.creational.factoryMethod.pages.SearchPage;

public class Shop extends Website {

	@Override
	public void createWebsite() {
		pages.add(new CartPage());
		pages.add(new ItemPage());
		pages.add(new SearchPage());
		
	}

}
