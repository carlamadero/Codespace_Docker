import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class AnalysisVM_Advanced {
    public static void main(String[] args) throws IOException {
        // Crear directorio para guardar resultados si no existe
        String resultsDirPath = "results";
        File resultsDir = new File(resultsDirPath);
        if (!resultsDir.exists()) resultsDir.mkdir();
        
        // Simulación de datos Iris
        String[] species = {"setosa", "versicolor", "virginica"};
        List<String> data = Arrays.asList(
                "setosa", "setosa", "versicolor", "virginica", "virginica", "setosa", "versicolor", "virginica"
        );
        
        // Exploración inicial de datos
        System.out.println("\nResumen de Datos:");
        System.out.println("Cantidad total de muestras: " + data.size());
        System.out.println("\nDistribución de las Especies:");
        for (String s : species) {
            long count = data.stream().filter(e -> e.equals(s)).count();
            System.out.println(s + ": " + count);
        }
        
        // Guardar resumen de datos
        try (FileWriter summaryWriter = new FileWriter(new File(resultsDir, "data_summary_vm.txt"))) {
            summaryWriter.write("Cantidad total de muestras: " + data.size() + "\n");
        }
        try (FileWriter speciesWriter = new FileWriter(new File(resultsDir, "species_count_vm.txt"))) {
            for (String s : species) {
                long count = data.stream().filter(e -> e.equals(s)).count();
                speciesWriter.write(s + ": " + count + "\n");
            }
        }
        
        // Simulación de clasificación
        Random random = new Random();
        List<String> predictions = new ArrayList<>();
        for (String sample : data) {
            predictions.add(species[random.nextInt(species.length)]);
        }
        
        // Guardar reporte de clasificación
        try (FileWriter reportWriter = new FileWriter(new File(resultsDir, "classification_report_vm.txt"))) {
            reportWriter.write("Simulación de reporte de clasificación.\n");
            for (String s : species) {
                long correct = data.stream().filter(e -> e.equals(s)).count();
                long predictedCount = predictions.stream().filter(e -> e.equals(s)).count();
                reportWriter.write(s + " - Real: " + correct + ", Predicho: " + predictedCount + "\n");
            }
        }
        
        System.out.println("\nAnálisis completado en VM. Resultados guardados en la carpeta 'results'.");
    }
}
