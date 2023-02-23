from lxml import etree
from lxml.etree import QName

class Item:

    def item(NSMAP, invoiceline):
        item = etree.SubElement(invoiceline, QName(NSMAP['cac'], 'Item'))
        child = etree.SubElement(item, QName(NSMAP['cbc'], 'Description'))
        child.text = ''
        standard_item_identification = etree.SubElement(item, QName(NSMAP['cac'], 'StandardItemIdentification'))
        child = etree.SubElement(standard_item_identification, QName(NSMAP['cbc'], 'ID'),
         schemeAgencyID="", 
         schemeID="999",
         schemeName="Estándar de adopción del contribuyente"                     
            )
        child.text = ''