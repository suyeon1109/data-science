import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.evaluation.NominalPrediction;
import weka.classifiers.rules.DecisionTable;
import weka.classifiers.rules.PART;
import weka.classifiers.trees.DecisionStump;
import weka.classifiers.trees.J48;
import weka.core.FastVector;
import weka.core.Instances;

// class printResult {
//     int x;
//     int y;
//     Parent(int x, int y) {
//         this.x = x;
//         this.y = y;
//     }
//     public void display() {
//         System.out.println("x: " + x);
//         System.out.println("y: " + y);
//     }
// }

// class Child extends Parent {
//     int z;
//     Child(int x, int y, int z) {
//         super(x, y); 
//         this.z = z;
//     }
//     @Override public void display() {
//         System.out.println("x: " + x+z);
//         System.out.println("y: " + y+z);
//     }
// }
 
public class finalProject {
	public static BufferedReader readDataFile(String filename) {
		BufferedReader inputReader = null;

		try {
			inputReader = new BufferedReader(new FileReader(filename));
		} catch (FileNotFoundException ex) {
			System.err.println("File not found: " + filename);
		}
		return inputReader;
	}

	public static Evaluation classify(Classifier model, Instances trainingSet, Instances testingSet) throws Exception {
		Evaluation evaluation = new Evaluation(trainingSet);
		model.buildClassifier(trainingSet);
		evaluation.evaluateModel(model, testingSet);
		return evaluation;
	}

	public static double calculateAccuracy(FastVector predictions) {
		double correct = 0;

		for (int i = 0; i < predictions.size(); i++) {
			NominalPrediction np = (NominalPrediction) predictions.elementAt(i);
			if (np.predicted() == np.actual()) {
				correct++;
			}
		}
		return 100 * correct / predictions.size();
	}

	public static Instances[][] crossValidationSplit(Instances data, int numberOfFolds) {
		Instances[][] split = new Instances[2][numberOfFolds];

		for (int i = 0; i < numberOfFolds; i++) {
			split[0][i] = data.trainCV(numberOfFolds, i);
			split[1][i] = data.testCV(numberOfFolds, i);
		}
		return split;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader datafile = readDataFile("weather.txt");

		Instances data = new Instances(datafile);
		data.setClassIndex(data.numAttributes() - 1);

		// 10-split cross validation
		Instances[][] split = crossValidationSplit(data, 10);

		// split data
		Instances[] trainingSplits = split[0];
		Instances[] testingSplits = split[1];

		Classifier[] models = { 
				new J48(), // a decision tree
				new PART(), 
				new DecisionTable(),//decision table majority classifier
				new DecisionStump() //one-level decision tree
		};

		// Run for each model
		for (int j = 0; j < models.length; j++) {

			// Collect every group of predictions for current model in a FastVector
			FastVector predictions = new FastVector();

			// For each training-testing split pair, train and test the classifier
			for (int i = 0; i < trainingSplits.length; i++) {
				Evaluation validation = classify(models[j], trainingSplits[i], testingSplits[i]);

				predictions.appendElements(validation.predictions());

				// summary for each training-testing pair.
				System.out.println(models[j].toString());
			}

			// overall accuracy of current classifier
			double accuracy = calculateAccuracy(predictions);

			// print current classifier's name and accuracy
			System.out.println("Accuracy of " + models[j].getClass().getSimpleName() + ": " + String.format("%.2f%%", accuracy));
		}
	}
}