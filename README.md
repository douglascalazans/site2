# Site Lite - Manual de Instruções

## Visão Geral
O Site Lite é uma plataforma para venda de conteúdos digitais (fotos e vídeos) através de pacotes com preços fixos. O sistema permite que os usuários comprem pacotes via PIX e acessem o conteúdo após a confirmação do pagamento.

## Estrutura do Projeto
- **src/**: Código-fonte principal
  - **models/**: Modelos do banco de dados
  - **routes/**: Rotas e controladores
  - **static/**: Arquivos estáticos (CSS, JS, imagens)
  - **templates/**: Templates HTML
  - **main.py**: Ponto de entrada da aplicação

## Funcionalidades Principais
1. **Página Inicial**: Exibe os pacotes disponíveis (PLUS PACK e MASTER PACK)
2. **Sistema de Pagamento**: Integração com PushinPay para processamento de pagamentos PIX
3. **Acesso a Conteúdo**: Liberação automática após confirmação do pagamento
4. **Painel Administrativo**: Gerenciamento de conteúdos e visualização de pagamentos

## Requisitos
- Python 3.8+
- Flask e dependências (listadas em requirements.txt)
- Conexão com internet para integração com PushinPay

## Instalação
1. Clone o repositório ou extraia os arquivos
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Execução
1. Execute o script de inicialização:
   ```
   ./start.sh
   ```
   Ou manualmente:
   ```
   source venv/bin/activate
   cd src
   python main.py
   ```
2. Acesse o site em: http://localhost:5000

## Painel Administrativo
- URL: http://localhost:5000/admin/login
- Usuário padrão: admin
- Senha padrão: admin123

**Importante**: Altere a senha padrão após o primeiro acesso!

## Configuração de Produção
Para implantar em ambiente de produção:
1. Configure um servidor web (Nginx, Apache) como proxy reverso
2. Use Gunicorn ou uWSGI como servidor WSGI
3. Configure variáveis de ambiente para produção
4. Utilize HTTPS para segurança

## Personalização
- Edite os templates em `src/templates/` para alterar a aparência
- Modifique os estilos em `src/static/css/` para personalizar o visual
- Ajuste as configurações em `src/main.py` conforme necessário

## Suporte
Para dúvidas ou problemas, entre em contato com o desenvolvedor.
