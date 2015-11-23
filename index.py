from bottle import route, run, static_file, template, redirect
import mb
import bottle


@route('/ping')
def test():
    return "Ping successful!"


@route('/')
def redirect_to_show_mb():
    redirect('/Mandelbrot/getMandelbrot/512/512/10')


@route('/Mandelbrot/getMandelbrot/<w:int>/<h:int>/<it:int>')
def show_mb(w, h, it):
    wMin, hMin, itMin = 1, 1, 1
    wMax, hMax, itMax = 800, 600, 1000

    if (w < wMin or w > wMax) or (h < hMin or h > hMax) or (it < itMin or it > itMax):
        return template('error.html', w=w, h=h, it=it, wMin=wMin, wMax=wMax, hMin=hMin, hMax=hMax, itMin=itMin, itMax=itMax)
    else:
        mb.create_mb(w, h, it)
        return template('index.html', mb='/mb.png', w=w, h=h, it=it)


@route('/<mb>')
def show_mb(mb):
    return static_file(mb, root=".")


bottle.TEMPLATE_PATH.insert(0, 'home/ec2-user/sys-int-uebungen/sys-int-uebung-1/')
run(server='paste', host='0.0.0.0', port=8080, debug=True)
