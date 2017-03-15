package designPatterns.creational.factoryMethod;

import designPatterns.creational.factoryMethod.websites.Blog;
import designPatterns.creational.factoryMethod.websites.Shop;
import designPatterns.creational.factoryMethod.websites.Website;

public class WebsiteFactory {
	
	public static Website getWebsite(WebsiteType siteType){
		switch (siteType) {
		case BLOG:
			return new Blog();
			
		case SHOP:
			return new Shop();
			
		default:
			return null;
		}
	}
}
