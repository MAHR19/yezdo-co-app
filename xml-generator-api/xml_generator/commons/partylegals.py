from lxml import etree
from lxml.etree import QName


class PartyLegals:
    
    def partylegalentity(NSMAP, party):
        party_legal_entity = etree.SubElement(party, QName(NSMAP['cac'], 'PartyLegalEntity'))
        registration_name = etree.SubElement(party_legal_entity, QName(NSMAP['cbc'], 'RegistrationName'))
        registration_name.text = 'Ftech Colombia S.A.S'
        companyid = etree.SubElement(party_legal_entity, QName(NSMAP['cbc'], 'CompanyID'),
         schemeAgencyID="195",
         schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)",
         schemeID="8",
         schemeName="31"
        )
        companyid.text = '901143311'
        corporateregistrationscheme = etree.SubElement(party_legal_entity, QName(NSMAP['cac'], 'CorporateRegistrationScheme'))
        id = etree.SubElement(corporateregistrationscheme, QName(NSMAP['cbc'], 'ID'))
        id.text = 'FP'
        name = etree.SubElement(corporateregistrationscheme, QName(NSMAP['cbc'], 'Name'))
        name.text = '2160555112'

        return party