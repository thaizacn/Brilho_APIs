# repository/BrilhoRepository.py
import psycopg2
from datetime import datetime
from typing import List
from models.CupomModel import CupomRequest

class BrilhoRepository:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="brilho_pime",
            user="brilho",
            password="Zix4CrCjcWanEnbYoQqYBWwjQfepqXn5",
            host="postgres.render.com",
            port="5432"
        )
        self.create_tables()

    def create_tables(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cupons (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(255),
                    codigo VARCHAR(255),
                    data_validade VARCHAR(255),
                    valor INT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cupons_resgatados (
                    id SERIAL PRIMARY KEY,
                    id_cupom INT,
                    data_resgate VARCHAR(255)
                )
            """)

        self.conn.commit()

    def cadastrar_cupom(self, cupom_request: CupomRequest) -> int:
        id_cupom = -1
        with self.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO cupons (nome, codigo, data_validade, valor)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (cupom_request.cupomName, cupom_request.cupomCode, cupom_request.cupomDate, cupom_request.cupomValue))
            id_cupom = cursor.fetchone()[0]

        self.conn.commit()
        return id_cupom

    def resgatar_cupom(self, id_cupom: int):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO cupons_resgatados (id_cupom, data_resgate)
                VALUES (%s, %s)
            """, (id_cupom, datetime.now()))

        self.conn.commit()

    def consultar_cupons(self) -> List[CupomRequest]:
        cupons = []
        
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM cupons")
            for row in cursor.fetchall():
                id, nome, codigo, data_validade, valor = row
                cupom = CupomRequest(
                    id=id,
                    cupomName=nome,
                    cupomCode=codigo,
                    cupomDate=data_validade,
                    cupomValue=valor
                )
                cupons.append(cupom)

        return cupons

    def consultar_cupom_por_id(self, cupom_id: int) -> str:
        cupom_string = None
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM cupons WHERE id = %s", (cupom_id,))
            row = cursor.fetchone()
            if row:
                id, nome, codigo, data_validade, valor = row
                cupom_string = f"ID: {id}, Nome: {nome}, Codigo: {codigo}, Validade: {data_validade}, Valor do cupom: {valor}"

        return cupom_string
