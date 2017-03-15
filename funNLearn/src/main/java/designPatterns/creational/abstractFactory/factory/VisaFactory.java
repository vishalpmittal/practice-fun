package designPatterns.creational.abstractFactory.factory;

import designPatterns.creational.abstractFactory.creditCard.CardType;
import designPatterns.creational.abstractFactory.creditCard.CreditCard;
import designPatterns.creational.abstractFactory.creditCard.VisaBlackCreditCard;
import designPatterns.creational.abstractFactory.creditCard.VisaGoldCreditCard;
import designPatterns.creational.abstractFactory.validators.Validator;
import designPatterns.creational.abstractFactory.validators.VisaValidator;

public class VisaFactory extends CreditCardFactory {

	@Override
	public CreditCard getCreditCard(CardType cardType) {
		switch (cardType) {
			case GOLD:
				
				return new VisaGoldCreditCard();
	
			case PLATINUM:
				
				return new VisaBlackCreditCard();	
			
		}
		
		return null;
	}

	@Override
	public Validator getValidator(CardType cardType) {
		return new VisaValidator();
	}

}
