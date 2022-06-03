import model_rac
import ui
import model_complex
import log

def button():
    v = ui.vid()
    if v == 'rac':
        a = ui.get_rac_chisla()
        b = ui.get_rac_chisla()
        c = ui.get_oper()
        model_rac.chisla(a, b, c)
        res  = model_rac.operation(a, b, c)
        ui.info(res)
        log.primer(a, b, c, res)
    elif v == 'complex':
        a = ui.get_complex_chisla()
        b = ui.get_complex_chisla()
        c = ui.get_oper()
        model_complex.chisla(a, b, c)
        res  = model_complex.operation(a, b, c)
        ui.info(res)
        log.primer(a, b, c, res)
    else: print(f'Wrong type. Try again')
