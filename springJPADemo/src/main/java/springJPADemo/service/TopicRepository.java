package springJPADemo.service;

import org.springframework.data.repository.CrudRepository;
import springJPADemo.model.Topic;

public interface TopicRepository extends CrudRepository<Topic, String> {

}
