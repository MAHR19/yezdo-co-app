from lxml import etree
from lxml.etree import QName


class LegalMonetaryTotal:


    def legalmonetarytotal(NSMAP, invoice):
        legal_monetary_total = etree.SubElement(invoice, QName(NSMAP['cac'], 'LegalMonetaryTotal'))
        child = etree.SubElement(legal_monetary_total, QName(NSMAP['cbc'], 'LineExtensionAmount'),
         currencyID = ''                                  
                                 )
        child.text = ''
        child = etree.SubElement(legal_monetary_total, QName(NSMAP['cbc'], 'TaxExclusiveAmount'),
         currencyID = ''                                                                          
                                 )
        child.text = ''
        child = etree.SubElement(legal_monetary_total, QName(NSMAP['cbc'], 'TaxInclusiveAmount'),
         currencyID = ''                                  
                                                                  
                                 )
        child.text = ''
        child = etree.SubElement(legal_monetary_total, QName(NSMAP['cbc'], 'PrepaidAmount'),
         currencyID = ''                                  
                                                                  
                                 )
        child.text = ''
        child = etree.SubElement(legal_monetary_total, QName(NSMAP['cbc'], 'PayableAmount'),
         currencyID = ''                                  
                                                                  
                                 )
        child.text = ''
        return invoice
