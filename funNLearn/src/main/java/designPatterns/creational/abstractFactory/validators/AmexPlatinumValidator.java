package designPatterns.creational.abstractFactory.validators;

import designPatterns.creational.abstractFactory.creditCard.CreditCard;

public class AmexPlatinumValidator implements Validator {

	@Override
	public boolean isValid(CreditCard creditCard) {
		
		return false;
	}

}
