package designPatterns.creational.factoryMethod.websites;

import designPatterns.creational.factoryMethod.pages.AboutPage;
import designPatterns.creational.factoryMethod.pages.CommentPage;
import designPatterns.creational.factoryMethod.pages.ContactPage;
import designPatterns.creational.factoryMethod.pages.PostPage;

public class Blog extends Website {

	@Override
	public void createWebsite() {
		pages.add(new PostPage());
		pages.add(new AboutPage());
		pages.add(new ContactPage());
		pages.add(new CommentPage());
	}
}
