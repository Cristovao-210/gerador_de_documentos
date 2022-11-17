import streamlit as st
from functions import*
import datetime as dt

# Criando arquivo do ato
def gerar_ato(info_ato):
  num_ato = info_ato['numero_ato']
  nome_arq_ato = f'ato_{num_ato}.html'
  # capturando ano
  hoje = dt.date.today()
  
  with open(nome_arq_ato, 'w',encoding="UTF-8") as arq_ato:
    arq_ato.write(f'''
    
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ato</title>''')
    arq_ato.write("""
    <style>
        .Texto_Centralizado_Maiusculas {
            text-align: center;
        }

        .Tabela_Texto_Centralizado {
            text-align: center;
        }

        .Texto_Justificado_Recuo_Primeira_Linha {
            text-indent: 50px;
            text-align: justify;
        }

        .Texto_Justificado {
            text-align: justify;
        }

        body {
            /*font-family: 'Times New Roman', Times, serif;*/
            font-size: 12;
        }
    </style>""")
    arq_ato.write(f'''
</head>
<body>
   
 <p class="Texto_Centralizado_Maiusculas"><strong>ATO DO DECANATO DE GESTÃO DE PESSOAS Nº {num_ato} / {hoje.year}</strong></p>
    <table align="center" border="0" cellpadding="20" cellspacing="2" style="width: 98%;">
        <tbody>
            <tr>
                <td style="width: 50%; text-align: left; padding-right: 25px;" valign="middle">&nbsp;&nbsp;</td>
                <td>
                    <p class="Texto_Justificado">Declara&nbsp;vago, por posse em outro cargo inacumulável, o cargo de
                         {info_ato['cargo']} ocupado pelo&nbsp;servidor, {info_ato['nome_servidor']}.
                    </p>
                </td>
            </tr>
            <tr>
                <td style="width: 50%; text-align: left; padding-right: 25px;" valign="middle">&nbsp;</td>
                <td>
                    <p class="Texto_Justificado">&nbsp;</p>
                </td>
            </tr>
        </tbody>
    </table>

    <p class="Texto_Justificado">A DECANA&nbsp;DE GESTÃO DE PESSOAS DA UNIVERSIDADE DE BRASÍLIA, no uso de suas
        atribuições legais, conferidas pelo Ato da Reitoria n. 514, de 27&nbsp;de abril de 2017, publicado
        no&nbsp;<em>DOU</em>&nbsp;n. 81, seção 2, de 28&nbsp;de abril de 2017, e de acordo com a competência que lhe foi
        delegada por meio do Ato da Reitoria n. 304, de 23 de março de 2017, publicado no&nbsp;<em>DOU</em>&nbsp;n. 58,
        seção 2, de 24 de março de 2017&nbsp;e à vista do constante no Processo Eletrônico nº {info_ato['numero_sei']},</p>

    <p class="Texto_Alinhado_Esquerda_Espacamento_Simples">&nbsp;</p>

    <p>&nbsp;</p>

    <p class="Texto_Justificado">R E S O L V E:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    </p>

    <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

    <p>&nbsp;</p>

    <p class="Texto_Justificado_Recuo_Primeira_Linha">Declarar vago, a partir de {info_ato['data_vacancia']}, o cargo de {info_ato['cargo']}, 
        código de vaga nº {info_ato['codigo_vaga']}, ocupado pelo&nbsp;servidor, {info_ato['nome_servidor']}, do
        quadro de pessoal permanente da Fundação Universidade de Brasília, com lotação no {info_ato['lotacao_servidor']}, por posse em outro cargo inacumulável.</p>

    <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>

    <p>&nbsp;</p>

    <p class="Tabela_Texto_Centralizado"><br>
        <span>Maria do Socorro Mendes Gomes<br>
            Decana&nbsp;de Gestão de Pessoas</span>
    </p>    
</body>
</html>
    
''')
    return [arq_ato, nome_arq_ato]
