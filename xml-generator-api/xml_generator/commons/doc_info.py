"""
    Añade toda la informacion referente al documento,
    Version de UBL, fechas etc.

"""

from lxml import etree
from lxml.etree import QName

class DocInfo:

    def documentinfo(NSMAP, invoice):
        ublversion = etree.SubElement(invoice, QName(NSMAP['cbc'], 'UBLVersionID'))
        ublversion.text = '2.1'
        customizationid = etree.SubElement(invoice, QName(NSMAP['cbc'], 'CustomizationID'))
        customizationid.text = '10'
        profileid = etree.SubElement(invoice, QName(NSMAP['cbc'], 'ProfileID'))
        profileid.text = 'DIAN 2.1: Factura Electrónica de Venta'
        profile_executionid = etree.SubElement(invoice, QName(NSMAP['cbc'], 'ProfileExecutionID'))
        profile_executionid.text = '1'
        id = etree.SubElement(invoice, QName(NSMAP['cbc'], 'ID'))
        id.text = 'FP140608'
        uuid = etree.SubElement(invoice, QName(NSMAP['cbc'], 'UUID'),
         schemeID = '1',
         schemeName  ='CUFE-SHA384'
        )
        uuid.text = 'e9c437dd3f48e7f8262e3d644770160a4c6730d799b0ba59405c66d483d09b8e8bb5b060eac6f088f9628641bad4c1f8'
        issuedate = etree.SubElement(invoice, QName(NSMAP['cbc'], 'IssueDate'))
        issuedate.text = '2022-04-05'
        issuetime = etree.SubElement(invoice, QName(NSMAP['cbc'], 'IssueTime'))
        issuetime.text = '21:42:24-05:00'
        DueDate = etree.SubElement(invoice, QName(NSMAP['cbc'], 'DueDate'))
        DueDate.text = '2022-04-05'
        invoicetypecode = etree.SubElement(invoice, QName(NSMAP['cbc'], 'InvoiceTypeCode'))
        invoicetypecode.text = '01'
        documentcurrencycode = etree.SubElement(invoice, QName(NSMAP['cbc'], 'DocumentCurrencyCode'))
        documentcurrencycode.text = 'COP'
        linecountnumeric = etree.SubElement(invoice, QName(NSMAP['cbc'], 'LineCountNumeric'))
        linecountnumeric.text = '1'

        return invoice
