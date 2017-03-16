package guimodule;

import java.util.List;
import java.util.Map;

import de.fhpotsdam.unfolding.UnfoldingMap;
import de.fhpotsdam.unfolding.data.GeoJSONReader;
import de.fhpotsdam.unfolding.providers.Google;
import de.fhpotsdam.unfolding.utils.MapUtils;
import de.fhpotsdam.unfolding.data.Feature;
import de.fhpotsdam.unfolding.marker.Marker;
import processing.core.PApplet;
import parsing.ParseFeed;

public class LifeExpectancy extends PApplet
{
	UnfoldingMap map = null;
	Map<String, Float> lifeExpByCountry = null;
	
	List<Feature> countries = null;
	List<Marker> countryMarkers = null;
	
	public void setup(){
		
		lifeExpByCountry = ParseFeed.loadLifeExpectancyFromCSV(this, "../data/LifeExpectancyWorldBank.csv"); 
		countries = GeoJSONReader.loadData(this, "../data/countries.geo.json");
		countryMarkers = MapUtils.createSimpleMarkers(countries);
		
		size(1000, 800, OPENGL);
		map = new UnfoldingMap(this, 50, 50, 900, 700, new Google.GoogleMapProvider());
		MapUtils.createDefaultEventDispatcher(this, map);
		
		map.addMarkers(countryMarkers);
		shadeCountries();
	}
	
	public void draw(){
		map.draw();
	}
	
	private void shadeCountries(){
		for (Marker marker : countryMarkers){
			String countryId = marker.getId();
			
			if (lifeExpByCountry.containsKey(countryId)){
				float lifeExp = lifeExpByCountry.get(countryId);
				int colorLevel = (int) map(lifeExp, 40, 90, 10, 255);
				marker.setColor(color(255-colorLevel, 100, colorLevel));
			}
			else{
				marker.setColor(color(150,150,150));
			}
		}
	}
	
}
