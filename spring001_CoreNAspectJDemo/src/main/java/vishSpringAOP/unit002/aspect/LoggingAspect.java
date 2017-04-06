package vishSpringAOP.unit002.aspect;

import org.aspectj.lang.ProceedingJoinPoint;

public class LoggingAspect {

    public Object myAroundAdvice(ProceedingJoinPoint pjp) {

        Object returnValue = null;
        try {
            System.out.println("Before Advice");
            returnValue = pjp.proceed();
            System.out.println("After Advice");
        } catch (Throwable e) {
            e.printStackTrace();
            System.out.println("After Throwing");
        }

        System.out.println("After Finally");
        return returnValue;
    }
}
