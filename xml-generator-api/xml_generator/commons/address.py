"""
    Añade el Nodo PhysicalLocation o RegistrationAddress y todos sus hijos
"""

from lxml import etree
from lxml.etree import QName


class Address:

    def address_means(NSMAP, party, address_type):

        """
            Seleccionando que nodo añadir
        """

        if(address_type == 'p_location'):
            physicallocation = etree.SubElement(party, QName(NSMAP['cac'], 'PhysicalLocation'))
            address = etree.SubElement(physicallocation, QName(NSMAP['cac'], 'Address'))
        elif(address_type == 'r_address'):
            address = etree.SubElement(party, QName(NSMAP['cac'], 'RegistrationAddress'))

        # Adding address data
        id = etree.SubElement(address, QName(NSMAP['cbc'], 'ID'))
        id.text = '05001'

        cityname = etree.SubElement(address, QName(NSMAP['cbc'], 'CityName'))
        cityname.text = 'MEDELLIN'

        countrysubentity = etree.SubElement(address, QName(NSMAP['cbc'], 'CountrySubentity'))
        countrysubentity.text = 'Antioquia'

        countrysubentitycode = etree.SubElement(address, QName(NSMAP['cbc'], 'CountrySubentityCode'))
        countrysubentitycode.text = '05'

        addressline = etree.SubElement(address, QName(NSMAP['cac'], 'AddressLine'))
        line = etree.SubElement(addressline, QName(NSMAP['cbc'], 'Line'))
        line.text = 'CR 43 A 15 SUR 15 ED XEROX OF 802'

        country = etree.SubElement(address, QName(NSMAP['cac'], 'Country'))
        country_code = etree.SubElement(country, QName(NSMAP['cbc'], 'IdentificationCode'))
        country_code.text = 'CO'
        country_name =  etree.SubElement(country, QName(NSMAP['cbc'], 'Name'),
         languageID = 'es'
        )
        country_name.text = 'COLOMBIA'


        return party