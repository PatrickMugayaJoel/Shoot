from flask import Flask, request, jsonify, abort
from .auth import requires_auth


def create_app(app):

    RECORDS_PER_PAGE = 10

    def paginate(page, records):
        """ return paginated questions """
        start = (page - 1) * RECORDS_PER_PAGE
        end = start + RECORDS_PER_PAGE
        allRecords = []

        for record, category in records:
            record = record.format()
            record['category_id'] = record['category']
            record['category'] = category
            allRecords.append(record)

        current_records = allRecords[start:end]

        return current_records

    @app.route('/')
    def index():
        return "It works"
