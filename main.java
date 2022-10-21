
public class main {
    public static void main(String[] args) {
        findProb prob = new findProb();
        char[] world = { 'g', 'g', 'r', 'g' };
        double[] belief = { world.length };
        double Xi = 1.0 / world.length;
        for (int i = 0; i < belief.length; i++) {
            belief[i] = Xi;
            System.out.println(belief[i]);
        }
        double[] newBelief = prob.find_prop(world, belief, 'g');
        for (int i = 0; i < belief.length; i++) {
            System.out.println(newBelief[i]);
        }
    }
}