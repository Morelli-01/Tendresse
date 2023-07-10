import json
import re
import subprocess


# Comando PowerShell da eseguire
class Bolla:
    def __init__(self, data, descrizioni, qta, um, note, lavorazione, respSpedizione, dataTrasp, aspetto, dst,
                 sameAddress, dst2, number, year):
        self.data = data
        self.descrizioni = descrizioni
        self.qta = qta
        self.um = um
        self.note = note
        self.lavorazione = lavorazione
        self.respSpedizione = respSpedizione
        self.dataTrasp = dataTrasp
        self.aspetto = aspetto
        self.dst = dst
        self.sameAddress = sameAddress
        self.dst2 = dst2
        self.number = number
        self.year = year

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Dst:

    def __init__(self, usr, riga1, riga2, citta, cap, prov, paese):
        self.usr = usr
        self.riga1 = riga1
        self.riga2 = riga2
        self.citta = citta
        self.cap = cap
        self.prov = prov
        self.paese = paese


def exec_cmd(args):
    # powershell_command = 'java.exe -jar ..\BollaDrawer\\target\BollaDrawer-1.0-SNAPSHOT.jar ' + args  # Puoi sostituire questo con il comando desiderato
    cmd_command = 'java -jar ..\BollaDrawer\\target\BollaDrawer-1.0-SNAPSHOT.jar ' + args
    print(cmd_command)
    # print("\"{'data':'27/02/2023','descrizioni':['Filato Composizioni Diverse'],'qta':['10'],'um':['Kg'],'note':['---'],'lavorazione':'Taglio','respSpedizione':'mittente','dataTrasp':'27/02/2023','aspetto':'visibile','dst':{'usr':'Nicola Morelli','riga1':'Via Giacomo Puccini 22','riga2':'','citta':'Carpi','cap':'41012','prov':'MO','paese':'Italia'},'sameAddress':true,'dst2':[null], 'year':'2023', 'number':'57'}\"")
    try:
        # Esegui il comando CMD
        result = subprocess.run(cmd_command, capture_output=True, text=True, check=True, shell=True)

        # Stampa l'output
        print("Output CMD:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("Errore durante l'esecuzione del comando CMD:")
        print(e)
        print(e.stderr)


if __name__ == '__main__':
    dst = Dst('Nicola Morelli', 'via Giacomo Puccini 22', '', 'Carpi', '41012', 'MO', 'Italia')
    descrizione = ['Filato Composizioni Diverse']
    qta = ['100']
    um = ['Kg']
    note = ['---']
    dst2 = [None]
    bolla = Bolla('27/07/2023', descrizione, qta, um, note, 'Taglio', 'Mittente', '27/07/2023', 'visibile', dst, True,
                  dst2, '58', '2023')
    args = bolla.to_json()
    args = args.replace('\"', "'")
    args = args.replace(' ', '')
    args = "\"" + args + "\""
    print(args)
    exec_cmd(args)
    # print(str(bolla.to_json()))
    # print(re.fullmatch('^note.*', 'no1erbhsr') is not None)

