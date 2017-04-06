package springBootDemo.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    /* will be returned for http://localhost:8080/hello */
    @RequestMapping("/hello")
    public String sayHello() {
        return "Hello";
    }
    
    
}
