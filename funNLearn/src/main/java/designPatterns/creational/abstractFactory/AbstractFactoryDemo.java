package designPatterns.creational.abstractFactory;

import designPatterns.creational.abstractFactory.creditCard.CardType;
import designPatterns.creational.abstractFactory.creditCard.CreditCard;
import designPatterns.creational.abstractFactory.factory.CreditCardFactory;

public class AbstractFactoryDemo {

	public static void main(String[] args) {
		
		CreditCardFactory abstractFactory = CreditCardFactory.getCreditCardFactory(775);
		
		CreditCard card = abstractFactory.getCreditCard(CardType.PLATINUM);
		
		System.out.println(card.getClass());
		
		abstractFactory = CreditCardFactory.getCreditCardFactory(600);
		
		CreditCard card2 = abstractFactory.getCreditCard(CardType.GOLD);
		
		System.out.println(card2.getClass());
	}

}
