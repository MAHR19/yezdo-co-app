from lxml import etree
import sys

def generate_cfdi():
    
    etree.register_namespace('cfdi', 'http://www.sat.gob.mx/cfd/4')
    qname = etree.QName({"http://www.w3.org/2001/XMLSchema-instance", "schemaLocation" })
    etree.register_namespace('implocal', 'http://www.sat.gob.mx/implocal')
    comprobante_40 = etree.Element('{http://www.sat.gob.mx/cfd/4}Comprobante',
    {qname:  "http://www.sat.gob.mx/cfd/4 http://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd http://www.sat.gob.mx/implocal http://www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xsd"},
     Version="4.0",
     Folio="167ABC",
     Fecha='2022-12-29T14:39:35',
     SubTotal="2000.00",
     Sello="",
     NoCertificado='30001000000400002434',
     Certificado='',
     Total="2320.00" ,
     Moneda="MXN",
     Exportacion="01",
     TipoDeComprobante="I" ,
     LugarExpedicion="58000",
     CondicionesDePago="CONDICIONES",
     FormaPago="01",
     Serie="A",
     MetodoPago="PUE",
    )

    etree.SubElement(comprobante_40,'{http://www.sat.gob.mx/cfd/4}Emisor',
     Rfc="EKU9003173C9" ,
     Nombre="ESCUELA KEMPER URGATE",
     RegimenFiscal="601"
    )

    etree.SubElement(comprobante_40,'{http://www.sat.gob.mx/cfd/4}Receptor',
     Rfc="AABF800614HI0" ,
     Nombre="FELIX MANUEL ANDRADE BALLADO",
     RegimenFiscalReceptor="616",
     DomicilioFiscalReceptor= '86400',
     UsoCFDI = 'S01'
    )

    conceptos = etree.SubElement(comprobante_40, '{http://www.sat.gob.mx/cfd/4}Conceptos')

    concepto = etree.SubElement(conceptos, '{http://www.sat.gob.mx/cfd/4}Concepto',
     Cantidad="1.00", 
     ClaveProdServ="90111503", 
     ClaveUnidad="ROM", 
     Descripcion="HABITACION",
     ObjetoImp="02", 
     Importe="2000.00", 
     NoIdentificacion="001", 
     Unidad="ROM", 
     ValorUnitario="2000.00"
     )

    impuestos_concepto = etree.SubElement(concepto, '{http://www.sat.gob.mx/cfd/4}Impuestos')
    impuestos_traslados = etree.SubElement(impuestos_concepto, '{http://www.sat.gob.mx/cfd/4}Traslados',)

    etree.SubElement(impuestos_traslados,'{http://www.sat.gob.mx/cfd/4}Traslado',
     Base="2000.00", 
     Importe="320.00", 
     Impuesto="002", 
     TasaOCuota="0.160000", 
     TipoFactor="Tasa"
    )


    impuestos_comprobante = etree.SubElement(comprobante_40,'{http://www.sat.gob.mx/cfd/4}Impuestos',
     TotalImpuestosTrasladados="320.00"
    )

    impuestos_traslados = etree.SubElement(impuestos_comprobante, '{http://www.sat.gob.mx/cfd/4}Traslados',)

    etree.SubElement(impuestos_traslados,'{http://www.sat.gob.mx/cfd/4}Traslado',
     Base="2000.00",
     Importe="320.00", 
     Impuesto="002", 
     TasaOCuota="0.160000", 
     TipoFactor="Tasa"
    )

    complemento = etree.SubElement(comprobante_40, '{http://www.sat.gob.mx/cfd/4}Complemento')

    impuestos_locales = etree.SubElement(complemento, '{http://www.sat.gob.mx/implocal}ImpuestosLocales',
     version = '1.0',
     TotaldeRetenciones = '0.0',
     TotaldeTraslados = '80.00'
    )

    traslados_locales = etree.SubElement(impuestos_locales, '{http://www.sat.gob.mx/implocal}TrasladosLocales',
     ImpLocTrasladado = 'ISH',
     TasadeTraslado = '4.00',
     Importe = '80.00'
                                         )



    file = open('/home/mhurtado/Documents/Dian_XML_Generator_PYXB/xml/ish.xml', 'a')
    file.truncate(0)
    cfdi = etree.tostring(comprobante_40)
    cfdi = str(cfdi, 'UTF-8')
    print(cfdi)
    file.write(cfdi)
    file.close()



generate_cfdi()