package designPatterns.creational.abstractFactory.validators;

import designPatterns.creational.abstractFactory.creditCard.CreditCard;

public class AmexGoldValidator implements Validator {

	@Override
	public boolean isValid(CreditCard creditCard) {
		
		return false;
	}

}
