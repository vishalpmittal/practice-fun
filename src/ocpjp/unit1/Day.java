package ocpjp.unit1;

import java.time.Month;

final class Day {

    private String name;

    private Day(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public static final Day MONDAY = new Day("Monday");
    public static final Day TUESDAY = new Day("Tuesday");
    public static final Day WEDNESDAY = new Day("Wednesday");
    public static final Day THURSDAY = new Day("Thursday");
    public static final Day FRIDAY = new Day("Friday");
    public static final Day SATURDAY = new Day("Saturday");
    public static final Day SUNDAY = new Day("Sunday");

    public static Day[] values() {
        return new Day[] { MONDAY, TUESDAY, WEDNESDAY };
    }
}

enum Day1 {
    MONDAY("Monday"), TUESDAY(), Wednesday("Wednesday"), Thursday("Thursday"), Friday("Friday"), Saturday(
            "Saturday"), Sunday("Sunday");

    String name;

    Day1() {

    }

    Day1(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

class DayTest {
    public static void test() {
        Day1 d = Day1.TUESDAY;
        System.out.println(d.getName());

        Day1[] dArr = Day1.values();
    }
}

class DayTester {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {

        }

        Month mnth = Month.valueOf("FEB");
        Day1[] d = Day1.values();
        Day1 d1 = Day1.valueOf("Monday");
        System.out.println(Day1.MONDAY.name);
    }
}