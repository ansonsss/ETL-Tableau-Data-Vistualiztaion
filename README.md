

<h1>LA Crime Analysis (2020-2023)</h1>
     <p><a href="https://public.tableau.com/views/LACrime2020-2023/LACrime2020-2023?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">View the Tableau Dashboard</a></p>
    <p>
        This project showcases an ETL process using Python to clean and prepare a dataset of crime incidents in Los Angeles from 2020 to 2023, followed by a visual analysis in Tableau. This project demonstrates data extraction, cleaning, and transformation, culminating in an interactive Tableau dashboard for insights into crime trends across different locations, times, and crime types.
    </p>
    <img width="576" alt="LA Crime Area" src="https://github.com/user-attachments/assets/3051dcca-c294-4276-916a-85becc16fc3e">

    
<h2>Project Overview</h2>
    <ul>
        <li><strong>Objective:</strong> Provide a comprehensive analysis of crime incidents in Los Angeles over the past few years.</li>
        <li><strong>Data Source:</strong> <a href="https://data.lacity.org/">Los Angeles Open Data portal</a></li>
        <li><strong>ETL Tool:</strong> Python</li>
        <li><strong>Visualization Tool:</strong> Tableau (<a href="https://public.tableau.com/views/LACrime2020-2023/LACrime2020-2023?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">Dashboard Link</a>)</li>
    </ul>

<h2>ETL Process</h2>
    <p>The ETL process was built using Python to achieve the following:</p>
    <ol>
        <li><strong>Data Extraction:</strong> Load crime incident data from a public CSV URL.</li>
        <li><strong>Data Transformation:</strong>
            <ul>
                <li>Select relevant columns for analysis.</li>
                <li>Rename columns for clarity and consistency.</li>
                <li>Format the date and time columns for standardized analysis.</li>
                <li>Filter data to include incidents from 2020 to 2023.</li>
            </ul>
        </li>
        <li><strong>Data Loading:</strong> Save the cleaned and filtered dataset to a new CSV file, <code>LA Crime 2020-2023.csv</code>, which was used in the Tableau dashboard.</li>
    </ol>

<h2>Tableau Visualization</h2>
    <p>The cleaned data was visualized using Tableau to uncover insights on:</p>
    <ul>
        <li><strong>Crime Type:</strong> Distribution and frequency of different crime types.</li>
        <li><strong>Location:</strong> Geographical hotspots of criminal activity.</li>
        <li><strong>Time Trends:</strong> Crime patterns by date and time to identify peak periods.</li>
    </ul>

<h3>Dashboard Highlights</h3>
    <p>The interactive Tableau dashboard includes:</p>
    <ul>
        <li><strong>Crime Distribution:</strong> Visual breakdown of various crime types and locations.</li>
        <li><strong>Time Series Analysis:</strong> Monthly and yearly trends to show fluctuations in crime activity over time.</li>
        <li><strong>Geographical Heatmap:</strong> Highlights areas with the highest frequency of crimes.</li>
        <li><strong>Number Details:</strong> Detailed statistics on total crime incidents, most common crime types, and trends by area.</li>
    </ul>
    <p><a href="https://public.tableau.com/views/LACrime2020-2023/LACrime2020-2023?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">View the Tableau Dashboard</a></p>

<h2>Project Files</h2>
    <ul>
        <li><code>etl_script.py</code>: Python script for data extraction, cleaning, and transformation.</li>
        <li><code>LA Crime 2020-2023.csv</code>: Cleaned dataset used for visualization in Tableau.</li>
    </ul>

<h2>Conclusion</h2>
    <p>
        This project illustrates a complete ETL process and data analysis workflow. The final dashboard allows stakeholders to make data-driven decisions by analyzing crime trends, area-specific crime distributions, and key numerical insights into LA’s crime data.
    </p>
