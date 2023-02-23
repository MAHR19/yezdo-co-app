"""
 Esta clase genera el XML de FE de acuerdo a los estandares de la DIAN
 y UBL. 
"""
from lxml import etree
from lxml.etree import QName
from xml_generator.namespaces.namespaces import Namespaces
from xml_generator.commons.ublextensions import UBLExtensions
from xml_generator.commons.doc_info import DocInfo
from xml_generator.commons.parties import AccountingParties
from xml_generator.commons.taxtotal import Taxtotal
from xml_generator.commons.legalmonetarytotal import LegalMonetaryTotal
from xml_generator.commons.invoiceline import InvoiceLine


class FE_generator:

    def __init__(self):
        FE_generator.create_fe()
        
    def create_fe():
        """
            Esta Funcion crea el Nodo padre Invoice y añade los Namespaces que seran necesarios
            para generar este XML.
        """
        # Namespaces mapping
        NSMAP = Namespaces.fe_namespaces()
        # Adding namespace for schemaLocation
        etree.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        # Adding schemaLocation
        schemalocation = QName('{http://www.w3.org/2001/XMLSchema-instance}urn:oasis:names:specification:ubl:schema:xsd:Invoice-2', 'schemaLocation')
        # Invoice Tag
        invoice = etree.Element('Invoice',
        {schemalocation : 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd'},
         nsmap=NSMAP
        )
        # Adding the Child nodes to root node Invoice
        UBLExtensions.ublextensions(NSMAP, invoice)
        DocInfo.documentinfo(NSMAP, invoice)
        AccountingParties.party(NSMAP, invoice, 'supplier')
        AccountingParties.party(NSMAP, invoice, 'customer')
        Taxtotal.taxtotal(NSMAP, invoice)
        LegalMonetaryTotal.legalmonetarytotal(NSMAP, invoice)
        InvoiceLine.invoiceline(NSMAP, invoice)
        
        
        #file = open('/home/mhurtado/Documents/Dian_XML_Generator_PYXB/app/xml_generator/xml/dian_fe.xml', 'w')
        fe = etree.tostring(invoice)
        fe = str(fe, 'UTF-8')
        #print(fe)
        #file.write(fe)
        #file.close()
        return fe

        
#FE_generator = FE_generator()
    
        
    
    
