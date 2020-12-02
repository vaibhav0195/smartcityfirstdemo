# This file contains all the queries we need to execute.
Q1 = """
SELECT DISTINCT ?TaxonName ?TaxonReference ?SiteName ?North ?East  
WHERE{
    ?Record a <http://purl.org/ontology/wo/ToaxonName>; <http://purl.org/ontology/wo/taxonomicName> ?TaxonName; <http://xmlns.com/foaf/0.1/openid> ?TaxonReference;<http://www.w3.org/2003/01/geo/wgs84_pos#lat> ?North; <http://www.w3.org/2003/01/geo/wgs84_pos#long> ?East;
    {
        ?Record <http://www.w3.org/2000/01/rdf-schema#Literal> ?SiteName .
        FILTER regex(str(?SiteName), "%s")
    }
    UNION
	{
    ?Record <http://www.w3.org/2000/01/rdf-schema#comment> ?SiteName .
        FILTER (?SiteName = "%s")
    } 
}LIMIT 1000"""

Q10 = """SELECT ?x ?Occurance ?Record
    WHERE{
    ?Record <http://www.w3.org/2000/01/rdf-schema#comment> ?x;
    FILTER regex(str(?x), "invasive dragonfly")
    BIND(CONCAT("The invasive dragonfly was found on Invasive record")AS ?Occurance)
}"""

Q3 = """
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?TaxonName ?Fortune
WHERE
{
    ?Record a <http://purl.org/ontology/wo/ToaxonName>;<http://purl.org/ontology/wo/taxonomicName> ?TaxonName; <http://example.org/csv/abundance> ?Abundance .
    BIND(if(SUBSTR(?Abundance,0,75) = "<10" || SUBSTR(?Abundance,0,75) = "1"|| SUBSTR(?Abundance,0,75) = "2" || SUBSTR(?Abundance,0,75) = "3" || SUBSTR(?Abundance,0,5) = "4" ||SUBSTR(?Abundance,0,75) = "5"|| SUBSTR(?Abundance,0,75) = "7" || SUBSTR(?Abundance,0,75) = "5-20" || SUBSTR(?Abundance,0,75) = "6" ||SUBSTR(?Abundance,0,75) = "8",
        "Chance of witnessing it again is minimal",
        "Chance of witnessing it again is more")
     AS ?Fortune)
} LIMIT 1000
"""

Q2 = """
SELECT DISTINCT ?TaxonName ?Date
WHERE
{
    ?Record a <http://purl.org/ontology/wo/ToaxonName>;<http://purl.org/ontology/wo/taxonomicName> ?TaxonName; <http://example.org/csv/date> ?time;
    BIND(CONCAT("It was witnessed on ", ?time)AS ?Date)
}ORDER BY ?Date LIMIT 100
"""
Q4 = """
SELECT DISTINCT ?TaxonName ?Lifestage ?AdditionalInformation
WHERE
{
    ?Record a <http://purl.org/ontology/wo/ToaxonName>;<http://purl.org/ontology/wo/taxonomicName> ?TaxonName; <http://www.w3.org/2000/01/rdf-schema#Literal> ?Lifestage;
FILTER regex(str(?Lifestage), "%s") .
     {
        ?Record <http://example.org/csv/additionalinformation> ?AdditionalInformation .
    }
    UNION
	{
    ?Record <http://www.w3.org/2000/01/rdf-schema#comment> ?AdditionalInformation .        
    }

}LIMIT 100"""

Q5 = """
SELECT DISTINCT ?TaxonName ?Researcher
WHERE{
        ?Record <http://purl.org/ontology/wo/taxonomicName> ?TaxonName; 
      {
		?Record <http://xmlns.com/foaf/0.1/givenName> ?Researcher;
        FILTER regex(str(?Researcher), "%s")  
}
UNION{
         ?Record <http://xmlns.com/foaf/0.1/name> ?Researcher
         FILTER regex(str(?Researcher), "%s")
     }
}LIMIT 50"""

Q6 = """
SELECT DISTINCT ?TaxonName ?Gender
WHERE{
        ?Record <http://purl.org/ontology/wo/taxonomicName> ?TaxonName;    
{
    ?Record a <http://xmlns.com/foaf/0.1/Agent>;
	<http://www.w3.org/2000/01/rdf-schema#comment> ?Gender .
	FILTER (?Gender = "%s")
	}
UNION
	{?Record a <http://xmlns.com/foaf/0.1/Agent>;
	<http://www.w3.org/2000/01/rdf-schema#comment> ?Gender .
	FILTER regex(str(?Gender), "%s")
    }
}LIMIT 50
"""
Q7 = """
SELECT DISTINCT ?TaxonName ?TaxonReference ?Habitat
WHERE{
    ?Record a <http://purl.org/ontology/wo/ToaxonName>; <http://xmlns.com/foaf/0.1/openid> ?TaxonReference;{ ?Record <http://example.org/csv/habitatdescription> ?Habitat;} UNION { ?Record <http://www.w3.org/2000/01/rdf-schema#comment> ?Habitat}
    {
        ?Record <http://purl.org/ontology/wo/taxonomicName> ?TaxonName .
        FILTER regex(?TaxonName,"^(%s)") 
    }
}LIMIT 10"""
Q8 = """
"""
# each query is mapped here
queryHash = {"Q2":Q2,"Q3":Q3,"Q10":Q10,"Q1":Q1,"Q4":Q4,"Q5":Q5,"Q6":Q6,"Q7":Q7}
# each query question we need to display to the user.
queryQuestion = [
    "Q1: Give information about Species found in the county = ",
    "Q2: Query over date",
    "Q3: Give the name of speices present in the abundance",
    "Q4: Give the spieces which are at lifestage = ",
    "Q5: Give all the observations made by the researcher =",
    "Q6: Give all the speices for the gender = ",
    "Q7: Query over Scientific Name starting with alphabet =",
    "Q10: Query yes or no whether any buterfly species is invasive to ireland"
]
