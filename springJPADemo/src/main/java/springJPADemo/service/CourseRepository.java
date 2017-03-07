package springJPADemo.service;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import springJPADemo.model.Course;

public interface CourseRepository extends CrudRepository<Course, String> {

    /* Declaration to find course by name */
    public List<Course> findByName(String name);

    /* Declaration to find course by description */
    public List<Course> findByDescription(String foo);

    /* Declaration to find course by topic id in there */
    public List<Course> findByTopicId(String topicId);
}
