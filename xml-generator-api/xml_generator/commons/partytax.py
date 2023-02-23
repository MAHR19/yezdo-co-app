from lxml import etree
from lxml.etree import QName
from xml_generator.commons.address import Address

class PartyTax:
    
    def partytax(NSMAP, party):
        partytaxscheme = etree.SubElement(party, QName(NSMAP['cac'], 'PartyTaxScheme'))
        registration_name = etree.SubElement(partytaxscheme, QName(NSMAP['cbc'], 'RegistrationName'))
        registration_name.text = 'Ftech Colombia S.A.S'
        companyid = etree.SubElement(partytaxscheme, QName(NSMAP['cbc'], 'CompanyID'),
         schemeAgencyID="195",
         schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)",
         schemeID="8",
         schemeName="31"
        )
        companyid.text = '901143311'
        taxlevelcode = etree.SubElement(partytaxscheme, QName(NSMAP['cbc'], 'TaxLevelCode'))
        taxlevelcode.text = 'R-99-PN'
        partytaxscheme = Address.address_means(NSMAP, partytaxscheme, 'r_address')
        taxscheme = etree.SubElement(partytaxscheme, QName(NSMAP['cac'], 'TaxScheme'))
        id = etree.SubElement(taxscheme, QName(NSMAP['cbc'], 'ID'))
        id.text = '1'
        name = etree.SubElement(taxscheme, QName(NSMAP['cbc'], 'Name'))
        name.text = 'IVA'

        return party