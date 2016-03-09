package catalinc.programming_praxis;

import java.util.LinkedList;
import java.util.Random;

public class DavidGriesCoffeCanProblem {

    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.printf("usage: %s WHITE_BEAN_COUNT BLACK_BEAN_COUNT\n",
                    DavidGriesCoffeCanProblem.class.getName());
            System.exit(1);
        }

        int whiteBeanCount = Integer.parseInt(args[0]);
        int blackBeanCount = Integer.parseInt(args[1]);
        simulate(whiteBeanCount, blackBeanCount);
    }

    private static void simulate(int whiteBeanCount, int blackBeanCount) {
        System.out.printf("Coffe-can contains %d WHITE and %d BLACK beans\n", whiteBeanCount, blackBeanCount);
        CoffeCan can = new CoffeCan(whiteBeanCount, blackBeanCount);
        while (can.beanCount() > 1) {
            Bean b0 = can.selectBean();
            Bean b1 = can.selectBean();
            if (b0 == b1) {
                can.addBean(Bean.BLACK);
            } else {
                can.addBean(Bean.WHITE);
            }
        }
        System.out.printf("The last last bean is %s\n", can.selectBean());
    }

}

enum Bean {
    WHITE,
    BLACK
}

class CoffeCan {

    private Random random;
    private LinkedList<Bean> beans;

    CoffeCan(int whiteBeanCount, int blackBeanCount) {
        random = new Random();
        beans = new LinkedList<>();

        for (int i = 0; i < whiteBeanCount; i++) {
            addBean(Bean.WHITE);
        }
        for (int i = 0; i < blackBeanCount; i++) {
            addBean(Bean.BLACK);
        }
    }

    public int beanCount() {
        return beans.size();
    }

    public void addBean(Bean bean) {
        if (beans.size() >= 1) {
            int index = random.nextInt(beans.size());
            beans.add(index, bean);
        } else {
            beans.add(bean);
        }
    }

    public Bean selectBean() {
        return beans.remove(0);
    }

}
