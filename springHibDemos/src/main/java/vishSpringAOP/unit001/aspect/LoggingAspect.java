package vishSpringAOP.unit001.aspect;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.AfterThrowing;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;

@Aspect
public class LoggingAspect {

    /* execute this method BEFORE the getName from circle/triangle class
     * No matter which class object is created
     * This is because we did not define any class name in @Before below */
    @Before("execution(public String getName())")
    public void LoggingAdvice_g(JoinPoint joinPoint) {
        System.out.println("LoggingAdvice run. Get method called. : \n "
                + joinPoint.toString());

        System.out.println("the calling object is : " + joinPoint.getTarget());
    }

    /* This is going to run for getCircle, getTriangle and getName all three */

    /* @Before("execution(public * get*(..))")
     * .. Means 0 or n number of arguments for the method
     * "*" Means 1 or n number of arguments for the method */

    @Before("execution(public * get*())")
    public void LoggingAdvice_wild() {
        System.out.println("LoggingAdvice run. Wild Get method called.");
    }

    /* This before will be called only for getName method of Circle class */
    @Before("execution(public String vishSpringAOP.unit001.model.Circle.getName())")
    public void LoggingAdvice_c() {
        System.out.println("LoggingAdvice run. Circle Get method called.");
    }

    /* This before will be called only for getName method of Triangle class */
    @Before("execution(public String vishSpringAOP.unit001.model.Triangle.getName())")
    public void LoggingAdvice_t() {
        System.out.println("LoggingAdvice run. Triangle Get method called.");
    }

    /* @Before("execution(public String vishSpringAOP.unit001.model.*.get*())")
     * will be called for every get method in model package classes */

    /* dummy method
     * kind of super annotation for firstAdvice and secondAdvice */
    @Pointcut("execution(* get*())")
    public void allGettersDummy() {
    }

    @Before("allGettersDummy()")
    public void firstAdvice() {
        System.out.println("firstAdvice run. Get method called.");
    }

    @Before("allGettersDummy()")
    public void secondAdvice() {
        System.out.println("secondAdvice run. Triangle Get method called.");
    }

    /* Pointcut for all the Circle class method */
    @Pointcut("within(vishSpringAOP.unit001.model.Circle)")
    public void allCircleMethod() {

    }

    /* run for all the methods with circle object as an argument */
    @Pointcut("args(vishSpringAOP.unit001.model.Circle)")
    public void allMethodsWithCircleObjAsArgument() {

    }

    /* @Before("pointcut1() && pointcut2()")
     * run for both the pointcut conditions */

    /* @After
     * same as Before but runs after the specified methods.
     * This runs no matter whether the method has run successfully or has got an exception */

    /* @AfterReturn
     * same as Before but runs after the specified methods.
     * This runs only when method completes successfully and there is no exception thrown from within the method */

    /* @AfterThrowing
     * same as Before but runs after the specified methods.
     * This runs only if the advice/method throws an exception */

    /* will have the return string in the args of this method */
    @AfterReturning(pointcut = "args(name)", returning = "returnString")
    public void StringArgumentMethod(String name, String returnString) {
        System.out.println(
                "A method that takes string arguments has been called. ");
        System.out.println("the value is " + name);
        System.out.println("the output value is " + returnString);
    }

    /* run this advice after a method with string args throws an exception
     * that exception object can be used here as follows ex */
    @AfterThrowing(pointcut = "args(name)", throwing = "ex")
    public void exceptionAdvice(String name, RuntimeException ex) {
        System.out.println("An exception has been thrown " + ex);
    }

    /* Around advices runs before and after the respective methods
     * but we can take that method as an argument and control the
     * before and after executions of that method */
    @Around("allGettersDummy()")
    public void myAroundAdvice(ProceedingJoinPoint pjp) {

        /* programmer can add some statements here. */

        /* This is exactly when that method will be executed. */
        try {
            pjp.proceed();
        } catch (Throwable e) {
            e.printStackTrace();
        }

        /* programmer can add some statements here. */
    }

    /* @Around("@annotation(vishSpringAOP.unit001.aspect.Loggable)")
     * will apply to only those methods which as annotated as @loggable
     * for ex look in ShapeService class */

}
