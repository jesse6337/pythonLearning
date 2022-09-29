import java.lang.annotation.Retention;

public class findProb {
    double sensor_acc = 0.9;
    double sensor_wrong = 1.0 - sensor_acc;
    double normalizer = 0;

    double[] find_prop(char[] world_, double[] belief_, double wlen_, char currentSensorReading_) {
        for (int i = 0; i < world_.length; i++) {
            if (world_[i] == currentSensorReading_) {
                belief_[i] *= sensor_acc;
            } else if (world_[i] != currentSensorReading_) {
                belief_[i] *= sensor_wrong;
            }
        }
        for (int i = 0; i < belief_.length; i++) {
            normalizer += belief_[i];
        }
        for (int i = 0; i < belief_.length; i++) {
            belief_[i] /= normalizer;
            System.out.println(belief_[i]);
        }
        return belief_;
    }
}
