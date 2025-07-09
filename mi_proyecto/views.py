from django.http import HttpResponse 

def saludo(request):
    return HttpResponse("Hola Mundo!")

def calcular_edad(request, anio):
    edad_actual = 19 
    periodo = anio - 2025
    edad_futura = edad_actual  + periodo
    documento = "El año  %s tendra  %s años "%(anio, edad_futura)
    return HttpResponse(documento)

def calcular_edad_pasada(request, anio):
    edad_actual = 18
    periodo = anio - 2025
    edad_pasada = edad_actual  + periodo
    documento = "El año  %s tendra  %s años "%(anio, edad_pasada)
    return HttpResponse(documento)

def suma_numeros(request, n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    resultado = "El resultado de sumar %i y %i es: %i" % (n1, n2, n1 + n2)
    return HttpResponse(resultado.encode('utf-8'))


def division_exacta(request, numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    resultado = "El resultado de dividir %i por %i es: %i" % (numero1, numero2, numero1 / numero2)
    return HttpResponse(resultado.encode('utf-8'))

def division_decimal(request, numero1, numero2):
    numero1 = float(numero1)
    numero2 = float(numero2)
    resultado = "El resultado de dividir %i por %i es: %i" % (numero1, numero2, numero1 / numero2)
    return HttpResponse(resultado.encode('utf-8'))


def multiplicacion(request, numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    resultado = "El resultado de multiplicar %i por %i es: %i" % (numero1, numero2, numero1 * numero2)
    return HttpResponse(resultado.encode('utf-8'))

def resta(request, numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    resultado = "El resultado de restar %i de %i es: %i" % (numero1, numero2, numero1 - numero2)
    return HttpResponse(resultado.encode('utf-8'))



def informacion(request):
    return HttpResponse("Información del Proyecto -")

def mi_informacion(request):
    return HttpResponse("Hola me llamo Carlos Andres y Soy programador FullStack  ")

def mi_nacionalidad(request):
    return HttpResponse("Soy de colombia nacido en bogota me puedes encontrar actualmente en pereira")

def edad(request):
    return HttpResponse("Mi edad: 19 años")

def mi_hobby(request):
    return HttpResponse("Mi hobby es programar y aprender nuevas tecnologias")

def mi_telefono(request):
    return HttpResponse("Mi telefono es: 3001234567")

def mi_email(request):
    return HttpResponse("Mi email es: carlosandres@gmail.com")

def mi_redes_sociales(request):     
    return HttpResponse("Mi redes sociales: https://www.instagram.com/andres_rys14/")

def mi_curso(request):
    return HttpResponse("Curso de Django - Python - Bases de Datos - HTML - CSS - JavaScript - Git y GitHub")   

def mi_blog(request):
    return HttpResponse("Mi blog: https://carlosandres.com/blog")

def mi_github(request):
    return HttpResponse("Mi github: https://github.com/carlo1404")


# html 
def pagina_html(request):
    html = """
    <html>
        <head>
            <title>Mi Página HTML</title>
        </head>
        <body>
            <h1>Bienvenido a mi página HTML</h1>
            <p>Esta es una página de ejemplo de como usar django</p>
            <video width="320" height="240" controls>
                <source src="https://www.example.com/video.mp4" type="video/mp4">
                Tu navegador no soporta el elemento de video.
        </body>
    </html>
    """
    return HttpResponse(html)

def video_example(request): 
    video = """
        <html>
            <head>
                <title>Mi Video</title>
            </head>
            <body>
                <h1>Bienvenido a mi video</h1> 
                <p> Aca puedes subir tu cancion </p>
                <video width="320" height="240" controls>
                    <source src="https://www.example.com/video.mp4" type="video/mp4">
                    Tu navegador no soporta el elemento de video.
                </video>
            </body>

        </html>
        """
    return HttpResponse(video)

# pratica de header de una pagina 

def header(request):
    header = """
        <html>
            <head>
                <title>Mi Header</title>
                <style>
                    .header{
                    background-color: #ECFBEB;
                    padding: 20px;
                    text-align: center;
                    border-radius: 3px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.2);
                    }
                    h1{
                        color: #000;
                    }
                </style>
            </head>
            <body>
                <header class="header"> 
                    <h1> Bienvenido me llamo andres </h1>
                </header>
            </body> 
        </html>
        """
    return HttpResponse(header)


# Practica de un main en django

def main(request):
    main = """
        <html>
            <head>
                <title>Mi Main</title>
                <style>
                    .main{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background-color: #FFA23E;
                    padding: 20px;
                    text-align: center;
                    border-radius: 3px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.2);
                    width:240px;
                    height:240px;
                    margin:auto;
                    position: relative;
                    top:50%;
                    transform: translateY(-50%);
                    }
                    h1{
                        color: #000;
                        font-size: 30px;
                        font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <main class="main"> 
                    <h1> Bienvenido me llamo andres </h1>
                </main>
            </body> 
        </html>
        """
    return HttpResponse(main)


# section en django con html 

def section(request):
    section = """
        <html>
            <head>
                <title>Mi Section</title>
                <style>
                    .section{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background-color: #FFA23E;
                    padding: 20px;
                    text-align: center;
                    border-radius: 3px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.2);
                    width:240px;
                    height:240px;
                    margin:auto;
                    position: relative;
                    top:50%;
                    transform: translateY(-50%);
                    gap: 20px;
                    }
                    .section__cajauno, .section__cajados {
                        background-color: #63BDED;
                        padding: 20px;
                        text-align: center;
                        border-radius: 3px;
                        box-shadow: 0 0 10px rgba(0,0,0,0.2);
                        margin: 10px;
                    }

                </style>
            </head>
            <body>
                <section class="section"> 
                    <div class="section__cajauno">
                        <h1> Bienvenido me llamo andres </h1>
                        <img src="https://www.example.com/image.jpg" alt="Imagen de ejemplo" width="200" height="200">
                        <p>Esta es una página de ejemplo de como usar django</p>
                    </div>
                    <div class="section__cajados">
                        <h1> Bienvenido me llamo andres </h1>
                        <img src="https://www.example.com/image.jpg" alt="Imagen de ejemplo" width="200" height="200">
                        <p>Esta es una página de ejemplo de como usar django</p>
                    </div>
                </section>
            </body> 
        </html>
        """
    return HttpResponse(section)


# ejemplo de un formulario

def formulario(request):
    formulario = """
        <html>
            <head>
                <title>Mi Formulario</title>
                <style>
                    body {
                        background-color: #EBFFCF;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }

                    form {
                        background-color: #ffffff;
                        padding: 30px 40px;
                        border-radius: 12px;
                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        width: 300px;
                    }

                    label {
                        display: block;
                        margin-bottom: 6px;
                        font-weight: 600;
                        color: #333;
                    }

                    input[type="text"],
                    input[type="email"] {
                        width: 100%;
                        padding: 10px 12px;
                        margin-bottom: 20px;
                        border: 1px solid #ccc;
                        border-radius: 8px;
                        font-size: 14px;
                        transition: border-color 0.3s;
                    }

                    input[type="text"]:focus,
                    input[type="email"]:focus {
                        border-color: #007bff;
                        outline: none;
                    }

                    input[type="submit"] {
                        background-color: #007bff;
                        color: white;
                        border: none;
                        padding: 10px 18px;
                        border-radius: 8px;
                        font-size: 14px;
                        cursor: pointer;
                        width: 100%;
                        transition: background-color 0.3s;
                    }

                    input[type="submit"]:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <form action="/mi_formulario/" method="post">
                    <label for="nombre">Nombre:</label><br>
                    <input type="text" id="nombre" name="nombre"><br>
                    <label for="email">Email:</label><br>
                    <input type="email" id="email" name="email"><br>
                    <input type="submit" value="Enviar">
                </form>
            </body>
        </html>
    """
    return HttpResponse(formulario)


# Un registro de usuario en django
def registro(request):
    registro = """
        <html>
            <head>
                <title>Mi Formulario de Registro</title>
                <style>
                    body {
                        background-color: #f2f2f2; /* fondo general suave */
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }

                    form {
                        background-color: #ffffff; /* fondo blanco para el formulario */
                        padding: 30px 40px;
                        border-radius: 15px;
                        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                        width: 100%;
                        max-width: 400px;
                    }

                    label {
                        display: block;
                        margin-bottom: 8px;
                        font-weight: 600;
                        color: #333;
                    }

                    input[type="text"],
                    input[type="password"],
                    input[type="email"] {
                        width: 100%;
                        padding: 10px 12px;
                        margin-bottom: 20px;
                        border: 1px solid #ccc;
                        border-radius: 8px;
                        box-sizing: border-box;
                        transition: border-color 0.3s;
                        font-size: 14px;
                    }

                    input[type="text"]:focus,
                    input[type="password"]:focus,
                    input[type="email"]:focus {
                        border-color: #007bff;
                        outline: none;
                    }

                    input[type="submit"] {
                        background-color: #007bff;
                        color: #fff;
                        border: none;
                        padding: 12px 20px;
                        border-radius: 8px;
                        cursor: pointer;
                        font-size: 16px;
                        font-weight: bold;
                        width: 100%;
                        transition: background-color 0.3s ease;
                    }

                    input[type="submit"]:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <form action="/mi_formulario/" method="post">
                    <label for="nombre">Nombre:</label><br>
                    <input type="text" id="nombre" name="nombre" placeholder="Escribe tu nombre"><br>
                    <label for="apellido">Apellido:</label><br>
                    <input type="text" id="apellido" name="apellido" placeholder="Escribe tu apellido"><br>
                    <label for ="contraseña">Contraseña:</label><br>
                    <input type="password" id="contraseña" name="contraseña" placeholder="Escribe tu contraseña"><br>
                    <label for="email">Email:</label><br>
                    <input type="email" id="email" name="email" placeholder="Escribe tu email"><br>
                    <input type="submit" value="Enviar">
                </form>
            </body>
        </html>
    """
    return HttpResponse(registro)

# iconos con saludo en django

def iconos_saludo(request):
    iconos = """
        <html>
            <head>
                <title>Mi Iconos</title>
                <style>
                    body {
                        background-color: #EBFFCF;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }

                    .iconos {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        gap: 20px;
                    }

                    .iconos__caja {
                        background-color: #ffffff;
                        padding: 20px;
                        border-radius: 12px;
                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        width: 200px;
                        height: 200px;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        gap: 10px;
                    }

                    .iconos__caja img {
                        width: 100px;
                        height: 100px;
                    }

                    .iconos__caja p {
                        font-size: 14px;
                        color: #333;
                    }
                </style>
                
            </head>
            <body>
                <div class="iconos">
                    <div class="iconos__caja">
                        <img src="https://www.example.com/image.jpg" alt="Imagen de ejemplo" width="100" height="100">
                        <p>Imagen 1</p>
                    </div>
                    <div class="iconos__caja">
                        <img src="https://www.example.com/image.jpg" alt="Imagen de ejemplo" width="100" height="100">
                        <p>Imagen 2</p>
                    </div>
                    <div class="iconos__caja">
                        <img src="https://www.example.com/image.jpg" alt="Imagen de ejemplo" width="100" height="100">
                        <p>Imagen 3</p>
                    </div>
                </div>
            </body>
        </html>
    """
    return HttpResponse(iconos)


# login

def login(request):
    login = """
        <html>
            <head>
                <title>Mi Login</title>
                <style>
                    body {
                        background-color: #f2f2f2; /* fondo general suave */
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }

                    form {
                        background-color: #ffffff; /* fondo blanco para el formulario */
                        padding: 30px 40px;
                        border-radius: 15px;
                        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                        width: 100%;
                        max-width: 400px;
                    }

                    label {
                        display: block;
                        margin-bottom: 8px;
                        font-weight: 600;
                        color: #333;
                    }

                    input[type="text"],
                    input[type="password"] {
                        width: 100%;
                        padding: 10px 12px;
                        margin-bottom: 20px;
                        border: 1px solid #ccc;
                        border-radius: 8px;
                        box-sizing: border-box;
                        transition: border-color 0.3s;
                        font-size: 14px;
                    }

                    input[type="text"]:focus,
                    input[type="password"]:focus {
                        border-color: #007bff;
                        outline: none;
                    }

                    input[type="submit"] {
                        background-color: #007bff;
                        color: #fff;
                        border: none;
                        padding: 12px 20px;
                        border-radius: 8px;
                        cursor: pointer;
                        font-size: 16px;
                        font-weight: bold;
                        width: 100%;
                        transition: background-color 0.3s ease;
                    }

                    input[type="submit"]:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <form action="/mi_formulario/" method="post">
                    <label for="usuario">Usuario:</label><br>
                    <input type="text" id="usuario" name="usuario" placeholder="Escribe tu usuario"><br>
                    <label for ="contraseña">Contraseña:</label><br>
                    <input type="password" id="contraseña" name="contraseña" placeholder="Escribe tu contraseña"><br>
                    <input type="submit" value="Enviar">
                    <p>No tienes cuenta? <a href="/registro/">Registrate</a></p>
                </form>
            </body>
        </html>
    """
    return HttpResponse(login)


# Un coro de una cancion de regueeton de blessd
def coro_blessd(request):
        coro = """
        <html>
            <head>
                <title>Coro de Blessd</title>
                <style>
                    body {
                        background-color: #71CBFF;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }
                    h1 {
                        color: #000;
                        text-align: center;
                        font-size: 42px;
                        font-weight: bold;
                        margin-bottom: 15px;
                    }
                    p {
                        color: #fff;
                        text-align: center;
                        font-size: 16px;
                    }

                </style>
            </head>
            <body>
                <div>
                    <h1>Un coro de Blessd</h1>
                    <p>Te dejo un coro de una cancion de regueeton de Blessd:</p>
                    <p>"Aunque esto me dolio mi amor le digo que su a dios duele ojala que otro me la consuele"</p
                </div>
            </body>
        </html>
        """
        return HttpResponse(coro)

# cancion completa de blessd piponas remix con video 

def cancion_blessd_piponas(request):
    cancion = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Canción - Blessd Piponas</title>
        <style>
            body {
                background-color: #71CBFF;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
            }

            .container {
                max-width: 960px;
                margin: 40px auto;
                padding: 20px;
            }

            h1 {
                text-align: center;
                color: #000;
                margin-bottom: 30px;
                font-size: 40px;
            }

            .video {
                width: 100%;
                aspect-ratio: 16 / 9;
                margin-bottom: 40px;
                box-shadow: 0 0 15px rgba(0,0,0,0.3);
                border-radius: 10px;
                overflow: hidden;
            }

            .video iframe {
                width: 100%;
                height: 100%;
                border: 0;
            }

            .letter {
                background-color: #63BDED;
                color: #fff;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.3);
                line-height: 1.7;
                font-size: 16px;
                white-space: pre-wrap;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Mi Canción - Blessd Piponas</h1>

            <div class="video">
                <iframe src="https://www.youtube.com/embed/Dftj21lTUIA" allowfullscreen></iframe>
            </div>

                <div class="letter">
                    <p>Ey, Kris R, dígalo pues, mi parcero, ¿sí sabe?
                        Bendito, mi socio, del Barrio Antioquia
                        Y si esa chimba no cree en el amor a primera vista
                        Le llegamos de nuevo pa que nos vuelva a ver
                        ¿Y si el novio está muy aleteao?
                        Lo prendemo'a candela, ¿sí sabe, mi parcero? Ja, ja
                        Ensaciada con la trama y el phillie
                        Me robo a la más chimba, como a 18, Krilin
                        Modelando Philipp Plein, chillin'
                        Ya subimos de nivel, easy
                        No me fronteen de reloj, si la hora no la da un Richard Mille
                        Ahora toas son modelito' argentina', parecen a TINI
                        Mi amor, yo fumo bareta
                        Pero si vamos pa'l PH ya le traigo su tussi
                        Pa que modele empelota' en el jacuzzi
                        Ay, qué delicia, rosadita esa pussy
                        En la gaveta 'el BM, tranquilo, yo guardo la Uzi
                        Ella es un ángel, pero encima'e mí se convierte en una hija de Lucifer
                        Tenga treinta mil pa que se compre el placer
                        Le cambié su Mazda 3 por un Mercedes Benz
                        Pida Louis Vuitton, qué pereza Guess
                        Usted no está con cualquiera, mami, usted está con Blessd
                        Usted, Blessd, no es ejemplo de nada
                        Qué hijueputa risa
                        Ahora mantengo parchaíto en Ibiza
                        Tranquilito con la playa y la brisa
                        Me voy pa Italia si me antojo de pizza
                        La K, El Bendito
                        Un pasecito, socio
                        Las putas son fina', exótica', sí
                        Igual que la bareta que meto, la bareta
                        De chirreo en una finca pepas y color psicodélico
                        Estoy to tapeto (toy todo farruco)
                        Rodeado de firmas de culos famosos (ah, sí)
                        Que vos solo ves por Instagram (por ahí, por el IG)
                        Más de una que, por sople, lo dan
                        Y no den lora en redes o la aprieto
                        Nítido, sisa, el color me baja y me ensistema
                        Que los míos se disfruten lo que yo he lograo
                        Hoy me voy de putas con el Emma (ah, sí)
                        Que hoy ando en un Spark, mi niño, todo Chevrolet y pusieron mis tema'
                        El que iba piloteando me dijo: "Socio, este quema sus temas", gas
                        Parece farmacia y rivo, trama, clona y metadona (hay de todito, papi)
                        Si me parcho en el Lleras
                        Lo' gringos se vuelven locos con el polvo madona
                        Vi la' lucas después de subir las aguas
                        Y no es Fiji, mi so, son pipona'
                        Nos fuimos de misión, Blessd dejó la G-Wa y sacamo La Ratona
                        No lo pienso y sin pensar la parto
                        Y ahora sí que le invierto sin asco
                        En una pieza exótica, en El Pobla le di
                        De deslactosada la harto (subimo de level)
                        Y otra llegó a cobrarlo, las huevas, no pago
                        A mí tiene que dármela free (no sea grosera)
                        Si no afloja rápido y está muy picada la chimba, me abro de aquí
                        Sí, señor, lucas hay pa gastar y ni crea, no gasto en bobadas
                        Menos en estas groupies que se pegan pa'l VIP
                        Llegan todas sopladas (ta bueno, sí)
                        Tantos pases que ni los del Barça, la puse a chupar y no fue banca
                        Le puse a cachos a la polla que tenía como WestCOL a Aida
                        Y estoy todo farro
                        Pero si hay clientes pa repartirle, me avisa
                        Que ya llegó el encargo, esos gringos abusan, se meten la mera sopliza
                        Y la otra toda sana, sisa, y con ese manto a misa
                        ¿Que porque no le pagué tragos, ni botella, no le iba a dar su pipisa?
                        Siguen comprando ropa barata
                        Y fumando bareta jaraca (ay, qué grosero)
                        Que ya también le estamos cobrando lo' shows
                        Y lo que soplan por la ñata, lo matamos a fierro o a lata
                        Y después nos vamo de piñata (de farra)
                        Y mantengo en la trampa siempre cuatro ojo'
                        Aquí no entran... (shh-shh-shh)
                        Sisa, yeah
                        La K, eh
                        El remix, ja, ja, ja, ja
                        Ave María, mi amor, ¿sí sabe?
                        El Bendito del Barrio Antioquia, mi cielo (El Bendito)
                        Y se diga lo que son (cuénteme, ah)
                        Mentira' no, el trap de Colombia, papi, le hablo claro
                        Y que se pique (con Kris R, ¿sí sabe?, mi parcero)
                        Ah, no
                        Dime, JB (usted no es ejemplo de nada)
                        Dime, Franky
                        Monja
                        Y que la pongan como quiera', gonorrea
                        Y que le ponga el chaleco de foto'e perfil, ja, ja, ja
                        Esa cogida de nosotro no la está aguantando nadie, qué calor
                        ¿Ah, no?, no estamo escopeando ni puta mierda, pa hablarle claro
                        Este es el remix, ah
                        </p>
                    </div>
            </body>
        </html>
        """
    return HttpResponse(cancion)

# ahora une ejemplo usando loader

def loader_example(request):
    from django.template import loader
    template = loader.get_template('mi_template.html')
    context = {
        'title': 'Mi Página con Loader',
        'message': 'Este es un ejemplo de cómo usar el loader de Django.',
    }
    return HttpResponse(template.render(context, request))

# ahora usando render
def render_example(request):
    from django.shortcuts import render
    context = {
        'title': 'Mi Página con Render',
        'message': 'Este es un ejemplo de cómo usar el render de Django.',
    }
    return render(request, 'mi_template.html', context)

# ahora usando render_to_response
def render_to_response_example(request):
    from django.shortcuts import render_to_response
    context = {
        'title': 'Mi Página con Render To Response',
        'message': 'Este es un ejemplo de cómo usar el render_to_response de Django.',
    }
    return render_to_response('mi_template.html', context, request)


