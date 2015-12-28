from indeed_api import IndeedClient
import xml.dom.minidom
import xml.etree.ElementTree as ET
from urllib import urlopen
import re
import os
from xmlutils.xml2csv import xml2csv

ext_ip = urlopen('http://icanhazip.com/').read().decode('utf-8')
client = IndeedClient('4336336693914377')


def job_search(query, location, radius, response_format):
        start = 0
        params = {
            'q' : "title: ({})".format(query),
            'l' : "{}".format(location),
            'format': response_format,
            'userip' : '1.2.3.4',
            'radius': radius,
            'start': 0,
            'limit': 25,
            'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
        }

        search_response = client.search(**params)
        results = ET.fromstring(search_response)
        total_results = results.findall('totalresults')[0]
        print ("Total Results = {}".format(total_results.text))

        for x in range(((int(total_results.text) - params['limit']) // params['limit']) + 1):
                params['start'] += 25
                params['limit'] += 25
                new_search_response = client.search(**params)
                new_results = ET.fromstring(new_search_response)

                xml_element_tree = results
                insertion_point = xml_element_tree.findall("./results")[0]
                for record in new_results.iter('results'):
                    insertion_point.extend(record)

        return results

if __name__ == '__main__':
        location = str(raw_input('enter a city. default is "New York, NY"')) or 'New York, NY'
        radius = str(raw_input('enter a radius. default is "2"')) or "2"
        query = str(raw_input('enter search criteria. default is "((Retail) OR (Salespersons))"')) or "((Retail) OR (Salespersons))"
        data = job_search(query, location, radius, 'xml')

        results_name = "location_{}_radius_{}_query_{}".format(location, radius, query)
        results_name = "".join(x for x in results_name if x.isalnum())
        xml_file = "./results/xml/{}.xml".format(results_name)
        csv_file = "./results/csv/{}.csv".format(results_name)

        try:
                os.remove(xml_file)
        except:
                pass

        f = open(xml_file, 'wb')
        f.write(ET.tostring(data))
        f.close()

        try:
                os.remove(csv_file)
        except:
                pass

        converter = xml2csv(xml_file, csv_file, encoding="utf-8")
        converter.convert(tag="result")
        print ("2 files have been generated")
        print ("-----------------------------------------------------------")
        print (csv_file)
        print (xml_file)
