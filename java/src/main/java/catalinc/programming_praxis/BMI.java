package catalinc.programming_praxis;

public class BMI {

    public static float computeBmi(float weightInKg, float heightInM) {
        return weightInKg / (heightInM * heightInM);
    }

    public static void main(String[] args) {
        if (args.length >= 2) {
            float weightInKg = Float.valueOf(args[0]);
            float heightInM = Float.valueOf(args[1]);
            float bmi = computeBmi(weightInKg, heightInM);
            System.out.printf("Kg: %f H: %f BMI: %f\n", weightInKg, heightInM, bmi);
        } else {
            System.out.printf("Usage: %s WeightInKg HeightInM\n", BMI.class.getName());
        }
    }

}
