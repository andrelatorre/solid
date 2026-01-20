'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''


class TaskHandler:
    def handler(self):
        self.__conect_api()
        self.__create_task()
        self.__update_task()
        self.__remove_task()
        self.__send_notification()
        self.__generate_report()
        self.__send_report()

    def __conect_api(self):
        pass

    def __create_task(self):
        pass

    def __update_task(self):
        pass

    def __remove_task(self):
        pass

    def __send_notification(self):
        pass

    def __generate_report(self):
        pass

    def __send_report(self):
        pass

