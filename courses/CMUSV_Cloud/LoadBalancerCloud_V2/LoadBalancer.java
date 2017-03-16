import java.io.IOException;
import java.net.ServerSocket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class LoadBalancer {
        private static final int THREAD_POOL_SIZE = 4;
        private final ServerSocket socket;
        private final DataCenterInstance[] instances;

        public LoadBalancer(ServerSocket socket, DataCenterInstance[] instances) {
                this.socket = socket;
                this.instances = instances;
        }

        // Complete this function
        public void start() throws IOException {
        		int dc_inst_num = 0;
                ExecutorService executorService = Executors.newFixedThreadPool(THREAD_POOL_SIZE);
                while (true) {
                        // By default, it will send all requests t o the first instance
                        Runnable requestHandler = new RequestHandler(socket.accept(), instances[dc_inst_num]);
                        executorService.execute(requestHandler);
                       	dc_inst_num++;
                        if (dc_inst_num >= 3)
                        	dc_inst_num = 0;
                }
        }
}
