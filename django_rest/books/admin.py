from django.contrib import admin
from .models import Book
from django.core.mail import EmailMessage
from django.conf import settings
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import openpyxl
from django.http import HttpResponse

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'published_date', 'is_active')  # Поля, отображаемые в списке
    list_filter = ('is_active', 'year')  # Фильтры в боковой панели
    search_fields = ('title', 'author')  # Поля для поиска
    ordering = ('-published_date',)  # Сортировка по убыванию даты публикации
    actions = ['export_to_pdf_and_email', 'export_to_xls_and_email']  # Добавляем действия

    def export_to_pdf_and_email(self, request, queryset):
        # Генерация PDF
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        data = [['Title', 'Author', 'Year', 'Published Date', 'Is Active']]  # Заголовки

        # Заполняем данными из queryset
        for book in queryset:
            data.append([
                book.title,
                book.author or 'N/A',
                book.year,
                book.published_date,
                'Yes' if book.is_active else 'No'
            ])

        # Создаём таблицу
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#d5d5d5'),  # Цвет заголовков
            ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), '#f5f5f5'),
            ('GRID', (0, 0), (-1, -1), 1, '#000000'),
        ]))
        elements = [table]
        doc.build(elements)

        # Подготовка email
        subject = 'Books Report (PDF)'
        message = 'В прикреплённом файле находится отчёт по книгам.'
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.DEFAULT_FROM_EMAIL],  # Укажите ваш email
        )
        email.attach('books_report.pdf', buffer.getvalue(), 'application/pdf')
        email.send()

        buffer.close()
        self.message_user(request, "PDF успешно создан и отправлен на email.")

    export_to_pdf_and_email.short_description = "Экспорт в PDF и отправка на email"

    def export_to_xls_and_email(self, request, queryset):
        # Генерация XLS
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Books"
        headers = ['Title', 'Author', 'Year', 'Published Date', 'Is Active']
        ws.append(headers)

        # Заполняем данными из queryset
        for book in queryset:
            ws.append([
                book.title,
                book.author or 'N/A',
                book.year,
                book.published_date,
                'Yes' if book.is_active else 'No'
            ])

        # Сохраняем в буфер
        buffer = BytesIO()
        wb.save(buffer)

        # Подготовка email
        subject = 'Books Report (XLS)'
        message = 'В прикреплённом файле находится отчёт по книгам.'
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['recipient-email@gmail.com'],  # Укажите ваш email
        )
        email.attach('books_report.xlsx', buffer.getvalue(), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        email.send()

        buffer.close()
        self.message_user(request, "XLS успешно создан и отправлен на email.")

    export_to_xls_and_email.short_description = "Экспорт в XLS и отправка на email"