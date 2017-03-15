package designPatterns.creational.abstractFactory.factory;

import designPatterns.creational.abstractFactory.creditCard.AmexGoldCreditCard;
import designPatterns.creational.abstractFactory.creditCard.AmexPlatinumCreditCard;
import designPatterns.creational.abstractFactory.creditCard.CardType;
import designPatterns.creational.abstractFactory.creditCard.CreditCard;
import designPatterns.creational.abstractFactory.validators.AmexGoldValidator;
import designPatterns.creational.abstractFactory.validators.AmexPlatinumValidator;
import designPatterns.creational.abstractFactory.validators.Validator;

public class AmexFactory extends CreditCardFactory {

	@Override
	public CreditCard getCreditCard(CardType cardType) {
		
		switch (cardType) {
			case GOLD:
				return new AmexGoldCreditCard();
	
			case PLATINUM:
				return new AmexPlatinumCreditCard();	
				
			default:
				break;
		}
		
		return null;
	}

	@Override
	public Validator getValidator(CardType cardType) {
		
		switch (cardType) {
			case GOLD:
				
				return new AmexGoldValidator();
	
			case PLATINUM:
				
				return new AmexPlatinumValidator();	
		
		}
		
		return null;
	}
}
