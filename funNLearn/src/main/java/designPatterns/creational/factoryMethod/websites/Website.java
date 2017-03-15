package designPatterns.creational.factoryMethod.websites;

import java.util.ArrayList;
import java.util.List;

import designPatterns.creational.factoryMethod.pages.Page;

public abstract class Website {
    protected List<Page> pages = new ArrayList<Page>();

    public List<Page> getPages() {
        return pages;
    }

    public Website() {
        this.createWebsite();
    }

    public abstract void createWebsite();
}
