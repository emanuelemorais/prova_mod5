from backend.models.base import Base
from sqlalchemy import Column, Integer, String

class Game(Base):
    __tablename__ = "game"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    platform = Column(String)
    price = Column(String)
    amount = Column(Integer)
    
    def __repr__(self) -> str:
        return f"id={self.id}, name={self.name}, platform={self.platform}, price={self.price}, amount={self.amount}"
    
    
# - Crie os modelos necessários para representar um jogo eletrônico (Nome do Jogo, Plataforma, Preço e Quantidade). Utilize os tipos de dados necessários para realizar essa criação.