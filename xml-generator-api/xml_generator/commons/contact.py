from lxml import etree
from lxml.etree import QName


class Contact:
    
    def contact(NSMAP, party):
        party_contact = etree.SubElement(party, QName(NSMAP['cac'], 'Contact'))
        name = etree.SubElement(party_contact, QName(NSMAP['cbc'], 'Name'))
        name.text = 'Ftech Colombia S.A.S'
        phone = etree.SubElement(party_contact, QName(NSMAP['cbc'], 'Telephone'))
        phone.text = '4531014323'
        email = etree.SubElement(party_contact, QName(NSMAP['cbc'], 'ElectronicMail'))
        email.text = 'prueba@gmail.com'

        return party