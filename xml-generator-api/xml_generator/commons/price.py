from lxml import etree
from lxml.etree import QName


class Price:

    def price(NSMAP, invoiceline):
        price_node = etree.SubElement(invoiceline, QName(NSMAP['cac'], 'Price'))
        child = etree.SubElement(price_node, QName(NSMAP['cbc'], 'PriceAmount'),
         currencyID = ''
            )
        child.text = ''
        child = etree.SubElement(price_node, QName(NSMAP['cbc'], 'BaseQuantity'),
         unitCode = ''                         
            )
        child.text = ''
        return invoiceline