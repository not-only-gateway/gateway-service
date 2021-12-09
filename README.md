# Gateway

Este serviço fornecer um ponto de acesso/controle para multiplos endpoints e serviços com **APIs REST**.



### Requisitos
1. **service-management** - Utilizado para controle de endpoints. `Obrigatório`
2. **statistics** - Utilizado para registro dos requests. `Opcional`
3. **buffer** - Utilizado para controle dos pacotes de dados (entrada e saida). `Opcional`

### Mapeamento
Por padrão o `gateway` irá consumir **todos** os requests feitos para o endereço de operação.

- A filtragem e autenticação dos requests serão feitas pelo serviço `service-management`.
- Caso disponível, o serviço `statistics` irá consumir os metadados do request como tempo de execução, headers, origem do request e etc.
- Caso disponível, o serviço `buffer` irá consumer os dados enviados no corpo do request e os dados que serão respondidos.

### Configuração do ambiente
É necessária a configuranção de um arquivo `env.py` contendo as seguintes constantes de ambiente:
1. `MQ_HOST`: Host de comunicação com o Message-Broker.
2. `MQ_PORT`: Porta de comunicação com o Message-Broker (padrão *5672*).
3. `MQ_USER`: Nome do usuário do Message-Broker.
4. `MQ_PASSWORD`: Senha do usuário do Message-Broker.
5. `SERVICE_MANAGEMENT_URL`: URL do serviço **service-management**.
6. `SECURE_TOKEN`: Token usado para criptografia da comunicação entre os serviços.

### Deploy
- **Desenvolvimento**: TODO
- **Produção**: TODO