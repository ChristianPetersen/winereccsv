#!/usr/bin/env python
# coding=utf-8
import csv
completecontent = csv.DictReader(open('lidl_raw.csv','rb'))
g=open('lidl_wein.csv', 'wb') #vielleicht mag auch rb besser passen
# writer = csv.DictWriter(g, ['ProductName', 'ProductPrice', "ProgramId", 'Zupid','MerchantProductNumber','CurrencySymbolOfPrice','ValidFromDate','ProductShortDescription','ProductLongDescription', 'MerchantProductCategory','ZanoxCategoryIds','ImageSmallURL','ImageMediumURL','ProductManufacturerBrand','ZanoxProductLink','DeliveryTime','TermsOfContract','ISBN','ShippingAndHandling','ShippingAndHandlingCost', 'url','ExtraTextOne', 'ExtraTextTwo','ExtraTextThree','post_title'], extrasaction='ignore')

writer = csv.DictWriter(g, ['aff_link','img_medium','name','shortdescription', 'longdescription', 'author', 'outlet', 'price', 'external_id', 'further_keywords','vineyard'], extrasaction='ignore')


writer.writeheader()
outputrow={}
print 'Start Export'
counter=0
for inputrow in completecontent:
		if inputrow['MerchantProductCategory'] in ['Weißwein', 'Rotwein', 'Roséwein', 'Champagner, Sekt / Secco']:
			print inputrow
			outputrow['aff_link']=inputrow['ZanoxProductLink']
			outputrow['img_medium']=inputrow['ImageLargeURL']
			outputrow['name']=inputrow['ProductName']
			outputrow['shortdescription']=inputrow['ProductShortDescription']+' ('+inputrow['MerchantProductCategory']+') '+inputrow['ExtraTextOne']+' '+inputrow['ExtraTextTwo']+' '+inputrow['ExtraTextThree']
			outputrow['author']='lidl'
			outputrow['outlet']='Lidl Online Shop'
			outputrow['price']=inputrow['ProductPrice']
			outputrow['external_id']=inputrow['Zupid']
			outputrow['further_keywords']=inputrow['MerchantProductCategory']
			writer.writerow(outputrow)
#			print outputrow
			counter+=1
print 'Anzahl Artikel: '+str(counter)
	# else:
	# 	print row['MerchantProductCategory'] + 'faengt nicht mit Wein an'
