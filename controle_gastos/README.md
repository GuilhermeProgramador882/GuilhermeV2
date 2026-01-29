# Controle de Gastos 💰

**Aplicação Django para controlar categorias e movimentações financeiras (receitas/despesas).**

---

## ✨ Visão geral

- Projeto criado com Django (app principal: `financeiro`).
- Banco de dados padrão: **SQLite** (arquivo `db.sqlite3`).
- Funcionalidades principais: CRUD de **Categorias** e **Movimentações**, autenticação básica (login/logout) e painel administrativo (`/admin/`).

---

## 🚀 Começando (rápido)

1. Clone o repositório e navegue até a pasta do projeto:

```bash
git clone <repo-url>
cd controle_gastos
```

2. (Opcional, recomendado) Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale dependências:

- Se existir `requirements.txt`:

```bash
pip install -r requirements.txt
```

- Caso não exista, instale o Django e outras libs necessárias manualmente (ex.: `pip install django`) e gere um `requirements.txt` com:

```bash
pip freeze > requirements.txt
```

4. Aplique as migrações e crie um superusuário:

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse a aplicação em `http://127.0.0.1:8000/`.

---

## 🧭 Rotas principais

- Página inicial (lista de movimentações): `/`
- Nova movimentação: `/movimentacao/nova/`
- Editar movimentação: `/movimentacao/editar/<id>/`
- Excluir movimentação: `/movimentacao/excluir/<id>/`

- Lista de categorias: `/categorias/`
- Nova categoria: `/categoria/nova/`
- Editar categoria: `/categoria/editar/<id>/`
- Excluir categoria: `/categoria/excluir/<id>/`

- Login: `/login/`
- Logout: `/logout/`
- Admin Django: `/admin/`

> ⚠️ Observação: as URLs acima são as definidas no `financeiro/urls.py`.

---

## 🧪 Testes

Execute os testes com:

```bash
python manage.py test financeiro
```

---

## 🧩 Estrutura de templates

Os templates estão em `controle_gastos/templates/`, com subpastas como `movimentacoes/` e `categorias/`. O template base é `base.html`.

---

## 💡 Dicas & Observações

- Caso precise configurar variáveis sensíveis (ex.: `SECRET_KEY`, `DEBUG`), configure via variáveis de ambiente ou use um `.env` (não comitar em repositórios públicos).
- O projeto usa SQLite por padrão; para produção, considere migrar para PostgreSQL ou outro SGBD.

---

## 🤝 Contribuição

1. Fork + branch com feature/fix
2. Abra um Pull Request com descrição clara
3. Adicione testes quando aplicável

---

## 📝 Licença

Adicione uma licença (ex.: MIT) se desejar. Atualmente não há arquivo de licença neste repositório.

---

Se quiser, posso também:
- Gerar um `requirements.txt` atual a partir do seu ambiente de desenvolvimento
- Adicionar um `CONTRIBUTING.md` ou `LICENSE`

**Próximo passo sugerido:** verifique se deseja que eu gere o `requirements.txt` automaticamente a partir do seu ambiente ou adicionar um arquivo de licença. 🔧
