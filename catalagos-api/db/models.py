#####----- Tables models -----#####

#####----- IMPORTS -----#####
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Float

class Producto(Base):
    __tablename__ = 'productos'
    id_producto = Column(Integer,primary_key =True, index=True)
    name = Column(String)
    descripcion = Column(String)
    um = Column(String)
    precio_u = Column(String)

#AlgoritmoteCUDE
class A_cude(Base):
    __tablename__='algoritmocude'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#CodigoPrecioReferencia
class C_preRef(Base):
    __tablename__='codigoprecioreferencia'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#Departamentos
class Departamentos(Base):
    __tablename__='departamentos'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#MediosPago
class M_pago(Base):
    __tablename__='mediospago'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#RemesaTransporte
class Rem_transporte(Base):
    __tablename__='remesatransporte'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TarifaImpuestoReteIVA
class T_impreteIVA(Base):
    __tablename__='tarifaimpuestoreteiva'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoEntrega
class T_entrega(Base):
    __tablename__='tipoentrega'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoOperacionF
class T_opeF(Base):
    __tablename__='tipooperacionf'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoOrganizacion
class T_orga(Base):
    __tablename__='tipoorganizacion'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#AlgoritmoCUFE
class A_cufe(Base):
    __tablename__='algoritmocufe'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#ConceptoReclamo
class C_reclamo(Base):
    __tablename__='conceptoreclamo'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#EventoDocumento
class E_documento(Base):
    __tablename__='eventodocumento'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#Municipio
class Municipio(Base):
    __tablename__='municipio'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TarifaImpuestoINC
class T_impINC(Base):
    __tablename__='tarifaimpuestoinc'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoAmbiente
class T_ambiente(Base):
    __tablename__='tipoambiente'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoIdFiscal
class T_idFiscal(Base):
    __tablename__='tipoidfiscal'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoOperacionNC
class T_opeNC(Base):
    __tablename__='tipoopercionnc'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoResponsabilidad
class T_resp(Base):
    __tablename__='tiporesponsabilidad'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#CodigoDescuento
class C_descuento(Base):
    __tablename__='codigodescuento'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#ConceptoNotaCredito
class Concepto_NC(Base):
    __tablename__='conceptonotacredito'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#FormasPago
class F_pago(Base):
    __tablename__='formaspago'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#Paises
class Paises(Base):
    __tablename__='paises'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TarifaImpuestoIVA
class T_impIVA(Base):
    __tablename__='tarifaimpuestoiva'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoCodigoProducto
class T_codProducto(Base):
    __tablename__='tipocodigoproducto'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoImpuesto
class T_impuesto(Base):
    __tablename__='tipoimpuesto'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoOPeracionND
class T_operacionND(Base):
    __tablename__='tipooperacionnd'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoEventos
class T_eventos(Base):
    __tablename__='tipoeventos'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#CodigoPostal
class CodigoP(Base):
    __tablename__='codigopostal'
    id = Column(Integer,primary_key =True, index=True)
    codigo_departamento = Column(String)
    nombre_departamento = Column(String)
    codigo_municipio = Column(String)
    nombre_municipio = Column(String)
    name = Column(String)
    tipo = Column(String)
#ConceptoNotaDebito
class Concepto_ND(Base):
    __tablename__='conceptonotadebito'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#LanguageCode
class LanguageCode(Base):
    __tablename__='languagecode'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#RegistroTransporte
class R_transporte(Base):
    __tablename__='registrotransporte'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TarifaImpuestoReteFuente
class T_impuestoReteF(Base):
    __tablename__='tarifaimpuestoretefuente'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoDocumento
class T_documento(Base):
    __tablename__='tipodocumento'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoMoneda
class T_moneda(Base):
    __tablename__='tipomoneda'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#TipoOperacionSalud
class T_opeSalud(Base):
    __tablename__='tipooperacionsalud'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
#UnidadesMedida
class U_M(Base):
    __tablename__='unidadesdemedida'
    id = Column(Integer,primary_key =True, index=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)