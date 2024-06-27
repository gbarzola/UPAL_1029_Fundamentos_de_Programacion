## Paso a paso

# Aquí están los pasos para obtener tu clave SSH y compartirla con GitHub:

- Abre la terminal en tu PC.
- Verifica si ya tienes claves SSH existentes:
`ls -al ~/.ssh`

- Si no tienes claves, genera una nueva:
`ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"`
(Reemplaza con tu email de GitHub)

- Presiona Enter para aceptar la ubicación predeterminada del archivo.
- Ingresa una contraseña segura cuando se te solicite (opcional pero recomendado).

- Inicia el agente SSH:
`eval "$(ssh-agent -s)"`

- Agrega tu clave privada al agente SSH:
ssh-add ~/.ssh/id_ed25519`

- Copia la clave pública al portapapeles:
`cat ~/.ssh/id_ed25519.pub | clip`
(En algunos sistemas, puedes usar xclip o pbcopy en lugar de clip)
