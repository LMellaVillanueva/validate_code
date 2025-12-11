# **Validate Code**

Valida o verifica el **código de un producto** con las siguientes reglas:
 `Debe comenzar con exactamente 3 letras o números (\w).`
 `Luego debe tener un guion medio -.`
 `Después del guion debe haber exactamente 4 dígitos (\d).`
 `No puede tener más caracteres.`
 `Debes usar regex y obligatoriamente usar \w y \d.`

---

## **Objetivo**

Este ejercicio forma parte de mis estudios en Python para aplicar mejores prácticas.  
La función `validate(code)` verifica el código de un producto y retorna un **booleano** si se valida o no.

---

## **Ejemplo de uso**

```python
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
# Resultado: True o False
```

## **Cómo ejecutar el script**

1. Clonar este repositorio:
    git clone https://github.com/LMellaVillanueva/validate_code.git

2. Navegar al directorio:
    cd regex1

3. Ejecutar el archivo:
    python regex1.py

---

## **Apuntes de implementación**

- Problema sencillo para entender cómo funciona Regex.
- Solución que valida el patrón que se pide con el código que se envía por parámetro.
