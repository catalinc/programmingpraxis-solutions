package catalinc.programming_praxis.permuted_index;

public class SentencePartition {

    private String head;
    private String tail;

    public SentencePartition(String head, String tail) {
        this.head = head;
        this.tail = tail;
    }

    public String getHead() {
        return head;
    }

    public String getTail() {
        return tail;
    }

    public void setHead(String head) {
        this.head = head;
    }

    public void setTail(String tail) {
        this.tail = tail;
    }
}
