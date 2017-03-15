package designPatterns.creational.abstractFactory.factory;

import designPatterns.creational.abstractFactory.creditCard.CardType;
import designPatterns.creational.abstractFactory.creditCard.CreditCard;
import designPatterns.creational.abstractFactory.validators.Validator;

//AbstractFactory
public abstract class CreditCardFactory {

	public static CreditCardFactory getCreditCardFactory(int creditScore) {
	
		if(creditScore > 650) {
			return new AmexFactory();
		}
		else {
			return new VisaFactory();
		}
	}
	
	public abstract CreditCard getCreditCard(CardType cardType);
		
	public abstract Validator getValidator(CardType cardType);
}
