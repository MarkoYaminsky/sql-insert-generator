def generate_insert(tables_data: dict):
    data = open('data', 'r').read().split('\n\n')
    complete_inserts = []

    for table, (table_name, table_columns) in zip(data, tables_data.items()):
        data_table = table.split('\n')
        reformated_data = []
        for line in data_table:
            reformated_line = ', '.join(line.split(','))
            reformated_line = f"({reformated_line}),"
            reformated_data.append(reformated_line)
        reformated_data[-1] = reformated_data[-1].rstrip(',') + ';'
        reformated_data = '\n'.join(reformated_data)
        complete_inserts.append(f"INSERT INTO {table_name} ({', '.join(table_columns.split())}) VALUES\n{reformated_data}")
    return complete_inserts


if __name__ == '__main__':
    tables = {
        "country": 'id name',
        "city": 'id name country_id',
        "bank": 'id name country_id',
        "bank_department": 'id street bank_id city_id',
        "client": 'id first_name last_name country_id',
        "client_bank": 'client_id bank_id',
        "person_type": 'id type',
        "bank_account": 'id requisites client_id person_type bank_id',
        "personal_account": 'id bank_id client_id',
        "transaction": 'id sum_in_dollars bank_account_seller_id bank_account_buyer_id'
    }

    print(*generate_insert(tables), sep="\n\n")