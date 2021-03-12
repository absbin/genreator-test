# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4, A5, landscape
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.units import mm, cm
from reportlab.platypus.flowables import PageBreak, Spacer
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from utils.spreadsheettable import SpreadsheetTable
from utils import arabic_reshaper
from utils.bidi.algorithm import get_display

import pymysql


def get_data():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='Abbas',
                           passwd='1234',
                           db='reportlab_db',
                           charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM persons")
    result = cur.fetchall()
    persons = list()
    for record in result:
        persons.append([record[0], record[1], record[2], record[3], record[4]])
    return persons


def replace_digits(num):
    number = {
        0: '۰',
        1: '۱',
        2: '۲',
        3: '۳',
        4: '۴',
        5: '۵',
        6: '۶',
        7: '۷',
        8: '۸',
        9: '۹'
    }
    return number.get(num)


def utf8_converter(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text


def create_pdfdoc(pdfdoc, story):
    MARGIN_SIZE = 5 * mm
    PAGE_SIZE = A4

    pdf_doc = BaseDocTemplate(pdfdoc, pagesize=PAGE_SIZE,
                              leftMargin=MARGIN_SIZE, rightMargin=MARGIN_SIZE,
                              topMargin=MARGIN_SIZE, bottomMargin=MARGIN_SIZE)
    main_frame = Frame(MARGIN_SIZE, MARGIN_SIZE,
                       PAGE_SIZE[0] - 2 *
                       MARGIN_SIZE, PAGE_SIZE[1] - 2 * MARGIN_SIZE,
                       leftPadding=0, rightPadding=0, bottomPadding=0,
                       topPadding=0, id='main_frame')
    main_template = PageTemplate(id='main_template', frames=[main_frame])
    pdf_doc.addPageTemplates([main_template])

    pdf_doc.build(story)


def reporter():
    pdfmetrics.registerFont(TTFont('BNazanin', 'utils\\nazanin.ttf'))
    style_sheet = getSampleStyleSheet()
    style_sheet.add(ParagraphStyle(name='TestStyle', fontName='BNazanin',
                                   fontSize=25, leading=50, alignment=TA_CENTER))
    style_sheet.add(ParagraphStyle(name='PageNum', fontName='BNazanin',
                                   fontSize=15, leading=9, alignment=TA_CENTER))
    style_sheet.add(ParagraphStyle(
        name='TTitle', fontName='BNazanin', fontSize=10, alignment=TA_CENTER))
    style_sheet.add(ParagraphStyle(
        name='About', fontSize=6, alignment=TA_RIGHT))

    table_style = [
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]

    data = []
    person_id = Paragraph(utf8_converter('ردیف'), style_sheet['TTitle'])
    first_name = Paragraph(utf8_converter('نام'), style_sheet['TTitle'])
    last_name = Paragraph(utf8_converter(
        'نام‌خانوادگی'), style_sheet['TTitle'])
    phone_num = Paragraph(utf8_converter('شماره تلفن'), style_sheet['TTitle'])
    user_address = Paragraph(utf8_converter('آدرس'), style_sheet['TTitle'])
    data.append([user_address, phone_num, last_name, first_name, person_id])

    story = []
    title = Paragraph(utf8_converter(
        'گروه فنی مهندسی خورشید ارتباطات'), style_sheet["TestStyle"])
    about = Paragraph(utf8_converter(
        'www.KhorshidErtebatat.com'), style_sheet["About"])

    story.append(title)
    page_number = 1
    overflow = 0

    for person in get_data():

        data.append([Paragraph(utf8_converter(person[4]),
                               style_sheet['TTitle']),
                     Paragraph(get_display(person[3]),
                               style_sheet['TTitle']),
                     Paragraph(utf8_converter(person[2]),
                               style_sheet['TTitle']),
                     Paragraph(utf8_converter(person[1]),
                               style_sheet['TTitle']),
                     Paragraph(str(replace_digits(person[0])),
                               style_sheet['TTitle'])
                     ])

        overflow += 1
        if overflow == 30:
            story.append(Spacer(0, 5 * mm))
            spreadsheet_table = SpreadsheetTable(data, repeatRows=1,
                                                 colWidths=(
                                                     3 * cm, 28 * mm, 25 * mm, 18 * mm, 13 * mm))
            spreadsheet_table.setStyle(table_style)
            story.append(spreadsheet_table)
            story.append(Spacer(0, 5 * mm))
            story.append(Paragraph(
                utf8_converter(str(replace_digits(page_number))
                               ) + utf8_converter('صفحه شماره  '),
                style_sheet['PageNum']))
            story.append(about)
            story.append(PageBreak())
            data = [[user_address, phone_num, last_name, first_name, person_id]]
            overflow = 0
            page_number += 1

    story.append(Spacer(0, 5 * mm))
    spreadsheet_table = SpreadsheetTable(data, repeatRows=1,
                                         colWidths=(
                                             5 * cm, 3 * cm, 4 * cm, 3 * cm, 2 * cm))
    spreadsheet_table.setStyle(table_style)
    story.append(spreadsheet_table)
    story.append(Spacer(0, 5 * mm))
    story.append(Paragraph(
        utf8_converter(str(replace_digits(page_number))) +
        utf8_converter('صفحه شماره  '),
        style_sheet['PageNum']))
    story.append(about)
    create_pdfdoc('report.pdf', story)


def create_pdfdoc(pdfdoc, story):
    MARGIN_SIZE = 5 * mm
    PAGE_SIZE = A4

    pdf_doc = BaseDocTemplate(pdfdoc, pagesize=PAGE_SIZE,
                              leftMargin=MARGIN_SIZE, rightMargin=MARGIN_SIZE,
                              topMargin=MARGIN_SIZE, bottomMargin=MARGIN_SIZE)
    main_frame = Frame(MARGIN_SIZE, MARGIN_SIZE,
                       PAGE_SIZE[0] - 2 *
                       MARGIN_SIZE, PAGE_SIZE[1] - 2 * MARGIN_SIZE,
                       leftPadding=0, rightPadding=0, bottomPadding=0,
                       topPadding=0, id='main_frame')
    main_template = PageTemplate(id='main_template', frames=[main_frame])
    pdf_doc.addPageTemplates([main_template])

    pdf_doc.build(story)


reporter()
print("Your report is ready.")
