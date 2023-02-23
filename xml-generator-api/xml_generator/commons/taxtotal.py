from lxml import etree
from lxml.etree import QName


class Taxtotal:

    def taxtotal(NSMAP, invoice):
        tax_total = etree.SubElement(invoice, QName(NSMAP['cac'],'TaxTotal'))
        child =  etree.SubElement(tax_total, QName(NSMAP['cbc'], 'TaxAmount'),
         currencyID = ''
            )
        child.text = ''
        child =  etree.SubElement(tax_total, QName(NSMAP['cbc'], 'RoundingAmount'),
         currencyID = ''                                  
            )
        child.text = ''
        child = etree.SubElement(tax_total, QName(NSMAP['cac'],'TaxSubtotal'))
        child = Taxtotal.tax_subtotal(NSMAP, child)
        return invoice

    def tax_subtotal(NSMAP, taxsubtotal):
        child =  etree.SubElement(taxsubtotal, QName(NSMAP['cbc'], 'TaxableAmount'),
         currencyID = ''                                  
            )
        child.text = ''
        child =  etree.SubElement(taxsubtotal, QName(NSMAP['cbc'], 'TaxAmount'),
            currencyID = ''
            )
        child.text = ''
        taxcategory = etree.SubElement(taxsubtotal, QName(NSMAP['cac'], 'TaxCategory'))
        child = etree.SubElement(taxcategory, QName(NSMAP['cbc'], 'Percent'))
        child.text = ''
        taxscheme = etree.SubElement(taxcategory, QName(NSMAP['cac'], 'TaxScheme'))
        child = etree.SubElement(taxscheme, QName(NSMAP['cbc'], 'ID'))
        child.text = ''
        child = etree.SubElement(taxscheme, QName(NSMAP['cbc'], 'Name'))
        child.text = ''
        return taxsubtotal
