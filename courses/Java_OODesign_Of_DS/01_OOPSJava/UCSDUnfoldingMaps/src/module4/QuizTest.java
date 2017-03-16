package module4;

import de.fhpotsdam.unfolding.data.PointFeature;
import de.fhpotsdam.unfolding.marker.Marker;
import de.fhpotsdam.unfolding.marker.SimplePointMarker;

public class QuizTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		PointFeature feature = null;
		
		Marker m = new OceanQuakeMarker(feature);
		
		EarthquakeMarker em = new OceanQuakeMarker(feature);
		
//		SimplePointMarker pm = new OceanQuakeMarker(feature);
//		EarthquakeMarker em1 = pm;
		
		Object o = new SimplePointMarker();
	
//		SimplePointMarker m = new Marker();
		
//		EarthquakeMarker em2 = new SimplePointMarker();
	}

}
