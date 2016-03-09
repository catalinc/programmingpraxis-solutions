package main.java.catalinc.programming_praxis;

/**
 * Solution to http://programmingpraxis.com/2014/11/04/gaussian-integers-part-1/
 */
public class Gaussian {

    private final int re;
    private final int im;

    public Gaussian(int re, int im) {
        this.re = re;
        this.im = im;
    }

    public Gaussian add(Gaussian other) {
        return new Gaussian(this.re + other.re, this.im + other.im);
    }

    public Gaussian substract(Gaussian other) {
        return new Gaussian(this.re - other.re, this.im - other.im);
    }

    public Gaussian multiply(Gaussian other) {
        int re = this.re * other.re - this.im * other.im;
        int im = this.re * other.im + this.im * other.re;
        return new Gaussian(re, im);
    }

    public Gaussian quotient(Gaussian other) {
        int n = other.re * other.re + other.im * other.im;
        int re = Math.round((float) (this.re * other.re + this.im * other.im) / n);
        int im = Math.round((float) (this.im * other.re - this.re * other.im) / n);
        return new Gaussian(re, im);
    }

    public Gaussian remainder(Gaussian other) {
        Gaussian quot = quotient(other);
        return substract(quot.multiply(other));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Gaussian gaussian = (Gaussian) o;

        if (im != gaussian.im) return false;
        if (re != gaussian.re) return false;

        return true;
    }

    @Override
    public int hashCode() {
        int result = re;
        result = 31 * result + im;
        return result;
    }

    @Override
    public String toString() {
        return "main.java.catalinc.programming_praxis.Gaussian{" +
                "re=" + re +
                ", im=" + im +
                '}';
    }

    public static void main(String[] args) {
        Gaussian a = new Gaussian(10, 10);
        Gaussian b = new Gaussian(5, 5);

        System.out.println(a.add(b));
        System.out.println(a.substract(b));
        System.out.println(a.multiply(b));
        System.out.println(a.quotient(b));
        System.out.println(a.remainder(b));
    }
}
