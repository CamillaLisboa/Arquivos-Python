from abc import ABC, abstractmethod

class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str) -> None:
        pass


class EmailService(ServicoNotificacao):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[EMAIL] Para: {destinatario} | Msg: {mensagem}")

class SMSService(ServicoNotificacao):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[SMS] Para: {destinatario} | Msg: {mensagem}")

class Notificacao:
    def __init__(self, servico: ServicoNotificacao):
        self.servico = servico

    def enviar(self, destinatario: str, mensagem: str) -> None:
        self.servico.enviar(destinatario, mensagem)


notificador_email = Notificacao(EmailService())
notificador_email.enviar("ana@email.com", "Seu pedido foi aprovado.")

notificador_sms = Notificacao(SMSService())
notificador_sms.enviar("+55 11 99999-0000", "Código: 123456")
