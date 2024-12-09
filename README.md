# cyrusurheim29
# Project Title
Equal Opportunity Boston: a data-driven volunteering approach
## Description
YOUTUBE LINK: https://youtu.be/npwl4FD0emc

The original purpose of this project was to build a website that allows users to view data (in the form of an interactive map) showing active volunteer opportunities in the broader Boston area. Volunteer opportunity data was collected from public archives such as the City of Boston's Community Center database, as well as lists and other forms of information scraped from reputable web sources. This data was then represented in a map feature that allows users to select an opportunity and find relevant contact information.

The current implementation builds on this core. The website runs on Flask and currently runs through VSCode hosted on Git Hub. It utilizes jinja to bridge the front-end HTML content that users view and interact with and the back-end python that establishes the website's space and provides all necessary data.

Our approach involves analyzing socioeconomic data and integrating it with existing volunteer opportunities to highlight areas of high need. This allows for the ability of users to view volunteer opportunities in their area and analyze relative levels of need based on current trends in housing and food disparity. As this project is completely open access, it benefits from user interactivity and contribution. More than this, as society develops on the large timescale and current availability of opportunities fluctuate on the small, input of users like yourself is essential. This website allows for such contribution, through submission of forms with new datasets, updated information, or anything else.


## Getting Started


### Dependencies
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

### Installing

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


### Executing program

* Once all the files have been uploaded successfully, begin by creating a virtual python environment in the finalproject folder by executing
  ```sh
  python -m venv <myenvpath>
  ```
*  To activate the virtual environment, execute
  ```sh
*  source venv/bin/activate
  ```
*  Once the virtual environment is activated, then you may begin installing the required dependencies using "pip install".
*  A Google Maps API Key is unfortunately required. In app.py, replace the existing placeholder with your API code
* To run the code, simply execute
  ```sh
  flask run
  ```
in the terminal, and open the web page via the forwarded port! Explore the Google Map's legend and heat map features; learn more about the project; contribute by sending in an email through the website; view the datasets.

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

* Many thanks to my TF Sedik for his dedicated support and advice.
* Inspiration of project exigence and html formatting comes from Harvard's own Opportunity Insights initiative.
