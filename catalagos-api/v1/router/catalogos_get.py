
from http.client import HTTPException
from fastapi import APIRouter, status, Response, Depends
from sqlalchemy.orm.session import Session
from v1.schemas import catalagosBase
from db.models import * 
from db import db_catalogos 
from db.database import get_db
from typing import List
from enum import Enum   


class tipoCatalogo(Enum):
    """
        Esta clase contiene definiciones de los tipos de catalogos existentes,
        esto para validar al momento de recibir un request si el tipo existe
    """
    AlgoritmoCUDE = 'AlgoritmoCUDE'
    CodigoPrecioReferencia = 'CodigoPrecioReferencia'
    Departamentos = 'Departamentos'
    MediosPago = 'MediosPago'
    RemesaTransporte = 'RemesaTransporte'
    TarifaImpuestoReteIVA = 'TarifaImpuestoReteIVA'
    TipoEntrega = 'TipoEntrega'
    TipoOperacionF = 'TipoOperacionF'
    TipoOrganizacion = 'TipoOrganizacion'
    AlgoritmoCUFE = 'AlgoritmoCUFE'
    ConceptoReclamo = 'ConceptoReclamo'  
    EventoDocumento = 'EventoDocumento'
    Municipio = 'Municipio'
    TarifaImpuestoINC = 'TarifaImpuestoINC'
    TipoAmbiente = 'TipoAmbiente'
    TipoIdFiscal = 'TipoIdFiscal'
    TipoOperacionNC = 'TipoOperacionNC'
    TipoResponsabilidad = 'TipoResponsabilidad'
    CodigoDescuento = 'CodigoDescuento'
    ConceptoNotaCredito = 'ConceptoNotaCredito'
    FormasPago = 'FormasPago'
    Paises = 'Paises'
    TarifaImpuestoIVA = 'TarifaImpuestoIVA'
    TipoCodigoProducto = 'TipoCodigoProducto'
    TipoImpuesto = 'TipoImpuesto'
    TipoOPeracionND = 'TipoOperacionND'
    TipoEventos = 'TiposEventos'
    ConceptoNotaDebito = 'ConceptoNotaDebito'
    LanguageCode = 'LanguageCode'
    RegistroTransporte = 'RegistroTransporte'
    TarifaImpuestoReteFuente = 'TarifaImpuestoReteFuente'
    TipoDocumento = 'TipoDocumento'
    TipoMoneda = 'TipoMoneda'
    TipoOperacionSalud = 'TipoOperacionSalud'
    UnidadesMedida = 'UnidadesMedida'

# Se añade el roter de la api para todo request que comience con /catalogos
router = APIRouter(
    prefix='/catalogos',
    tags=['catalogos']
)

@router.get('/Productos', response_model = list[catalagosBase.ProductoDisplay], status_code = status.HTTP_200_OK)
def get_producto(name : str | None = None ,db : Session=Depends(get_db)):
    return db_catalogos.get_catalog_query(db, name,Producto)
    
@router.get('/CodigoPostal', response_model = list[catalagosBase.catalogoCP], status_code = status.HTTP_200_OK)
def get_codigo(name : str| None = None ,db : Session=Depends(get_db)):
    return db_catalogos.get_catalog_query( db , name , CodigoP)
    
@router.get('/{type}',response_model=list[catalagosBase.catalogoDisplay] ,status_code=status.HTTP_200_OK)
def get_catalogo(type : tipoCatalogo,    name : str| None = None ,db : Session=Depends(get_db)):
    if type in tipoCatalogo:
        if type is tipoCatalogo.AlgoritmoCUDE:
            return db_catalogos.get_full_catalog(db, A_cude)
        if type is tipoCatalogo.CodigoPrecioReferencia:
            return db_catalogos.get_full_catalog(db,C_preRef)
        if type is tipoCatalogo.MediosPago: 
            return db_catalogos.get_catalog_query(db,name,M_pago)
        if type is tipoCatalogo.RemesaTransporte:
            return db_catalogos.get_catalog_query(db,name,Rem_transporte)
        if type is tipoCatalogo.TarifaImpuestoReteIVA:
            return db_catalogos.get_catalog_query(db,name,T_impuestoReteF)
        if type is tipoCatalogo.TipoEntrega:
            return db_catalogos.get_catalog_query(db,name,T_entrega)
        if type is tipoCatalogo.TipoOperacionF:
            return db_catalogos.get_full_catalog(db,T_opeF)
        if type is tipoCatalogo.TipoOrganizacion:
            return db_catalogos.get_catalog_query(db,name,T_orga)
        if type is tipoCatalogo.AlgoritmoCUFE:
            return db_catalogos.get_catalog_query(db,name,A_cufe)
        if type is tipoCatalogo.ConceptoReclamo:
            return db_catalogos.get_catalog_query(db,name,C_reclamo)
        if type is tipoCatalogo.EventoDocumento:
            return db_catalogos.get_catalog_query(db,name,E_documento)
        if type is tipoCatalogo.Municipio:
            return db_catalogos.get_catalog_query(db,name,Municipio)
        if type is tipoCatalogo.TarifaImpuestoINC:
            return db_catalogos.get_catalog_query(db,name,T_impINC)
        if type is tipoCatalogo.TipoAmbiente:
            return db_catalogos.get_catalog_query(db,name,T_ambiente)
        if type is tipoCatalogo.TipoIdFiscal:
            return db_catalogos.get_catalog_query(db,name,T_idFiscal)
        if type is tipoCatalogo.TipoOperacionNC:
            return db_catalogos.get_catalog_query(db,name,T_opeNC)
        if type is tipoCatalogo.TipoResponsabilidad:
            return db_catalogos.get_catalog_query(db,name,T_resp)
        if type is tipoCatalogo.CodigoDescuento:
            return db_catalogos.get_catalog_query(db,name,C_descuento)
        if type is tipoCatalogo.ConceptoNotaCredito:
            return db_catalogos.get_catalog_query(db,name,Concepto_NC)
        if type is tipoCatalogo.FormasPago:
            return db_catalogos.get_full_catalog(db,F_pago)
        if type is tipoCatalogo.Paises:
            return db_catalogos.get_catalog_query(db,name,Paises)
        if type is tipoCatalogo.TarifaImpuestoIVA:
            return db_catalogos.get_catalog_query(db, name, T_impIVA)
        if type is tipoCatalogo.TipoCodigoProducto:
            return db_catalogos.get_catalog_query(db,name,T_codProducto)
        if type is tipoCatalogo.TipoImpuesto:
            return db_catalogos.get_catalog_query(db,name,T_impuesto)
        if type is tipoCatalogo.TipoOPeracionND:
            return db_catalogos.get_catalog_query(db,name,T_operacionND)
        if type is tipoCatalogo.TipoEventos:
            return db_catalogos.get_catalog_query(db,name,T_eventos)
        if type is tipoCatalogo.ConceptoNotaDebito:
            return db_catalogos.get_catalog_query(db,name,Concepto_ND)
        if type is tipoCatalogo.LanguageCode:
            return db_catalogos.get_catalog_query(db,name,LanguageCode)
        if type is tipoCatalogo.RegistroTransporte:
            return db_catalogos.get_catalog_query(db,name,R_transporte)
        if type is tipoCatalogo.TarifaImpuestoReteFuente:
            return db_catalogos.get_catalog_query(db,name,T_impuestoReteF)
        if type is tipoCatalogo.TipoDocumento:
            return db_catalogos.get_catalog_query(db,name,T_documento)
        if type is tipoCatalogo.TipoMoneda:
            return db_catalogos.get_catalog_query(db,name,T_moneda)
        if type is tipoCatalogo.TipoOperacionSalud:
            return db_catalogos.get_catalog_query(db,name,T_opeSalud)
        if type is tipoCatalogo.UnidadesMedida:
            return db_catalogos.get_catalog_query(db,name,U_M)
    if type is not tipoCatalogo:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'not found')



