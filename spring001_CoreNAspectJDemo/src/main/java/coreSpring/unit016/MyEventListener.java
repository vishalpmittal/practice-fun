package coreSpring.unit016;

import org.springframework.context.ApplicationListener;
import org.springframework.context.ApplicationEvent;
import org.springframework.stereotype.Component;

@Component
public class MyEventListener implements ApplicationListener<ApplicationEvent> {

    public void onApplicationEvent(ApplicationEvent appEvent) {
        System.out.println(appEvent.toString());
    }

}
