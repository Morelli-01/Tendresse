import hashlib
import json
import random

from django.contrib.auth.models import User

from bolle_vecchie.models import *
from Bolle.models import *
from account.models import Address, Feedback
from cart.models import Cart, Product_in_Cart
from checkout.models import Checkout
from product.models import *
from seller.models import Stats
from app_stats.models import *
# from Bolle.models import Bolla_dst
from django.core import exceptions


def dump_db_users():
    User.objects.all().delete()


# def load_old_db():
#     input = open('dst.json', 'r')
#     input_json = ''
#     for l in input.readlines():
#         input_json += l
#         # print(l)
#     input_json = json.loads(input_json)
#     for dst in input_json:
#         new_dst = Bolla_dst()
#         new_dst.name = dst['Username']
#         new_dst.line1 = dst['Riga1']
#         new_dst.line2 = dst['Riga2']
#         new_dst.city = dst['Citta']
#         new_dst.cap = dst['CAP']
#         new_dst.province = dst['prov']
#         new_dst.country = dst['Paese']
#         new_dst.save()
#         print(new_dst)
#     input.close()

def populate_product():
    Product.objects.all().delete()
    Stats.objects.all().delete()
    Tag.objects.all().delete()
    Checkout.objects.all().delete()
    Cart.objects.all().delete()
    User.objects.all().delete()
    Address.objects.all().delete()
    Feedback.objects.all().delete()

    create_users()
    create_product()
    create_address()
    create_cart()
    create_checkout()
    create_feedbacks()


def create_users():
    names = ['nicola', 'lorenzo', 'francesco', 'federico', 'francesca', 'giulia', 'giorgia', 'viola', 'giacomo', 'luca']
    surnames = ['rossi', 'ferrari', 'russo', 'esposito', 'bianchi', 'romano', 'gallo', 'costa', 'fontana', 'conti']
    base_mail = '@gmail.com'
    sha256_hash = hashlib.sha256()

    rnd = random.Random()
    for i in range(15):
        name = names[rnd.randint(0, 9)].capitalize()
        surname = surnames[rnd.randint(0, 9)].capitalize()
        mail = name.lower() + surname.lower() + base_mail
        byte = mail.encode('utf-8')
        sha256_hash.update(byte)
        psw = sha256_hash.hexdigest()
        try:
            User(first_name=name, last_name=surname, email=mail, username=mail, password=psw).save()
        except:
            continue
    User(first_name='Nicola', last_name='Morelli', email='nicolamorelli@jemore.it', username='nicolamorelli@jemore.it',
         password='sudo', is_staff=True).save()


def create_product():
    tee_title = ['Maglia verde', 'Maglia bianca', 'Maglia nera', 'Maglia viola', 'Maglia grigia']
    hoodie_title = ['Felpa nera', 'Felpa grigia', 'Felpa rossa']
    pant_title = ['Pantaloni beige', 'Pantaloni crema', 'Pantaloni verdi', 'Pantaloni marroni', 'Pantaloni grigi',
                  'Pantaloni neri']
    jacket_title = ['Giacca verde', 'Giacca rossa', 'Giacca marrone/nara', 'Giacca grigia', 'Giacca marrone',
                    'Giacca nera']
    price = [15.50, 14.99, 20.0, 25.90, 30, 40.75, 55.99, 79.90, 90, 150, 250]
    tee_imgs = ['green-tee.webp', 'white_tee.webp', 'black_tee.webp', 'violet_tee.webp', 'grey_tee.webp']
    hoodie_imgs = ['black_hoodie.webp', 'grey_hoodie.webp', 'red_hoodie.webp']
    pants_imgs = ['beige_pants.webp', 'cream_pants.webp', 'green_pants.webp', 'brown_pants.webp', 'grey_pants.webp',
                  'black_pants.webp']
    jacket_imgs = ['green_jacket.webp', 'red_jacket.webp', 'black_brown_jacket.webp', 'grey_jacket.webp',
                   'brown_jacket.webp', 'black_jacket.webp']

    rnd = random.Random()
    tee_tag = Tag.objects.create(name='Maglia', type='cat')
    hoodie_tag = Tag.objects.create(name='Felpa', type='cat')
    pant_tag = Tag.objects.create(name='Pantaloni', type='cat')
    jacket_tag = Tag.objects.create(name='Giacca', type='cat')
    violet_tag = Tag.objects.create(name='Viola', type='col')
    black_tag = Tag.objects.create(name='Nero', type='col')
    white_tag = Tag.objects.create(name='Bianco', type='col')
    red_tag = Tag.objects.create(name='Rosso', type='col')
    blue_tag = Tag.objects.create(name='Blu', type='col')
    beige_tag = Tag.objects.create(name='Beige', type='col')
    brown_tag = Tag.objects.create(name='Marrone', type='col')
    grey_tag = Tag.objects.create(name='Grigio', type='col')
    green_tag = Tag.objects.create(name='Verde', type='col')
    cream_tag = Tag.objects.create(name='Crema', type='col')
    for i in range(len(tee_title)):
        product = Product()
        product.title = tee_title[i]
        product.price = price[rnd.randint(a=0, b=10)]
        product.img1 = tee_imgs[i]
        product.img2 = tee_imgs[rnd.randint(a=0, b=4)]
        product.description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus ducimus esse itaque omnis temporibus. Ab ad aliquid amet consequatur dicta, eum, expedita explicabo facere incidunt ipsum itaque labore mollitia numquam possimus praesentium quam reprehenderit saepe tempora vitae voluptatum. Adipisci, amet aperiam commodi dicta enim libero optio quisquam ratione vero voluptatem!'
        product.available_sizes = json.dumps({
            'sizes': [
                {
                    'size': 'XS',
                    'qty': '100'
                },
                {
                    'size': 'S',
                    'qty': '100'
                },
                {
                    'size': 'M',
                    'qty': '100'
                },
                {
                    'size': 'L',
                    'qty': '100'
                },
                {
                    'size': 'XL',
                    'qty': '100'
                },
            ]
        })
        product.save()

    for i in range(len(hoodie_title)):
        product = Product()
        product.title = hoodie_title[i]
        product.price = price[rnd.randint(a=0, b=10)]
        product.img1 = hoodie_imgs[i]
        product.img2 = tee_imgs[rnd.randint(a=0, b=4)]
        product.description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus ducimus esse itaque omnis temporibus. Ab ad aliquid amet consequatur dicta, eum, expedita explicabo facere incidunt ipsum itaque labore mollitia numquam possimus praesentium quam reprehenderit saepe tempora vitae voluptatum. Adipisci, amet aperiam commodi dicta enim libero optio quisquam ratione vero voluptatem!'
        product.available_sizes = json.dumps({
            'sizes': [
                {
                    'size': 'XS',
                    'qty': '100'
                },
                {
                    'size': 'S',
                    'qty': '100'
                },
                {
                    'size': 'M',
                    'qty': '100'
                },
                {
                    'size': 'L',
                    'qty': '100'
                },
                {
                    'size': 'XL',
                    'qty': '100'
                },
            ]
        })
        product.save()

    for i in range(len(pant_title)):
        product = Product()
        product.title = pant_title[i]
        product.price = price[rnd.randint(a=0, b=10)]
        product.img1 = pants_imgs[i]
        product.img2 = pants_imgs[rnd.randint(a=0, b=5)]
        product.description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus ducimus esse itaque omnis temporibus. Ab ad aliquid amet consequatur dicta, eum, expedita explicabo facere incidunt ipsum itaque labore mollitia numquam possimus praesentium quam reprehenderit saepe tempora vitae voluptatum. Adipisci, amet aperiam commodi dicta enim libero optio quisquam ratione vero voluptatem!'
        product.available_sizes = json.dumps({
            'sizes': [
                {
                    'size': 'XS',
                    'qty': '100'
                },
                {
                    'size': 'S',
                    'qty': '100'
                },
                {
                    'size': 'M',
                    'qty': '100'
                },
                {
                    'size': 'L',
                    'qty': '100'
                },
                {
                    'size': 'XL',
                    'qty': '100'
                },
            ]
        })
        product.save()

    for i in range(len(jacket_title)):
        product = Product()
        product.title = jacket_title[i]
        product.price = price[rnd.randint(a=0, b=10)]
        product.img1 = jacket_imgs[i]
        product.img2 = jacket_imgs[rnd.randint(a=0, b=5)]
        product.description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus ducimus esse itaque omnis temporibus. Ab ad aliquid amet consequatur dicta, eum, expedita explicabo facere incidunt ipsum itaque labore mollitia numquam possimus praesentium quam reprehenderit saepe tempora vitae voluptatum. Adipisci, amet aperiam commodi dicta enim libero optio quisquam ratione vero voluptatem!'
        product.available_sizes = json.dumps({
            'sizes': [
                {
                    'size': 'XS',
                    'qty': '100'
                },
                {
                    'size': 'S',
                    'qty': '100'
                },
                {
                    'size': 'M',
                    'qty': '100'
                },
                {
                    'size': 'L',
                    'qty': '100'
                },
                {
                    'size': 'XL',
                    'qty': '100'
                },
            ]
        })
        product.save()

    for product in Product.objects.all():
        if product.title.__contains__('Maglia'):
            product.category_tags.add(tee_tag)
        elif product.title.__contains__('Pantaloni'):
            product.category_tags.add(pant_tag)
        elif product.title.__contains__('Giacca'):
            product.category_tags.add(jacket_tag)
        elif product.title.__contains__('Felpa'):
            product.category_tags.add(hoodie_tag)

        if product.title.__contains__('verde') or product.title.__contains__('verdi'):
            product.color_tags.add(green_tag)
        if product.title.__contains__('bianca') or product.title.__contains__('bianchi'):
            product.color_tags.add(white_tag)
        if product.title.__contains__('nera') or product.title.__contains__('neri'):
            product.color_tags.add(black_tag)
        if product.title.__contains__('viola'):
            product.color_tags.add(violet_tag)
        if product.title.__contains__('grigia') or product.title.__contains__('grigi'):
            product.color_tags.add(grey_tag)
        if product.title.__contains__('beige'):
            product.color_tags.add(beige_tag)
        if product.title.__contains__('crema'):
            product.color_tags.add(cream_tag)
        if product.title.__contains__('marrone') or product.title.__contains__('marroni'):
            product.color_tags.add(brown_tag)
        if product.title.__contains__('rossa'):
            product.color_tags.add(red_tag)

        product.save()


def create_address():
    vie = ['Via Roma 10', 'Via Giuseppe Garibaldi 10', 'Via Guglielmo Marconi 10', 'Voa Giuseppe Mazzini 10',
           'Via Dante Alighieri 10', 'Via Giuseppe Verdi 10']
    zip = '41012'
    province = 'MO'
    city = 'Carpi'
    rnd = random.Random()
    for u in User.objects.all():
        addr = Address()
        addr.name = u.first_name
        addr.surname = u.last_name
        addr.line1 = vie[rnd.randint(0, 5)]
        addr.zip = zip
        addr.province = province
        addr.city = city
        addr.user_id = u.email
        addr.save()


def create_cart():
    rnd = random.Random()
    sizes = ['XS', 'S', 'M', 'L', 'XL']

    for i in range(50):
        cart = Cart()
        cart.user = User.objects.all()[random.Random().randint(0, (User.objects.all().count() - 1))]
        cart.save()
        products = {}
        for i in range(rnd.randint(1, 5)):
            product = Product.objects.all()[rnd.randint(0, Product.objects.all().count() - 1)]
            qty = rnd.randint(1, 5)
            size = sizes[rnd.randint(0, 4)]
            prod_in_cart = Product_in_Cart()
            prod_in_cart.product = product
            prod_in_cart.size = size
            prod_in_cart.qty = qty
            prod_in_cart.save()
            cart.products_in_cart.add(prod_in_cart)

        cart.checked_out = False
        cart.save()


def create_checkout():
    pp_method = ['pp', 'cc', 'collect']
    ship_method = ['standard', 'collect']
    for cart in Cart.objects.all():
        checkout = Checkout()
        checkout.cart = cart
        checkout.user = cart.user
        checkout.addr = Address.objects.get(user=checkout.user)
        prezzo_finale = 0
        products = checkout.cart.products_in_cart
        for prod_in_cart in products.all():
            prezzo_finale += prod_in_cart.product.price * prod_in_cart.qty
        if checkout.ship_method == 'standard':
            prezzo_finale += 10
        checkout.total_price = float(str(prezzo_finale)[0:5])
        checkout.payment_method = pp_method[random.Random().randint(0, 2)]
        checkout.ship_method = ship_method[random.Random().randint(0, 1)]
        checkout.confirmed = True
        cart.checked_out = True
        decrease_availability(cart)
        cart.save()
        checkout.save()


def decrease_availability(cart: Cart):
    products = cart.products_in_cart.all()
    for prod_in_cart in products:
        qty_to_remove = prod_in_cart.qty
        size_to_remove = prod_in_cart.size

        pid = prod_in_cart.product.pid
        p = Product.objects.get(pid=pid)
        availability = json.loads(p.available_sizes)
        if size_to_remove == 'XS':
            availability['sizes'][0]['qty'] = str(int(availability['sizes'][0]['qty']) - int(qty_to_remove))
        elif size_to_remove == 'S':
            availability['sizes'][1]['qty'] = str(int(availability['sizes'][1]['qty']) - int(qty_to_remove))
        elif size_to_remove == 'M':
            availability['sizes'][2]['qty'] = str(int(availability['sizes'][2]['qty']) - int(qty_to_remove))
        elif size_to_remove == 'L':
            availability['sizes'][3]['qty'] = str(int(availability['sizes'][3]['qty']) - int(qty_to_remove))
        elif size_to_remove == 'XL':
            availability['sizes'][4]['qty'] = str(int(availability['sizes'][4]['qty']) - int(qty_to_remove))

        p.available_sizes = json.dumps(availability)
        p.save()


def create_feedbacks():
    comments_pool = [
        'Non come da descrizione',
        'Prezzo troppo alto',
        'Non sono soddisfatto',
        'Buoni materiali',
        'Ottimi materiali',
        'Ottimo prodotto'
    ]

    for u in User.objects.all():
        for check in Checkout.objects.all().filter(cart__user=u):
            cart = check.cart
            products = cart.products_in_cart.all()
            for prod_in_cart in products:
                feed = Feedback()
                feed.product = Product.objects.get(pid=prod_in_cart.product.pid)
                feed.user = u
                rnd = random.Random().randint(0, 5)
                feed.stars = rnd
                feed.comment = comments_pool[int(rnd)]
                try:
                    feed.save()
                except:
                    continue


def staff_required(func):
    def checK_staff(*args, **kwargs):
        result = func(*args, **kwargs)
        if args[0].user.is_staff:
            return result
        else:
            raise exceptions.PermissionDenied()

    return checK_staff


def logging(func):
    def log(*args, **kwargs):
        result = func(*args, **kwargs)
        request = args[0]
        ip = request.META.get('REMOTE_ADDR')
        if total_log.objects.all().count() == 0:
            new_count = total_log()
            new_count.count = 0
            new_count.save()

        count_log = total_log.objects.all().first()
        count_log.count = count_log.count + 1
        count_log.save()
        if not ip_log.objects.filter(ip=ip).exists():
            new_ip = ip_log()
            new_ip.ip = ip
            new_ip.save()
        return result

    return log


def export_db():
    with open('export_bolle_vecchie_bolle_old.txt', 'w') as file:
        file.write('use tendress;\n')
        for b in bolle_old.objects.all():
            file.write("insert into bolle_vecchie_bolle_old (`numero`,`anno`) values('" + str(b.numero) + "','" + str(
                b.anno) + "');\n")
    with open('export_bolle_bolla_dst.txt', 'w') as file:
        file.write('use tendress;\n')
        for dst in Bolla_dst.objects.all():
            file.write(
                "INSERT INTO Bolle_bolla_dst (`id`,`name`,`line1`,`line2`,`city`,`province`,`zip`,`country`,`alt_dst`) VALUES('" + str(
                    dst.id) + "','" + str(dst.name) + "','" + str(dst.line1) + "','" + str(dst.line2) + "','" + str(
                    dst.city) + "','" + str(dst.province) + "','" + str(dst.zip) + "','" + str(
                    dst.country) + "'," + str(dst.alt_dst) + ");\n")
