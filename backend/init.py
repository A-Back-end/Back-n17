from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from fastapi import FastAPI

app = FastAPI()

engine = create_async_engine('sqlite+aiosqlite:///books.db')


new_sesion = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with get_session() as session:
        yield session
        
class Base(DeclarativeBase):
    pass

class BookModel(Base):
    __tablename__ = "name"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    
@app.post("/setup_database")
async def set_up_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"status": True}


