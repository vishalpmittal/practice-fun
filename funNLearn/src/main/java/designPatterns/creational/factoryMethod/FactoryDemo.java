package designPatterns.creational.factoryMethod;

import designPatterns.creational.factoryMethod.websites.Website;

public class FactoryDemo {
	
	public static void main(String args[]) {
		Website site = WebsiteFactory.getWebsite(WebsiteType.BLOG);
		System.out.println(site.getPages());
		
		site = WebsiteFactory.getWebsite(WebsiteType.SHOP);
		System.out.println(site.getPages());
	}
	
	
}
