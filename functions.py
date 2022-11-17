import streamlit as st
import datetime


def data_selecionada(dt_select):
    st.write(data_format_br(dt_select))

# função para deixar data recebida no formato necessário
def data_recebida(dt): # recebe uma String
  dia = dt[8:]
  mes = dt[5:7]
  ano = dt[0:4]
  return datetime.date(int(ano), int(mes), int(dia)) # retorna tipo datetime

# função para deixar data recebida no formato usado no Brasil
def data_format_br(dat): # recebe um objeto dateTime
  dia = (f'0{str(dat.day)}' if int(dat.day) < 10 else str(dat.day))
  mes = (f'0{str(dat.month)}' if int(dat.month) < 10 else str(dat.month))
  ano = str(dat.year)
  return f'{dia}/{mes}/{ano}' # retorna uma String

# função para calcular períodos entre uma data e outra
def calcula_perido(d_ini, d_fim):
  dif_periodo = data_recebida(d_fim) - data_recebida(d_ini)
  dias_periodo = (dif_periodo.days + 1)
  return dias_periodo