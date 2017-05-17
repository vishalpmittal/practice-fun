package dsAlgo;

import java.util.Arrays;

public class Trials {

    private enum PolProps {
        hostFailuresToTolerate, localSnapshotFrequency, localInstancesRetained, localProtection;
    }

    public static void main(String[] args) {
        // String s = "P1_VSAN_LP-10.145.137.51-vsanDatastore-centos-64-vmwpv-p-0001";
        // System.out.println(s.split("-", 2)[1]);

        String test = PolProps.hostFailuresToTolerate.toString();
        
        System.out.println(test);
    }
}
