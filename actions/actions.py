from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

class ValidateNumeroProcessoForm(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_numero_processo_form"

  
    def validate_numero_processo(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.replace("-","").isnumeric():
            processo = consulta_processo_api(value)
            if processo == 'Processo não existe':
                dispatcher.utter_message(text=processo)
                dispatcher.utter_message(template="utter_wrong_numero_processo")
                return {"numero_processo": None}
            dispatcher.utter_message(text=processo)
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"numero_processo": value}
        else:
            dispatcher.utter_message(template="utter_wrong_numero_processo")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"numero_processo": None}


from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
class ActionAskContinueNumeroProcesso(Action):

    def name(self) -> Text:
        return "action_ask_continue_numero_processo"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last_intent = tracker.latest_message['intent'].get('name')
        if last_intent == 'afirmar':
            dispatcher.utter_message(text='O que mais deseja saber sobre o processo?')
        else:
            dispatcher.utter_message(text='Ok! o que mais posso fazer por você?')
            return [SlotSet("numero_processo", None)]
        return []


####

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = processo_from_dict(json.loads(json_string))

from typing import List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Assunto:
    assunto: List[str]

    def __init__(self, assunto: List[str]) -> None:
        self.assunto = assunto

    @staticmethod
    def from_dict(obj: Any) -> 'Assunto':
        assert isinstance(obj, dict)
        assunto = from_list(from_str, obj.get("assunto"))
        return Assunto(assunto)

    def to_dict(self) -> dict:
        result: dict = {}
        result["assunto"] = from_list(from_str, self.assunto)
        return result


class OutrasInformacoe:
    serventia: List[str]
    classe: List[str]
    assuntos: List[Assunto]
    valor_causa: List[str]
    valor_condenacao: List[str]
    processo_originario: List[str]
    fase_processual: List[str]
    data_distribuicao: List[str]
    segredo_justica: List[str]
    data_transito_julgado: List[str]
    status: List[str]
    prioridade: List[str]
    efeito_suspensivo: List[str]
    julgado2_grau: List[str]
    custa: List[str]
    penhora_rosto: List[str]
    data_prescricao: List[str]

    def __init__(self, serventia: List[str], classe: List[str], assuntos: List[Assunto], valor_causa: List[str], valor_condenacao: List[str], processo_originario: List[str], fase_processual: List[str], data_distribuicao: List[str], segredo_justica: List[str], data_transito_julgado: List[str], status: List[str], prioridade: List[str], efeito_suspensivo: List[str], julgado2_grau: List[str], custa: List[str], penhora_rosto: List[str], data_prescricao: List[str]) -> None:
        self.serventia = serventia
        self.classe = classe
        self.assuntos = assuntos
        self.valor_causa = valor_causa
        self.valor_condenacao = valor_condenacao
        self.processo_originario = processo_originario
        self.fase_processual = fase_processual
        self.data_distribuicao = data_distribuicao
        self.segredo_justica = segredo_justica
        self.data_transito_julgado = data_transito_julgado
        self.status = status
        self.prioridade = prioridade
        self.efeito_suspensivo = efeito_suspensivo
        self.julgado2_grau = julgado2_grau
        self.custa = custa
        self.penhora_rosto = penhora_rosto
        self.data_prescricao = data_prescricao

    @staticmethod
    def from_dict(obj: Any) -> 'OutrasInformacoe':
        assert isinstance(obj, dict)
        serventia = from_list(from_str, obj.get("serventia"))
        classe = from_list(from_str, obj.get("classe"))
        assuntos = from_list(Assunto.from_dict, obj.get("assuntos"))
        valor_causa = from_list(from_str, obj.get("valorCausa"))
        valor_condenacao = from_list(from_str, obj.get("valorCondenacao"))
        processo_originario = from_list(from_str, obj.get("processoOriginario"))
        fase_processual = from_list(from_str, obj.get("faseProcessual"))
        data_distribuicao = from_list(from_str, obj.get("dataDistribuicao"))
        segredo_justica = from_list(from_str, obj.get("segredoJustica"))
        data_transito_julgado = from_list(from_str, obj.get("dataTransitoJulgado"))
        status = from_list(from_str, obj.get("status"))
        prioridade = from_list(from_str, obj.get("prioridade"))
        efeito_suspensivo = from_list(from_str, obj.get("efeitoSuspensivo"))
        julgado2_grau = from_list(from_str, obj.get("julgado2Grau"))
        custa = from_list(from_str, obj.get("custa"))
        penhora_rosto = from_list(from_str, obj.get("penhoraRosto"))
        data_prescricao = from_list(from_str, obj.get("dataPrescricao"))
        return OutrasInformacoe(serventia, classe, assuntos, valor_causa, valor_condenacao, processo_originario, fase_processual, data_distribuicao, segredo_justica, data_transito_julgado, status, prioridade, efeito_suspensivo, julgado2_grau, custa, penhora_rosto, data_prescricao)

    def to_dict(self) -> dict:
        result: dict = {}
        result["serventia"] = from_list(from_str, self.serventia)
        result["classe"] = from_list(from_str, self.classe)
        result["assuntos"] = from_list(lambda x: to_class(Assunto, x), self.assuntos)
        result["valorCausa"] = from_list(from_str, self.valor_causa)
        result["valorCondenacao"] = from_list(from_str, self.valor_condenacao)
        result["processoOriginario"] = from_list(from_str, self.processo_originario)
        result["faseProcessual"] = from_list(from_str, self.fase_processual)
        result["dataDistribuicao"] = from_list(from_str, self.data_distribuicao)
        result["segredoJustica"] = from_list(from_str, self.segredo_justica)
        result["dataTransitoJulgado"] = from_list(from_str, self.data_transito_julgado)
        result["status"] = from_list(from_str, self.status)
        result["prioridade"] = from_list(from_str, self.prioridade)
        result["efeitoSuspensivo"] = from_list(from_str, self.efeito_suspensivo)
        result["julgado2Grau"] = from_list(from_str, self.julgado2_grau)
        result["custa"] = from_list(from_str, self.custa)
        result["penhoraRosto"] = from_list(from_str, self.penhora_rosto)
        result["dataPrescricao"] = from_list(from_str, self.data_prescricao)
        return result


class ParteParte:
    parte_tipo: List[str]
    nome: List[str]

    def __init__(self, parte_tipo: List[str], nome: List[str]) -> None:
        self.parte_tipo = parte_tipo
        self.nome = nome

    @staticmethod
    def from_dict(obj: Any) -> 'ParteParte':
        assert isinstance(obj, dict)
        parte_tipo = from_list(from_str, obj.get("parteTipo"))
        nome = from_list(from_str, obj.get("nome"))
        return ParteParte(parte_tipo, nome)

    def to_dict(self) -> dict:
        result: dict = {}
        result["parteTipo"] = from_list(from_str, self.parte_tipo)
        result["nome"] = from_list(from_str, self.nome)
        return result


class ProcessoParte:
    parte: List[ParteParte]

    def __init__(self, parte: List[ParteParte]) -> None:
        self.parte = parte

    @staticmethod
    def from_dict(obj: Any) -> 'ProcessoParte':
        assert isinstance(obj, dict)
        parte = from_list(ParteParte.from_dict, obj.get("parte"))
        return ProcessoParte(parte)

    def to_dict(self) -> dict:
        result: dict = {}
        result["parte"] = from_list(lambda x: to_class(ParteParte, x), self.parte)
        return result


class Processo:
    numero: List[str]
    area: List[str]
    numero_tco: List[str]
    id_processo: List[str]
    hash_processo: List[str]
    partes: List[ProcessoParte]
    outras_informacoes: List[OutrasInformacoe]
    header: str

    def __init__(self, numero: List[str], area: List[str], numero_tco: List[str], id_processo: List[int], hash_processo: List[str], partes: List[ProcessoParte], outras_informacoes: List[OutrasInformacoe], header: str) -> None:
        self.numero = numero
        self.area = area
        self.numero_tco = numero_tco
        self.id_processo = id_processo
        self.hash_processo = hash_processo
        self.partes = partes
        self.outras_informacoes = outras_informacoes
        self.header = header

    @staticmethod
    def from_dict(obj: Any) -> 'Processo':
        assert isinstance(obj, dict)
        numero = from_list(from_str, obj.get("numero"))
        area = from_list(from_str, obj.get("area"))
        numero_tco = from_list(from_str, obj.get("numeroTco"))
        id_processo = from_list(from_str, obj.get("idProcesso"))
        hash_processo = from_list(from_str, obj.get("hashProcesso"))
        partes = from_list(ProcessoParte.from_dict, obj.get("partes"))
        outras_informacoes = from_list(OutrasInformacoe.from_dict, obj.get("outrasInformacoes"))
        header = from_str(obj.get("header"))
        return Processo(numero, area, numero_tco, id_processo, hash_processo, partes, outras_informacoes, header)

    def to_dict(self) -> dict:
        result: dict = {}
        result["numero"] = from_list(from_str, self.numero)
        result["area"] = from_list(from_str, self.area)
        result["numeroTco"] = from_list(from_str, self.numero_tco)
        result["idProcesso"] = from_list(lambda x: from_str((lambda x: str(x))(x)), self.id_processo)
        result["hashProcesso"] = from_list(from_str, self.hash_processo)
        result["partes"] = from_list(lambda x: to_class(ProcessoParte, x), self.partes)
        result["outrasInformacoes"] = from_list(lambda x: to_class(OutrasInformacoe, x), self.outras_informacoes)
        result["header"] = from_str(self.header)
        return result


def processo_from_dict(s: Any) -> Processo:
    return Processo.from_dict(s)


def processo_to_dict(x: Processo) -> Any:
    return to_class(Processo, x)

import requests
import json

def consulta_processo_api(numero_processo):
  api_adress = 'https://pjapp.twohills.com.br/api/v1/public/'
  url = api_adress + numero_processo
  json_data = requests.get(url).json()
  if 'error' in json_data:
        return json_data.get("error")
  processo = processo_from_dict(json_data)
  numero = processo.numero[0]
  area = processo.area[0]
  segredo = processo.outras_informacoes[0].segredo_justica[0]
  if segredo == 'Sim':
    return 'Foi encontrado o processo, cujo número é {0} da área {1}, e está sob segredo de justiça a consulta é restrita.'.format(numero,area) 
  polo_ativo = [parte.nome[0] for parte in processo.partes[0].parte if parte.parte_tipo[0] == "Polo Ativo" ]

  polo_passivo = [parte.nome[0] for parte in processo.partes[0].parte if parte.parte_tipo[0] == "Polo Passivo" ][0]
  serventia = processo.outras_informacoes[0].serventia[0]
  classe = processo.outras_informacoes[0].classe[0]
  assuntos = processo.outras_informacoes[0].assuntos[0].assunto[0]
  valor = processo.outras_informacoes[0].valor_causa[0]
  processo_result = 'Foi encontrado o processo {0}, cujo número é {1} da área {2} com valor {3} proposto por {4} contra {5}.'.format(classe,numero,area,valor,polo_ativo,polo_passivo)
  processo_outras_informacoes = 'O processo encontra-se na serventia {0}.'.format(serventia)
  return processo_result + processo_outras_informacoes