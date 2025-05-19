import weka.core.converters.ConverterUtils.DataSource;
import weka.core.Instances;
import weka.classifiers.trees.RandomForest;
import weka.classifiers.Evaluation;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class AnalysisVM_Advanced {
    public static void main(String[] args) throws Exception {
        // Crear directorio para guardar resultados si no existe
        String resultsDirPath = "results";
        File resultsDir = new File(resultsDirPath);
        if (!resultsDir.exists()) resultsDir.mkdir();
        
        // Cargar datos (Iris dataset)
        DataSource source = new DataSource("iris.arff");
        Instances data = source.getDataSet();
        if (data.classIndex() == -1) data.setClassIndex(data.numAttributes() - 1);
        
        // Exploración inicial de datos
        System.out.println("\nResumen de Datos:");
        System.out.println(data.toSummaryString());
        System.out.println("\nDistribución de las Especies:");
        int numClasses = data.numClasses();
        for (int i = 0; i < numClasses; i++) {
            String className = data.classAttribute().value(i);
            int count = data.attributeStats(data.classIndex()).nominalCounts[i];
            System.out.println(className + ": " + count);
        }
        
        // Guardar resumen de datos
        try (FileWriter summaryWriter = new FileWriter(new File(resultsDir, "data_summary_vm.txt"))) {
            summaryWriter.write(data.toSummaryString());
        }
        try (FileWriter speciesWriter = new FileWriter(new File(resultsDir, "species_count_vm.txt"))) {
            for (int i = 0; i < numClasses; i++) {
                String className = data.classAttribute().value(i);
                int count = data.attributeStats(data.classIndex()).nominalCounts[i];
                speciesWriter.write(className + ": " + count + "\n");
            }
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
        
        // Guardar reporte de clasificación
        try (FileWriter reportWriter = new FileWriter(new File(resultsDir, "classification_report_vm.txt"))) {
            reportWriter.write(eval.toSummaryString());
            reportWriter.write(eval.toMatrixString("\nMatriz de Confusión:"));
        }
        
        System.out.println("\nAnálisis completado en VM. Resultados guardados en la carpeta 'results'.");
    }
}
