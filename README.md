In this project I built a web mapping application about building permits in Calgary. Users can filter and visualize building permits in Calgary in a mapping front-end.

**Application.py:**
There are only 2 routes in this file.

1. `@app.route("/")` 
	- This is the home page, some info that indicates no searches have been performed is sent and the `index.html` template is rendered.
	- ![](https://github.com/mitchellbrown98/ENGO55Lab2/blob/main/screenshots/2021-02-22_10h28_25.png)
	
2. `@app.route("/search")`
	- This route takes in the 2 values from the start and end date pickers, and formats them so they can be placed in the api call URL. 
	- ![](https://github.com/mitchellbrown98/ENGO55Lab2/blob/main/screenshots/2021-02-22_10h29_24.png)
	- The api call response is converted to a json object, and the 'features' are assigned to a new variable. 
	- The formatted date values are sent back to the html page along with the geojson object. 
	

**HTML Files:**

`Index.html:`

- This page has a map on the left side, and a search function on the right side. 
- The map will request the user's location, and pan to it if they accept. If they decline, it will be centered on Calgary. The map is using stadiamaps tiles. 
- When the web page is first loaded, there will be no markers on the map, and some text below the search function will indicate no results are being shown on the page.
- ![](https://github.com/mitchellbrown98/ENGO55Lab2/blob/main/screenshots/2021-02-22_10h28_25.png)
- The search function allows users to search for building permits within a date range. The datepickers are by Gijgo.com and they are a plug-in for the jQuery Javascript library.
- If the user enters an 'End date' that is earlier than the 'start date', an error message is displayed, and nothing happens.
- ![](https://github.com/mitchellbrown98/ENGO55Lab2/blob/main/screenshots/2021-02-22_10h30_26.png)
- If they enter 2 valid dates, the search will be performed by the api call, and a geojson object will be returned. 
- A markercollection Cluster group is created with some settings to allow spiderfyOnMaxZoom, and to keep the clusters on max zoom (so the spiderfy effect works correctly)
- The script will loop through each item in the geojson object, and create a geojson feature if the object has a geometry type defined. 
- Each geojson feature will have the issueddate, workclassgroup, contractor, community, and originaladdress properties binded to it with a popup. 
- Each geojson feature will then be added to the markercollection layer group. 
- The total length of the markercollection layer group is determined, and the value is displayed below the search function, to let users know how many results are being displayed on the map between the two dates they picked. 
- ![](https://github.com/mitchellbrown98/ENGO55Lab2/blob/main/screenshots/2021-02-22_10h31_27.png)
- Users can then click on individual markers to see the pop up info, and can click on clusters to zoom in to them. 
- ![](https://github.com/mitchellbrown98/ENGO55Lab2/blob/main/screenshots/2021-02-22_10h32_04.png)
- For buildings with multiple permits, users can click on the cluster, and the markers will spiderfy out, so each individual one can be seen/clicked on. 
- ![](https://github.com/mitchellbrown98/ENGO55Lab2/blob/main/screenshots/2021-02-22_10h32_45.png)
- When a new search is performed, the markercollection layer will be cleared out, and removed from the map before new geojson features are added to it. 
