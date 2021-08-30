import eel
import sqlite3
from json import dumps
from datetime import date
from jinja2 import Template

conn = sqlite3.connect('stock.db')
cur = conn.cursor()


def initDB():
    with open('Schemas.sql', 'r') as sql:
        script = sql.read()
    try:
        cur.executescript(script)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


initDB()


eel.init('web')


@eel.expose
def getItems():
    try:
        cur.execute('SELECT name from Items ORDER BY name')
        items = [item for (item, ) in cur.fetchall()]
        return dumps(items)
    except Exception as e:
        print(f'getItems: {e}')
        return []


@eel.expose
def getInvoices(category):
    try:
        cur.execute(
            'SELECT date, invoice, item, quantity from {} WHERE substr(date, -4, 4)=?'.format(category), (str(date.today().year), ))
        invoices = [{"date": date, "invoiceID": invoiceID, "item": item, "quantity": quantity}
                    for (date, invoiceID, item, quantity) in cur.fetchall()]
        return dumps(invoices)
    except Exception as e:
        print(f'getInvoices: {e}')
        return []


@eel.expose
def insertItem(item):
    try:
        cur.execute("INSERT INTO Items ('name') VALUES (?)", (item, ))
        conn.commit()
        return 200
    except Exception as e:
        print(f'insertItem: {e}')
        conn.rollback()
        return 0


@eel.expose
def insertInvoice(invoice, category):
    try:
        cur.execute("INSERT INTO {} ('date', 'invoice', 'item', 'quantity') VALUES (?, ?, ?, ?)".format(category),
                    (invoice['date'], invoice['invoiceID'], invoice['item'], invoice['quantity']))
        conn.commit()
        return 200
    except Exception as e:
        print(f'insertInvoice: {e}')
        conn.rollback()
        return 0


@eel.expose
def generateReport(category, period, filter, invoices, isSummary):
    try:
        with open('report.html', 'r') as file:
            html = file.read()
        report = Template(html).render(category=category, period=period,
                                       filter=filter, invoices=invoices, isSummary=isSummary)
        return report
    except Exception as e:
        print(f'generateReport: {e}')
        return ''


eel.start('index.html', cmdline_args=[
          '--start-fullscreen'])
