import weka.core.converters.ConverterUtils.DataSource;
import weka.core.Instances;
import weka.classifiers.trees.RandomForest;
import weka.classifiers.Evaluation;
import java.util.Random;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class AnalysisVM_Basic {
    public static void main(String[] args) throws Exception {
        // Cargar el conjunto de datos Iris
        DataSource source = new DataSource("iris.arff");
        Instances data = source.getDataSet();
        if (data.classIndex() == -1) data.setClassIndex(data.numAttributes() - 1);
        
        // Exploración inicial de datos
        System.out.println("\nResumen de Datos:");
        System.out.println(data.toSummaryString());
        
        // Distribución de las especies
        System.out.println("\nDistribución de las Especies:");
        int numClasses = data.numClasses();
        for (int i = 0; i < numClasses; i++) {
            String className = data.classAttribute().value(i);
            int count = data.attributeStats(data.classIndex()).nominalCounts[i];
            System.out.println(className + ": " + count);
        }
        
        // Dividir datos en entrenamiento y prueba (70-30)
        int trainSize = (int) Math.round(data.numInstances() * 0.7);
        int testSize = data.numInstances() - trainSize;
        Instances train = new Instances(data, 0, trainSize);
        Instances test = new Instances(data, trainSize, testSize);
        
        // Entrenamiento del modelo
        RandomForest rf = new RandomForest();
        rf.setNumTrees(100);
        rf.buildClassifier(train);
        
        // Evaluación del modelo
        Evaluation eval = new Evaluation(train);
        eval.evaluateModel(rf, test);
        System.out.println("\nReporte de Clasificación:");
        System.out.println(eval.toSummaryString());
        System.out.println(eval.toMatrixString("\nMatriz de Confusión:"));
        
        // Guardar resultados
        File resultsDir = new File("results");
        if (!resultsDir.exists()) resultsDir.mkdir();
        try (FileWriter reportWriter = new FileWriter(new File(resultsDir, "classification_report_vm.txt"))) {
            reportWriter.write(eval.toSummaryString());
            reportWriter.write(eval.toMatrixString("\nMatriz de Confusión:"));
        }
        
        System.out.println("\nAnálisis completado en VM. Resultados guardados en la carpeta 'results'.");
    }
}
