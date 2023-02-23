from lxml import etree
from lxml.etree import QName
from xml_generator.commons.address import Address
from xml_generator.commons.partytax import PartyTax
from xml_generator.commons.partylegals import PartyLegals
from xml_generator.commons.contact import Contact
#from pdb import set_trace

class AccountingParties:
    
    def party(NSMAP, invoice, party):

        if(party == 'supplier'):
            root = etree.SubElement(invoice, QName(NSMAP['cac'], 'AccountingSupplierParty'))
        elif(party == 'customer'):
            root = etree.SubElement(invoice, QName(NSMAP['cac'], 'AccountingCustomerParty'))
            
        additionalaccountid = etree.SubElement(root, QName(NSMAP['cbc'], 'AdditionalAccountID'))
        additionalaccountid.text = '1'
        root = AccountingParties.partymeans(NSMAP, root)
        return invoice

    def partymeans(NSMAP, root):
        party = etree.SubElement(root, QName(NSMAP['cac'], 'Party'))
        industryclassificationcode = etree.SubElement(party, QName(NSMAP['cbc'], 'IndustryClassificationCode'))
        industryclassificationcode.text = '6201;6312'
        partyname = etree.SubElement(party, QName(NSMAP['cac'], 'PartyName'))
        name = etree.SubElement(partyname, QName(NSMAP['cbc'], 'Name'))
        name.text = 'FACTURATECH'
        party = Address.address_means(NSMAP, party, 'p_location')
        party = PartyTax.partytax(NSMAP, party)
        party = PartyLegals.partylegalentity(NSMAP, party)
        party = Contact.contact(NSMAP, party)
        
        return party
        
