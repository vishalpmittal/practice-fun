package designPatterns.creational.abstractFactory.validators;

import designPatterns.creational.abstractFactory.creditCard.CreditCard;

public interface Validator {
	public boolean isValid(CreditCard creditCard);
}
