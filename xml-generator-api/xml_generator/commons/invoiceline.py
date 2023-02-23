from lxml import etree
from lxml.etree import QName
from xml_generator.commons.taxtotal import Taxtotal
from xml_generator.commons.item import Item
from xml_generator.commons.price import Price
class InvoiceLine:


    def invoiceline(NSMAP, invoice):
        invoiceline = etree.SubElement(invoice, QName(NSMAP['cac'], 'InvoiceLine'))
        child = etree.SubElement(invoiceline, QName(NSMAP['cbc'], 'ID'))
        child.text = ''
        child = etree.SubElement(invoiceline, QName(NSMAP['cbc'], 'Note'))
        child.text = ''
        child = etree.SubElement(invoiceline, QName(NSMAP['cbc'], 'InvoicedQuantity'),
         unitCode = ''                                     
            )
        child.text = ''
        child = etree.SubElement(invoiceline, QName(NSMAP['cbc'], 'LineExtensionAmount'),
         currencyID = ''
            )
        child.text = ''

        Taxtotal.taxtotal(NSMAP, invoiceline)
        Item.item(NSMAP, invoiceline)
        Price.price(NSMAP, invoiceline)
        
        return invoice

        
