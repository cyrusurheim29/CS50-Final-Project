# cyrusurheim29
# Project Title
Equal Opportunity Boston: a data-driven volunteering approach
## Design

This project represents a multidisciplinary approach at creating a website to aid volunteers with finding opportunities in the Metro Boston Area. 

The website itself is coded in HTML. HTML's ability to become dynamic, through integration with Jinja and Flask, made it the perfect choice of language for coding the layout and structure of this project. Bootstrap afforded the tools to make specific HTML objectives possible. These specific HTML endeavors are:
<ol>
  <li>a "layout.html" file, which establishes the general layout for all different paths</li>
  <li>a drop-down menu, which allows for easy access to these paths</li>
  <li>an accordion element that contains more information on the project's goal</li>
</ol> 
Javascript additionally allowed for more customization of the static webpage itself. JS projects in the code include:
<ol>
  <li>"typewriter" code, that types out the "About Us" info in real time</li>
  <li>the entirety of the Google Map feature, and all of the specific syntax and requirements that came with utilizing Google Maps API; this includes the legend, the heat maps, orienting the map on Boston, inputting Pins onto the map, etc.</li>
</ol> 


### HTML Front-End
* Built with
<ol>
  <li>python</li>
  <li>HTML/JavaScript</li>
  <li>Jinja</li>
  <li>Flask</li>
  <li>SQL</li>
</ol> 


* Dependencies are listed below
<ol>
  <li>flask</li>
  <li>cs50 (for SQL)</li>
  <li>os</li>
  <li>selenium</li>
  <li>time</li>
  <li>pandas</li>
  <li>sqlite3</li>
  <li>pdfplumber</li>
  <li>csv</li>
</ol> 

### JavaScript Usage

* Download the project.zip file and open in VSCode. You should have the following structure:

finalproject/  
├── app.py/                 
├── static/               
│   ├── aa_heatmap_data.json  
|   ├── college_heatmap.json  
│   ├── fi_heatmap.json  
|   ├── fi_p_heatmap_data_set2.json  
|   ├── lat_heatmap_data.json  
|   ├── mhi_heatmap_data.json  
|   ├── pov_heatmap_data.json  
│   └── styles.css  
├── templates/          
│   ├── aboutus.html          
│   ├── contribute.html      
│   ├── datasets.html   
│   ├── layout.html               
│   └── map.html                
├── web_scraping/                 
│   ├── bcyf_links.py             
│   ├── bcyf_links.txt  
│   ├── bcyf.py                   
│   ├── community_centers.csv  
│   ├── complete_homeless_shelters.csv  
│   ├── complete_kitchens.csv  
│   ├── complete_kitchens1.csv  
│   ├── complete_kitchens2.csv  
│   ├── complete_kitchens3.csv  
│   ├── delete.py  
│   ├── food_banks.pdf  
│   ├── foodbanks_add.py         
│   ├── homeless_shelters.py         
│   ├── kitchens.csv  
│   └── volopps.db  
├── app.py  
└── __pycache__/                


### Python Backend (Flask, app.py)

* Once all the files have been uploaded successfully, begin by creating a virtual python environment in the finalproject folder by executing
  ```sh
  python -m venv <myenvpath>
  ```
*  To activate the virtual environment, execute
  ```sh
*  source venv/bin/activate
  ```
*  Once the virtual environment is activated, then you may begin installing the required dependencies using "pip install".

* To run the code, simply execute
  ```sh
  flask run
  ```
in the terminal, and open the web page via the forwarded port! Explore the Google Map's legend and heat map features; learn more about the project; contribute by sending in an email through the website; view the datasets.

### Python Backend (Web Scraping and Data Collection)

## Authors
Cyrus Urheim

## Version History

* 0.2
    * In the works!
* 0.1
    * Initial Release, Dec 8, 2024

## License

This project is not licensed as of now. It is completely publicly accessible and usable.

## Acknowledgments

* Many thanks to my CS50 Sedik for his dedicated support and advice.
* Inspiration of project exigence and html formatting comes from Harvard's own Opportunity Insights initiative.
