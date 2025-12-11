"""
Ejercicio tipo Codewars (6–7 kyu) usando regex, obligatorio usar \d y \w.

Ejercicio: Validar código de producto
Debes crear una función que valide un código de producto con las siguientes reglas:

-Debe comenzar con exactamente 3 letras o números (\w).
-Luego debe tener un guion medio -.
-Después del guion debe haber exactamente 4 dígitos (\d).
-No puede tener más caracteres.
-Debes usar regex y obligatoriamente usar \w y \d.

Ejemplos válidos

"A1b-1234"
"abc-0001"
"Z9X-9999"

Ejemplos inválidos

"AB-1234" (solo 2 caracteres antes del guion)
"abcd-1234" (4 caracteres antes del guion)
"abc-12a4" (contiene una letra donde deben ir dígitos)
"abc-12345" (demasiados dígitos)
"abc-123" (faltan dígitos)
"ab-12" (demasiado corto)

Tu función debe:

Retornar True si coincide con el patrón.
Retornar False si no.
"""

from os import system
if system("clear") != 0: system("cls")

import re
def validate(code):
    pattern = r'\w{3}-\d{4}'
    match_code = re.fullmatch(pattern, code)
    return True if match_code else False

validate("A1b-1234")
validate("abc-0001")
validate("Z9X-9999")
validate("AB-1234")
validate("abcd-1234")
validate("abc-12a4")
validate("abc-12345")
validate("abc-123")
validate("ab-12")