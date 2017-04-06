package springBootDemo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import springBootDemo.model.Topic;
import springBootDemo.service.TopicService;

@RestController
public class TopicController {

    @Autowired
    private TopicService topicService;

    /* GET is default
     * 
     * @RequestMapping(method = RequestMethod.GET, value = "/topics") */
    @RequestMapping("/topics")
    public List<Topic> getAppTopics() {
        return topicService.getAllTopics();
    }

    @RequestMapping("/topics/{id}")
    public Topic getTopic(@PathVariable String id) {
        return topicService.getTopic(id);
    }

    @RequestMapping(method = RequestMethod.POST, value = "/topics")
    public void addTopic(@RequestBody Topic topic) {
        topicService.addTopic(topic);
    }

    @RequestMapping(method = RequestMethod.PUT, value = "/topics/{id}")
    public void updateTopic(@RequestBody Topic topic, @PathVariable String id) {
        topicService.updateTopic(id, topic);
    }

    @RequestMapping(method = RequestMethod.DELETE, value = "/topics/{id}")
    public void deleteTopic(@PathVariable String id) {
        topicService.deleteTopic(id);
    }

    /* =======================
     * Unit One
     * =======================
     * 
     * @RequestMapping("/topics_str")
     * public String getAppTopics_str() {
     * return "All Topics";
     * }
     * 
     * @RequestMapping("/topics")
     * public List<Topic> getAppTopics() {
     * return Arrays.asList(new Topic("springId", "Spring Framework Name", "spring Framework desciption"),
     * new Topic("javaId", "Java Name", "java desciption"),
     * new Topic("javascriptId", "Javascript name", "javascript desciption"));
     * } */
}
