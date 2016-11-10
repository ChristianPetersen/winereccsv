#!/usr/bin/env python
# coding=utf-8
import csv
completecontent = csv.DictReader(open('eworld24_raw.csv','rb'))
g=open('eworld24_wein.csv', 'wb') #vielleicht mag auch rb besser passen
# writer = csv.DictWriter(g, ['ProductName', 'ProductPrice', "ProgramId", 'Zupid','MerchantProductNumber','CurrencySymbolOfPrice','ValidFromDate','ProductShortDescription','ProductLongDescription', 'MerchantProductCategory','ZanoxCategoryIds','ImageSmallURL','ImageMediumURL','ProductManufacturerBrand','ZanoxProductLink','DeliveryTime','TermsOfContract','ISBN','ShippingAndHandling','ShippingAndHandlingCost', 'url','ExtraTextOne', 'ExtraTextTwo','ExtraTextThree','post_title'], extrasaction='ignore')

writer = csv.DictWriter(g, ['aff_link','img_medium','name','shortdescription', 'longdescription', 'author', 'outlet', 'price', 'external_id', 'further_keywords','vineyard'], extrasaction='ignore')


writer.writeheader()
outputrow={}
print 'Start Export'
counter=0
for inputrow in completecontent:
	print 'vorhandene Keys:'
	for i in inputrow.keys():
		print i
	print 'keyliste beendet'
	if "wein" in inputrow['MerchantProductCategory'].lower():
		print inputrow
		outputrow['aff_link']=inputrow['ZanoxProductLink']
		try:
			outputrow['img_medium']=inputrow['ImageLargeURL']
		except:
			try:
				outputrow['img_medium']=inputrow['ImageMediumURL']
			except:
				outputrow['img_medium']=inputrow['ImageSmallURL']				
		outputrow['name']=inputrow['ProductName']
		outputrow['shortdescription']=inputrow['ProductShortDescription']
		outputrow['author']='eworld24'
		outputrow['outlet']='eworld24 Online Shop'
		outputrow['price']=inputrow['ProductPrice']
		if 'Zupid' in inputrow.keys():
			outputrow['external_id']=inputrow['Zupid']
		outputrow['further_keywords']=[inputrow['MerchantProductCategory']]
		outputrow['further_keywords'].append(inputrow['ProductManufacturerBrand'])
		writer.writerow(outputrow)
#			print outputrow
		counter+=1
print 'Anzahl Artikel: '+str(counter)
	# else:
	# 	print row['MerchantProductCategory'] + 'faengt nicht mit Wein an'
