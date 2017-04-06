package coreSpring.unit016;

import org.springframework.context.ApplicationEvent;

public class DrawEvent extends ApplicationEvent {

    public DrawEvent(Object source) {
        super(source);
    }

    public String toString() {
        return "Draw event occured";
    }
}
