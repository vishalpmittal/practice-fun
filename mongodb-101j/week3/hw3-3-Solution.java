ANSWER

BlogPostDAO.java


    // Append a comment to a blog post
    public void addPostComment(final String name, final String email, final String body,
                               final String permalink) {

        // XXX HW 3.3, Work Here
        // Hints:
        // - email is optional and may come in NULL. Check for that.
        // - best solution uses an update command to the database and a suitable
        //   operator to append the comment on to any existing list of comments
        Document comment = new Document("author", name).append("body", body);
        if (email != null && !email.equals("")) {
            comment.append("email", email);
        }

        postsCollection.updateOne(eq("permalink", permalink),
                                  new Document("$push", new Document("comments", comment)));
    }