from lxml import etree
from lxml.etree import QName

# Add UBLExtensions Node
class UBLExtensions:

    def ublextensions(NSMAP, invoice):
        ublextensions = etree.SubElement(invoice, QName(NSMAP['ext'], 'UBLExtensions'))
        UBLExtensions.ublextension(NSMAP, ublextensions)
    
    # Add UBLExtension Nodes must be two at least
    def ublextension(NSMAP, ublextensions):
        ublextension = etree.SubElement(ublextensions, QName(NSMAP['ext'], 'UBLExtension'))
        ublextension = UBLExtensions.extensioncontent(NSMAP, ublextension)
        return ublextensions

    def extensioncontent(NSMAP, ublextension):
        etree.SubElement(ublextension, QName(NSMAP['ext'], 'ExtensionContent'))
        

