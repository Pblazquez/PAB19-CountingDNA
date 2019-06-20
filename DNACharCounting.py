
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

/**
 * Created by ajnebro on 30/3/16.
 */
public class DNACharCounting {
    public static void main(String[] args) throws FileNotFoundException {

        long[] result = new long[]{0, 0, 0, 0};
        long initTime = System.currentTimeMillis();
        try (Stream<String> stream = Files.lines(Paths.get(args[0]))) {
            result = stream
                    .parallel()
                    .map(line -> {
                        long[] localCount = new long[4];
                        //
                        for (int i = 0; i < line.length(); i++) {
                            char c = line.charAt(i);
                            switch (c) {
                                case 'A':
                                    localCount[0]++;
                                    break;
                                case 'C':
                                    localCount[1]++;
                                    break;
                                case 'T':
                                    localCount[2]++;
                                    break;
                                case 'G':
                                    localCount[3]++;
                            }
                        }
                        return localCount;
                    })
                    .reduce(new long[]{0, 0, 0, 0}, (vector1, vector2) -> {
                        long[] totalCount = new long[4];
                        for (int i = 0; i < vector1.length; i++) {
                            totalCount[i] = vector1[i] + vector2[i];
                        }
                        return totalCount;
                    });
        } catch (IOException e) {
            e.printStackTrace();
        }

        long computingTime = System.currentTimeMillis() - initTime;

        System.out.println("Computing time: " + computingTime);
        System.out.printf("%d %d %d %d", result[0], result[1], result[2], result[3] );
    }
}
