package catalinc.programming_praxis.bst;

public class BinarySearchTree<T extends Object & Comparable<? super T>> {

    private Node<T> root;
    private int size;

    public BinarySearchTree() {
        clear();
    }

    public int size() {
        return size;
    }

    public boolean lookup(T value) {
        Node<T> n = root;
        while (n != null) {
            switch (value.compareTo(n.getData())) {
                case 0:
                    return true;
                case -1:
                    n = n.getLeft();
                    break;
                case 1:
                default:
                    n = n.getRight();
            }
        }
        return false;
    }

    public void insert(T value) {
        root = insert(new Node<T>(value), root);
        size++;
    }

    private Node<T> insert(Node<T> node, Node<T> start) {

        if (start == null) {
            return node;
        }

        if (node == null) {
            return start;
        }

        Node<T> n = start;
        boolean done = false;
        while (!done) {
            switch (node.getData().compareTo(n.getData())) {
                case 0:
                case -1:
                    if (n.getLeft() == null) {
                        n.setLeft(node);
                        done = true;
                    } else {
                        n = n.getLeft();
                    }
                    break;
                case 1:
                default:
                    if (n.getRight() == null) {
                        n.setRight(node);
                        done = true;
                    } else {
                        n = n.getRight();
                    }
            }
        }

        return start;
    }

    public void delete(T value) {
        Node<T> n = root;
        Node<T> p = null;
        boolean done = false;
        boolean isLeft = false;
        while (!(n == null || done)) {
            switch (value.compareTo(n.getData())) {
                case 0:
                    n = insert(n.getLeft(), n.getRight());
                    if (p == null) {
                        root = n;
                    } else {
                        if (isLeft) {
                            p.setLeft(n);
                        } else {
                            p.setRight(n);
                        }
                    }
                    size--;
                    done = true;
                    break;
                case -1:
                    isLeft = true;
                    p = n;
                    n = n.getLeft();
                    break;
                case 1:
                default:
                    isLeft = false;
                    p = n;
                    n = n.getRight();
            }
        }
    }

    public void clear() {
        root = null;
        size = 0;
    }

}
