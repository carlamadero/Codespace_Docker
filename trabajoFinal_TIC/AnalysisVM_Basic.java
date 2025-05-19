import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class AnalysisVM_Basic {
    public static void main(String[] args) throws IOException {
        // Crear lista de datos (simulación del dataset Iris)
        List<String> data = new ArrayList<>(Arrays.asList(
            "setosa", "setosa", "versicolor", "virginica", "virginica", "setosa", "versicolor", "virginica",
            "setosa", "versicolor", "versicolor", "virginica", "setosa", "setosa", "virginica", "virginica"
        ));
        String[] species = {"setosa", "versicolor", "virginica"};
        
        // Exploración inicial de datos
        System.out.println("\nResumen de Datos:");
        System.out.println("Cantidad total de muestras: " + data.size());
        
        // Distribución de las especies
        System.out.println("\nDistribución de las Especies:");
        for (String s : species) {
            long count = data.stream().filter(e -> e.equals(s)).count();
            System.out.println(s + ": " + count);
        }
        
        // División de datos en entrenamiento y prueba (70-30), creando listas independientes
        int trainSize = (int) (data.size() * 0.7);
        List<String> train = new ArrayList<>(data.subList(0, trainSize));
        List<String> test = new ArrayList<>(data.subList(trainSize, data.size()));
        
        // Simulación de clasificación (predicciones aleatorias)
        Random random = new Random();
        List<String> predictions = new ArrayList<>();
        for (String sample : test) {
            predictions.add(species[random.nextInt(species.length)]);
        }
        
        // Guardar reporte simulado en carpeta 'results'
        File resultsDir = new File("results");
        if (!resultsDir.exists()) resultsDir.mkdir();
        
        try (FileWriter reportWriter = new FileWriter(new File(resultsDir, "classification_report_vm.txt"))) {
            reportWriter.write("Simulación de reporte de clasificación.\n");
            for (String s : species) {
                long realCount = test.stream().filter(e -> e.equals(s)).count();
                long predictedCount = predictions.stream().filter(e -> e.equals(s)).count();
                reportWriter.write(s + " - Real: " + realCount + ", Predicho: " + predictedCount + "\n");
            }
        }
        
        System.out.println("\nAnálisis completado en VM. Resultados guardados en la carpeta 'results'.");
    }
}
