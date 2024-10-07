import pandas
from flask import Flask, request, render_template

app = Flask(__name__)

palavras_chave = ["App", "Desenvolvimento", "Mobile", "Aplicativo", "Sistema", "Automatizado", "Impressora", "Jogo"]

@app.route("/", methods=['GET', 'POST'])
def upload():
    linhas = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return "Erro"
        
        file = request.files['file']
        if file.filename == '':
            return "Erro, O objeto é nulo"
        
        if file and file.filename.endswith(".xlsx"):
            planilha = pandas.read_excel(file)
            
            clas = planilha['Classificação']
            title = planilha['Título']
            prop = planilha['Proponente']
            campi = planilha['Campus']
            status = planilha['Status']
            modal = planilha['Modalidade']
            bolsa = planilha['Bolsa']

            linhas = []
            for i in range(planilha.shape[0]):
                
                sn = False
                for palavra in palavras_chave:
                    if palavra.lower() in title[i].lower():
                        sn = True 
                    if sn:
                        linhas.append(f"{clas[i]} - {title[i]} - {prop[i]} - {campi[i]} - {status[i]} - {modal[i]} - {bolsa[i]}")
                        sn = False
                        
        print(linhas)
            
    return render_template('index.html', linhas=linhas)
    
if __name__ == '__main__':
    app.run(debug=True)