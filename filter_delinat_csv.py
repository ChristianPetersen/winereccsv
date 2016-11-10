#!/usr/bin/env python
# coding=utf-8
import csv
completecontent = csv.DictReader(open('delinat_raw.csv','rb'), delimiter=";")
g=open('delinat_wein.csv', 'wb') #vielleicht mag auch rb besser passen
# writer = csv.DictWriter(g, ['ProductName', 'ProductPrice', "ProgramId", 'Zupid','MerchantProductNumber','CurrencySymbolOfPrice','ValidFromDate','ProductShortDescription','ProductLongDescription', 'MerchantProductCategory','ZanoxCategoryIds','ImageSmallURL','ImageMediumURL','ProductManufacturerBrand','ZanoxProductLink','DeliveryTime','TermsOfContract','ISBN','ShippingAndHandling','ShippingAndHandlingCost', 'url','ExtraTextOne', 'ExtraTextTwo','ExtraTextThree','post_title'], extrasaction='ignore')

writer = csv.DictWriter(g, ['aff_link','img_medium','name','shortdescription', 'longdescription', 'author', 'outlet', 'price', 'external_id', 'further_keywords','vineyard'], extrasaction='ignore')


writer.writeheader()
outputrow={}
print 'Start Export'
counter=0
for inputrow in completecontent:
		outputrow['aff_link']=inputrow['Deeplink1']
		outputrow['img_medium']=inputrow['Img_url']
		outputrow['name']=inputrow['Title']
		outputrow['shortdescription']=inputrow['Description_Short']
		outputrow['author']='delinat'
		outputrow['outlet']='Delinat Online Shop'
		outputrow['price']=inputrow['DisplayPrice'].split('EUR')[0]
		outputrow['external_id']=inputrow['ArtNumber']
		outputrow['further_keywords']=['Biowein', 'Bio']+[inputrow['ProductCategoryName']]
		writer.writerow(outputrow)
#			print outputrow
		counter+=1
print 'Anzahl Artikel: '+str(counter)
	# else:
	# 	print row['MerchantProductCategory'] + 'faengt nicht mit Wein an'
