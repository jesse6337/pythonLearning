public class main {
    public static void main(String[] args) {
        findProb findP = new findProb();
        char[] world = { 'r', 'g', 'g', 'r', 'g' };
        double[] belief = new double[world.length];
        double wlen = 1.0 / world.length;
        for (int i = 0; i < world.length; i++) {
            belief[i] = wlen;
        }
        belief = findP.find_prop(world, belief, wlen, 'g');
    }
}