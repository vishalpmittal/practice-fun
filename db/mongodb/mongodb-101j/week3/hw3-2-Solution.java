ANSWER

BlogPostDAO.java:


import static com.mongodb.client.model.Filters.eq;
import static com.mongodb.client.model.Sorts.descending;

import java.util.ArrayList;

    // Return a single post corresponding to a permalink
    public Document findByPermalink(String permalink) {

        // XXX HW 3.2,  Work Here

        Document post = postsCollection.find(eq("permalink", permalink)).first();

        return post;
    }

    // Return a list of posts in descending order. Limit determines
    // how many posts are returned.
    // Requires importing com.mongodb.client.model.Sorts.descending
    public List<Document> findByDateDescending(int limit) {

        // XXX HW 3.2,  Work Here
        // Return a list of DBObjects, each one a post from the posts collection

        List<Document> posts = postsCollection.find().sort(descending("date")).limit(limit).into(new ArrayList<Document>());

        return posts;
    }

    public String addPost(String title, String body, List tags, String username) {

        System.out.println("inserting blog entry " + title + " " + body);

        String permalink = title.replaceAll("\\s", "_"); // whitespace becomes _
        permalink = permalink.replaceAll("\\W", ""); // get rid of non alphanumeric
        permalink = permalink.toLowerCase();


        // XXX HW 3.2, Work Here
        // Remember that a valid post has the following keys:
        // author, body, permalink, tags, comments, date
        //
        // A few hints:
        // - Don't forget to create an empty list of comments
        // - for the value of the date key, today's datetime is fine.
        // - tags are already in list form that implements suitable interface.
        // - we created the permalink for you above.

        // Build the post object and insert it


        // Build the post object.
        Document post = new Document()
                        .append("title", title)
                        .append("author", username)
                        .append("body", body)
                        .append("permalink", permalink)
                        .append("tags", tags)
                        .append("comments", new ArrayList())
                        .append("date", new java.util.Date());

        postsCollection.insertOne(post);
        System.out.println("Inserting blog post with permalink " + permalink);

        return permalink;

    }