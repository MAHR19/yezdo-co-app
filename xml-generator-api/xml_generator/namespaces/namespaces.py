
class Namespaces:

    #NAMESPACES######################################################
    #############################################################################
    empty = "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
    cac = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
    cbc = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
    ccts = "urn:un:unece:uncefact:documentation:2"
    ds = "http://www.w3.org/2000/09/xmldsig#"
    ext = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
    sts = "dian:gov:co:facturaelectronica:Structures-2-1"
    qdt = "urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2"
    sac = "urn:sunat:names:specification:ubl:peru:schema:xsd:SunatAggregateComponents-1"
    udt = "urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2"
    #############################################################################

 
    def fe_namespaces():
        fe_nsmap = {None:Namespaces.empty, 'cac':Namespaces.cac, 'cbc':Namespaces.cbc,
        'ccts':Namespaces.ccts, 'ds':Namespaces.ds, 'ext':Namespaces.ext, 'sts':Namespaces.sts,
        'qdt':Namespaces.qdt, 'sac':Namespaces.sac, 'udt':Namespaces.udt,
        }
        return fe_nsmap
        

    def dnote_namespaces():
        pass