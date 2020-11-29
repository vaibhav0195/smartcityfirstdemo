
Q1 = """SELECT DISTINCT * WHERE { 
               ?Record a <http://example.org/csv/Record>; <http://example.org/csv/taxonname> ?taxonname; 
        <http://example.org/csv/lifestage> ?lifestage
         FILTER(?lifestage = '%s' ) } """%('Adult')
# q1 = """select * from table1 where col=1 """
queryHash = {"Q1":Q1}
