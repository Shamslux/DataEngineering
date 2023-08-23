<a href="https://www.goodreads.com/user/show/50697219-jo-o-paulo-m-ller-mamede">
    <img src="https://img.shields.io/badge/Goodreads-372213?style=for-the-badge&logo=goodreads&logoColor=white" alt="Goodreads Badge"/>
  </a>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Brazilian_flag_icon_round.svg/1200px-Brazilian_flag_icon_round.svg.png" width=25 height=25/>
  
## Índice

Verifique as três barras laterais exibidas no canto superior direito da tela. Clique lá e o GitHub já produz um ToC automaticamente para este arquivo MD.

# AWS Certified Cloud Practitioner Exam Guide por Rajesh Daswani

<img src="https://m.media-amazon.com/images/I/41I21sU8XsL.jpg"/>

# Resumo

Portanto, este é outro resumo de outro livro útil. Estou retomando, pois em breve farei o exame mais básico da AWS em setembro.

# CAPÍTULO 1 - O QUE É COMPUTAÇÃO EM NUVEM

## INTRODUÇÃO

A computação em nuvem tornou-se o método preferido para a criação de aplicativos de TI em todo o mundo. Antigamente, as empresas tinham que investir em sua própria infraestrutura e contratar desenvolvedores, o que era caro e inflexível. No entanto, com a computação em nuvem, as empresas podem economizar dinheiro, ser mais inovadoras e dimensionar facilmente suas soluções. Os profissionais de TI precisam aprender sobre computação em nuvem para se manterem relevantes e fornecerem soluções eficientes. A computação em nuvem oferece vários modelos e opções de implantação, e entendê-los é crucial para criar estratégias de nuvem eficazes. A virtualização desempenha um papel vital em tornar a computação em nuvem possível.

Na computação em nuvem, as empresas acessam serviços de TI como capacidade de computação, armazenamento e software de provedores terceirizados pela Internet. Em vez de gerenciar sua própria infraestrutura, eles podem alugar esses serviços de provedores como Amazon Web Services (AWS). A computação em nuvem já existe há algum tempo, com exemplos iniciais como o Hotmail. Hoje, a AWS é um importante provedor de nuvem que oferece soluções de TI econômicas, seguras e confiáveis, tornando-se uma escolha popular para muitas empresas e startups.

## AS SEIS VANTAGENS DA COMPUTAÇÃO EM NUVEM

A computação em nuvem oferece várias vantagens para as empresas:

1. **Economia de custos**: Em vez de investir antecipadamente em infraestrutura cara, as empresas podem pagar apenas pelos recursos que realmente usam, reduzindo as despesas de capital. Essa flexibilidade permite que as empresas aloquem recursos para outras áreas importantes.

2. **Economias de escala**: provedores de nuvem como a AWS podem oferecer preços mais baixos porque hospedam infraestrutura para muitos clientes e têm maior poder de compra.

3. **Planejamento de capacidade aprimorado**: a computação em nuvem permite que as empresas escalem sua infraestrutura automaticamente com base na demanda, evitando superprovisionamento ou subprovisionamento de recursos.

4. **Mais velocidade e agilidade**: fornecedores de nuvem como a AWS permitem o provisionamento rápido de recursos de TI, permitindo que as organizações lancem aplicativos mais rapidamente e respondam às necessidades em constante mudança com mais eficiência.

5. **Custos de data center reduzidos**: Ao usar serviços de nuvem, as empresas podem eliminar a necessidade de gerenciar e manter data centers físicos, economizando em imóveis, energia e despesas de manutenção.

6. **Alcance global**: os provedores de nuvem têm data centers em várias regiões do mundo, permitindo que as empresas ofereçam experiências de baixa latência aos clientes e garantam a conformidade com os regulamentos de dados.

No geral, a adoção de tecnologias de nuvem ajuda as empresas a otimizar custos, melhorar a escalabilidade e responder rapidamente às demandas do mercado.

## BÁSICO SOBRE VIRTUALIZAÇÃO

A virtualização é uma tecnologia central que revolucionou a computação em nuvem, dando origem a grandes provedores de nuvem como AWS, Microsoft Azure e Google Cloud Platform. Ele permite uma ampla gama de serviços com alta disponibilidade, elasticidade e rápido provisionamento para os clientes.

Antes da virtualização, a terceirização da infraestrutura envolvia longos tempos de espera para configurar servidores físicos, incluindo CPUs, memória e armazenamento, juntamente com um sistema operacional e aplicativos.

Avanços na tecnologia de hardware levaram servidores físicos poderosos a permanecerem subutilizados. No entanto, a engenharia de software consome com eficiência recursos de hardware para alimentar aplicativos.

A virtualização permite que um único servidor físico seja emulado como vários componentes virtuais, implantados como máquinas virtuais (VMs) com seus próprios sistemas operacionais e aplicativos.

Um hypervisor atua como uma ponte entre o hardware físico e as VMs, permitindo acesso controlado e isolamento de recursos. Ele esculpe representações virtualizadas de hardware físico em componentes menores apresentados como VMs.

A principal vantagem da virtualização é o provisionamento rápido de recursos. A emulação de hardware existente com software reduz significativamente os prazos de provisionamento de servidores virtuais, armazenamento ou ambientes de rede.

## VIRTUALIZAÇÃO VS COMPUTAÇÃO EM NUVEM

A virtualização é uma tecnologia que permite serviços de computação em nuvem, mas não é a própria computação em nuvem. Provedores de nuvem como a AWS utilizam a virtualização para oferecer ferramentas de gerenciamento de autoatendimento para provisionar recursos de infraestrutura virtualizada. Essas ferramentas incluem um console de gerenciamento, CLI e APIs, permitindo que os clientes provisionem facilmente servidores, rede, armazenamento e bancos de dados sem esperar pela configuração manual.

Os provedores de computação em nuvem aproveitam a virtualização e as modernas tecnologias de hardware para fornecer recursos de computação compartilhados e produtos de software como serviço (SaaS) pela Internet. Eles oferecem elasticidade, automação, escalabilidade e alta disponibilidade em um modelo de preço pré-pago, tornando seus serviços acessíveis a uma ampla gama de clientes em todo o mundo.

## EXPLORANDO MODELOS DE COMPUTAÇÃO EM NUVEM

A computação em nuvem oferece às empresas a oportunidade de mudar de aplicativos de gerenciamento e hospedagem, com provedores que oferecem aplicativos convencionais e aplicativos de linha de negócios (LOB) sob medida como serviços completos. Diferentes modelos de nuvem atendem a necessidades específicas:

1. **Infraestrutura como serviço (IaaS)**: oferece flexibilidade ao dar aos clientes acesso para configurar componentes de infraestrutura virtualizada, como rede, armazenamento e serviços de computação, semelhante à propriedade da infraestrutura física.

2. **Plataforma como serviço (PaaS)**: concentra-se no desenvolvimento de aplicativos, eliminando o fardo de gerenciar a infraestrutura subjacente. O provedor fornece a infraestrutura necessária, com alguma flexibilidade na configuração.

3.**Software como Serviço (SaaS)**: Os aplicativos são totalmente hospedados e gerenciados pelo provedor, eliminando a necessidade de configuração de infraestrutura física. Os usuários acessam os aplicativos pela Internet e a configuração ainda pode ser necessária para atender a requisitos comerciais específicos.

## ENTENDENDO OS MODELOS DE IMPLANTAÇÃO DA NUVEM

Ao implantar serviços em nuvem para uma organização, três modelos principais de implantação devem ser considerados:

1. **Nuvem pública**: as empresas consomem serviços de TI de fornecedores terceirizados, como a AWS, pela Internet. Ele oferece uma vasta gama de serviços com preços pré-pagos, permitindo gerenciamento de custos e flexibilidade. A nuvem pública fornece recursos de autoatendimento e acesso a consoles de gerenciamento, APIs e interfaces de linha de comando.

2. **Nuvem Privada**: A organização adquire, instala, configura e gerencia toda a infraestrutura necessária e os componentes de software internamente. O software de gerenciamento adicional permite o provisionamento de autoatendimento. Uma nuvem privada é altamente personalizável, oferecendo controle máximo sobre segurança e configuração de infraestrutura.

3. **Nuvem híbrida**: combina serviços de TI locais gerenciados exclusivamente pela organização com serviços de um ou mais provedores de nuvem terceirizados. É usado para reduzir o investimento CAPEX, projetos de recuperação de desastres e testar novas tecnologias. As opções de conectividade, como túneis VPN ou conexões dedicadas baseadas em fibra, facilitam a integração entre ambientes locais e na nuvem. As implantações de nuvem híbrida permitem abordagens de migração em fases, interrupção mínima dos negócios durante a migração e implementação de soluções de alta disponibilidade (HA). Eles também permitem redirecionar os consumidores para serviços de réplica hospedados pelo provedor de nuvem pública durante o tempo de inatividade.

# CAPÍTULO 2 - INTRODUÇÃO À AWS E À INFRAESTRUTURA GLOBAL

## O QUE É AWS?

Amazon Web Services (AWS) é o maior provedor público de computação em nuvem do mundo, oferecendo mais de 175 serviços distintos acessíveis pela Internet em um modelo de pagamento conforme o uso. Atende a uma ampla gama de clientes, incluindo start-ups, empresas e organizações governamentais como a Marinha dos Estados Unidos. A AWS tem sido consistentemente reconhecida como líder no mercado de computação em nuvem pelo Quadrante Mágico da Gartner Research para Infraestrutura de Nuvem e Serviços de Plataforma.

A história da AWS começou em 2002 com alguns serviços ad hoc e, desde então, cresceu exponencialmente. A infraestrutura global da empresa, composta por data centers em todo o mundo, é fundamental para fornecer sua vasta gama de serviços em nuvem. Você pode acessar relatórios de pesquisa analítica, incluindo o Quadrante Mágico do Gartner, no site da AWS para saber mais sobre suas ofertas e liderança no setor de nuvem.

## EXPLORANDO A INFRAESTRUTURA GLOBAL DA AWS

A infraestrutura global da AWS consiste em vários datacenters espalhados por diferentes regiões geográficas em todo o mundo. Esses data centers hospedam servidores, dispositivos de armazenamento e equipamentos de rede. Atualmente, a AWS possui 77 zonas de disponibilidade (AZs) em 24 regiões, com planos para mais 18 AZs e 6 regiões adicionais da AWS no futuro.

As regiões são locais físicos onde a AWS hospeda clusters de datacenters, cada um contendo duas ou mais AZs. As AZs são grupos de data centers separados lógica e fisicamente em uma região. O objetivo de ter vários AZs é fornecer alta disponibilidade, tolerância a falhas e escalabilidade para os aplicativos dos clientes.

Além de Regiões e AZs, a AWS também opera pontos de presença, que são usados para entrega de conteúdo e armazenamento em cache. Os pontos de presença são estrategicamente posicionados e conectados às regiões da AWS por meio de links de alta velocidade, permitindo acesso mais rápido ao conteúdo acessado com frequência.

Alguns serviços da AWS são globais, o que significa que podem ser acessados de qualquer região sem a necessidade de especificar um local específico. Esses serviços incluem IAM, Amazon CloudFront, Amazon Route 53 e Amazon S3.

A AWS também oferece serviços locais, como AWS Snow Family, Amazon Storage Gateway e Amazon Outposts. Esses serviços são projetados para facilitar implantações de nuvem híbrida, auxiliar na migração de dados e atender clientes com requisitos rígidos de residência de dados.

Compreender a infraestrutura, regiões e AZs globais da AWS permite que os clientes projetem arquiteturas altamente disponíveis e tolerantes a falhas, ao mesmo tempo em que fornecem acesso de baixa latência a conteúdo e ativos digitais. Selecionar o plano de suporte da AWS certo também é essencial para o uso eficiente dos recursos da AWS e garantir o nível apropriado de suporte para seu caso de uso específico.

## ESCOLHER O PLANO DE SUPORTE DA AWS CERTO PARA SEU NEGÓCIO

A AWS fornece diferentes planos de suporte personalizados para atender às diversas necessidades das empresas. Os planos de suporte vão do Basic ao Enterprise e oferecem diferentes níveis de assistência técnica e tempos de resposta.

1. **Plano de suporte básico**: este plano é gratuito para todas as contas da AWS e cobre suporte básico ao cliente, problemas relacionados à conta e acesso a documentação disponível publicamente e fóruns de suporte. Também inclui acesso limitado à ferramenta Trusted Advisor para melhores práticas e ao Personal Health Dashboard para alertas de interrupções de serviço.

2. **Plano de suporte ao desenvolvedor**: recomendado para testes e cargas de trabalho fora da produção, este plano oferece suporte técnico por e-mail durante o horário comercial. Os tempos de resposta para orientação geral são de 24 horas e 12 horas para problemas de sistema prejudicado. Inclui acesso às verificações básicas da ferramenta Trusted Advisor.

3. **Plano de Suporte Empresarial**: Adequado para ambientes de produção, este plano fornece suporte 24 horas por dia, 7 dias por semana via e-mail, chat e telefone. Os tempos de resposta variam de acordo com a gravidade do problema. Ele inclui ajuda com solução de problemas e problemas de interoperabilidade. As empresas podem optar pelo AWS Infrastructure Event Management (IEM) para obter orientação adicional durante lançamentos ou migrações de projetos.

4. **Plano de Suporte Corporativo**: Projetado para grandes organizações com cargas de trabalho extensas, este plano premium inclui um Gerente Técnico de Contas (TAM) designado que auxilia ativamente no planejamento, design e implementação de projetos de nuvem. Ele oferece acesso a engenheiros de nuvem seniores e revisões bem arquitetadas para otimizar soluções. O tempo de resposta para questões críticas de negócios é de 15 minutos.

Cada plano tem recursos e benefícios distintos, e as empresas devem escolher com base em seus requisitos e orçamento específicos. Mais detalhes sobre os planos de suporte podem ser encontrados no site da AWS.

## VISÃO GERAL DO PAINEL DE INTEGRIDADE DE SERVIÇOS DA AWS

A AWS fornece um painel de integridade do serviço que oferece informações de status do serviço em tempo real em todos os datacenters em várias regiões. Este é o primeiro lugar para verificar se um serviço parece não responder. A AWS também oferece Acordos de nível de serviço (SLAs) para suas ofertas de serviço, garantindo níveis específicos de confiabilidade e disponibilidade.

O AWS Personal Health Dashboard (PHD) fornece informações personalizadas sobre problemas que podem afetar seus aplicativos e recursos. Ele oferece visualizações personalizadas da integridade do serviço, notificações proativas, orientação detalhada para solução de problemas, integração com o CloudWatch Events para automação e a capacidade de agregar eventos de integridade nas organizações da AWS para gerenciamento centralizado.

Antes de usar qualquer serviço na plataforma AWS, é essencial revisar e concordar com a Política de uso aceitável (AuP) da AWS, que descreve os termos e condições de uso do serviço.

## O AUP da AWS

Absolutamente, é essencial cumprir a Política de Uso Aceitável (AuP) da AWS ao se inscrever em uma conta da AWS para uso pessoal ou comercial. A política descreve os usos aceitáveis e proibidos dos serviços da AWS. O não cumprimento das diretrizes da política pode resultar na suspensão ou encerramento da conta, afetando potencialmente suas cargas de trabalho implantadas. Ao se inscrever nos serviços da AWS, você concorda automaticamente com a versão mais recente desta política. Para revisar a política completa, você pode visitar https://aws.amazon.com/aup/.

# CAPÍTULO 3 - EXPLORANDO AS CONTAS DA AWS, A ESTRATÉGIA DE MÚLTIPLAS CONTAS E AS ORGANIZAÇÕES DA AWS

## POR QUE TER UM AMBIENTE AWS DE MÚLTIPLAS CONTAS?

Certamente, uma arquitetura multiconta é essencial para gerenciar com eficiência cargas de trabalho complexas na AWS. Hospedar todos os recursos em uma única conta da AWS pode se tornar uma sobrecarga e dificultar o gerenciamento adequado. Ao separar as cargas de trabalho em diferentes contas, você obtém vários benefícios:

1. **Isolamento Administrativo**: Diferentes unidades de negócios podem ter níveis variados de controle administrativo. Por exemplo, os desenvolvedores podem não precisar de acesso total à conta de produção.

2. **Visibilidade limitada**: as contas da AWS criam um limite natural, garantindo que os recursos em uma conta não sejam acessíveis a identidades de outras contas sem permissão explícita.

3. **Gerenciamento de identidade e segurança**: centralize as contas de identidade do usuário em uma conta de gerenciamento de identidade da AWS, reduzindo contas duplicadas e simplificando o gerenciamento. O acesso entre contas garante que os usuários possam trabalhar em outras contas com as permissões necessárias.

4. **Recuperação e isolamento de auditoria**: cargas de trabalho de continuidade de negócios e recuperação de desastres podem ser colocadas em contas separadas para recuperação eficiente e continuidade operacional.

Na próxima seção, nos aprofundamos nos serviços da AWS que ajudam a projetar e implementar uma estratégia de várias contas. O AWS Landing Zone, que auxilia na criação de uma arquitetura de linha de base personalizada para implantações de várias contas, e o AWS Control Tower, uma solução automatizada alinhada às melhores práticas do setor, são discutidos em detalhes. Esses serviços fornecem a estrutura para gerenciar e proteger com eficiência seus recursos da AWS em várias contas.

## ZONA DE ATERRISSAGEM AWS X TORRE DE CONTROLE AWS

**Resumo:**
Projetar um ambiente de várias contas na AWS pode ser complexo e demorado. A AWS fornece metodologias de práticas recomendadas para essa finalidade. O obsoleto AWS Landing Zone foi substituído pelo AWS Control Tower. Enquanto a Landing Zone permanece em suporte, a Torre de Controle é recomendada. O Control Tower automatiza a configuração da zona de aterrissagem com o AWS Organizations, IAM, log e políticas de segurança.

**Elementos chave:**
- **Zona de aterrissagem da AWS:**
   - Blueprint de linha de base para arquitetura de várias contas.
   - Gerenciamento de identidade, governança, segurança e registro.
   - Obsoleto em favor do AWS Control Tower.
   - Pode aparecer em exames apesar da falta de novos recursos.

- **Torre de controle da AWS:**
   - Automatiza a configuração da zona de aterrissagem usando os modelos mais recentes.
   - Inclui AWS Organizations e configuração de várias contas.
   - Utiliza AWS Single Sign-On (SSO) para gerenciamento de identidade.
   - Suporta federação de contas com SSO.
   - Logging centralizado com AWS CloudTrail e AWS Config.
   - Vem com as políticas de segurança recomendadas (guarda-corpos).
   - Permite personalização para alinhar com as políticas organizacionais.

- **Benefícios:**
   - Simplifica a arquitetura multiconta complexa.
   - Economiza tempo em comparação com a configuração manual.
   - Oferece segurança e conformidade prontas para uso.

- **Próximos passos:**
   - Compreensão do AWS Organizations para gerenciamento central de contas.
   - Importância das ferramentas na construção de arquitetura de nuvem segura.

## ORGANIZAÇÕES DA AWS

**Resumo:**
O gerenciamento eficiente de várias contas da AWS é crucial para a separação e conformidade da carga de trabalho. O AWS Organizations oferece gerenciamento centralizado, permitindo a criação de uma conta de gerenciamento e várias contas de membros. Unidades de organização (OUs) agrupam contas logicamente e políticas de controle de serviço (SCPs) impõem restrições de serviço. O faturamento consolidado ajuda no gerenciamento de custos e diferentes estruturas de unidades organizacionais atendem a diversas necessidades de negócios.

**Elementos chave:**
- **Organizações da AWS:**
   - Gerencia centralmente várias contas da AWS.
   - Oferece um serviço gratuito com recursos cobráveis.
   - Cria uma conta de gerenciamento e contas de membro.
   - OUs organizam contas hierarquicamente.
   - Os SCPs aplicam proteções aos serviços por UO.
   - Fornece faturamento consolidado para gerenciamento de custos.
   - Permite várias estruturas OU com base nas necessidades.
   - Facilita limites de segurança e conformidade.

- **UOs principais:**
   - UO de infraestrutura: serviços compartilhados (por exemplo, diretório, rede).
   - OU de segurança: IAM, políticas entre contas, registro.
   - Separa as contas de produção e não produção.

- **OUs adicionais:**
   - OUs Sandbox: Ambiente isolado para experimentos.
   - OUs de cargas de trabalho: hospeda aplicativos voltados para o cliente (Dev, Test, Prod).
   - OUs Suspensas: Contas para auditoria, com acesso restrito.

- **Benefícios:**
   - Gerencie com eficiência várias contas da AWS.
   - Garanta a segurança e a separação da carga de trabalho.
   - Reforçar a conformidade com os SCPs.
   - Otimização de custos através do faturamento consolidado.

- **Considerações:**
   - Determine as contas necessárias da AWS com base nas necessidades de negócios.
   - Equilibrar requisitos funcionais e técnicos.
   - Siga as estruturas de OU recomendadas para orientação.

- **Próximos passos:**
   - Explorar as estruturas de OU recomendadas:
     [Guia de estrutura de OU recomendada](https://docs.aws.amazon.com/whitepapers/latest/organizating-your-aws-environment/recommended-ous.html).
   - Saiba mais sobre contas e criação de nível gratuito da AWS na próxima seção.

## CONTAS DE NÍVEL GRATUITO da AWS

**Resumo:**
A conta de nível gratuito da AWS oferece uma conta padrão para várias cargas de trabalho, gratuita nos primeiros 12 meses. Ele fornece acesso a mais de 85 serviços da AWS, com limites de uso específicos. As principais ofertas incluem armazenamento Amazon S3, instâncias EC2 e instâncias RDS. Ferramentas adicionais como AWS CloudFormation e Elastic Beanstalk são gratuitas, mas os recursos implantados são cobrados. Certos serviços como CloudWatch, Lambda e AWS Organizations são sempre gratuitos até os limites especificados. Também existem serviços de teste gratuitos, como Amazon Workspaces, Detective e Redshift. O nível gratuito é valioso para aprendizado e experimentação.

**Elementos chave:**
- **Conta de nível gratuito da AWS:**
   - Conta padrão para diversas cargas de trabalho.
   - Gratuito por 12 meses com limites de uso.
   - Acesso a mais de 85 tecnologias e serviços da AWS.
   - Exemplos de uso no nível gratuito:
     - Armazenamento Amazon S3 até 5 GB.
     - Instância t2.micro EC2 para 750 horas/mês.
     - Instância do Amazon RDS por 750 horas/mês.

- **Ferramentas gratuitas:**
   - AWS CloudFormation: Modelos para implantação de infraestrutura.
   - Amazon Elastic Beanstalk: Serviço de orquestração de aplicações.
   - As ferramentas são gratuitas, mas os recursos têm cobranças.

- **Serviços Sempre Gratuitos:**
   - Amazon CloudWatch: 10 métricas personalizadas, 10 alarmes, 1 milhão de solicitações de API.
   - Amazon Lambda: 1 milhão de solicitações gratuitas, 3,2 milhões de segundos de computação.
   - AWS Organizations: gerencie contas centralmente com faturamento consolidado.

- **Avaliações Gratuitas:**
   - Amazon Workspaces: teste de desktops virtuais com limites de uso.
   - Amazon Detective: teste de análise de dados de segurança (30 dias).
   - Redshift: teste de armazenamento de dados (2 meses, 750 horas/mês).

- **Benefícios:**
   - Experimente os serviços da AWS.
   - Criar ambientes sandbox.
   - Aprenda e se prepare para os exames.
   - Arquitetar soluções com experiência prática.

- **Considerações:**
   - Aplicam-se limites e limitações de uso.
   - Útil para explorar configurações complexas.
  
- **Próximos passos:**
   - Aproveite o nível gratuito da AWS para aprendizado, experimentação e preparação.
   - Entenda os limites de uso e explore configurações mais avançadas da AWS.

# CAPÍTULO 4: GERENCIAMENTO DE IDENTIDADE E ACESSO

## INTRODUÇÃO AO SERVIÇO AWS IAM

Nesta seção do livro, nos aprofundamos nos fundamentos do serviço AWS Identity and Access Management (IAM). Ele começa enfatizando a importância do usuário root, que é essencialmente o criador da conta da AWS e possui privilégios significativos. A proteção das credenciais do usuário raiz é enfatizada e é recomendável não usar essa conta para tarefas do dia a dia.

A introdução destaca o conceito de usuários IAM, que são contas de usuário adicionais que podem ser criadas para realizar operações de rotina. O console do IAM é apresentado como a interface principal para acessar os serviços da AWS, e os leitores são informados de que ele pode ser acessado por meio do console de gerenciamento baseado na web, da interface de linha de comando (CLI) ou SDKs da AWS para fins de codificação.

A estrutura do Console de gerenciamento da AWS é discutida, revelando que os serviços são categorizados em títulos como Computação, Rede e Armazenamento. O AWS IAM está situado na categoria Segurança, Identidade e Conformidade. A capacidade de procurar serviços usando a barra de pesquisa também é mencionada.

Ao entrar no console do IAM, alertas de segurança e melhores práticas são apresentados. Um URL de login exclusivo é revelado para os usuários do IAM na conta, permitindo a personalização para facilitar o uso. Essa URL, que contém o ID da conta da AWS, pode ser adaptada para um nome mais reconhecível. O processo de personalização da URL de login é detalhado.

O URL de login personalizado do IAM pode então ser compartilhado com outros usuários do IAM, permitindo que eles acessem a conta caso possuam uma conta de usuário do IAM. O significado dos usuários do IAM e sua criação é detalhado. O texto conclui sugerindo o próximo tópico a ser discutido: a conta do usuário root e a implementação da autenticação multifator (MFA) para maior segurança.

## A CONTA DO USUÁRIO ROOT E A IMPLEMENTAÇÃO DA AUTENTICAÇÃO MULTIFATORIAL (MFA)

Nesta parte do livro, o foco está na importância da conta do usuário raiz na AWS e na implementação da autenticação multifator (MFA) para aumentar a segurança. Inicialmente, são destacadas as limitações de depender apenas de um nome de usuário e senha para autenticação, considerando as ameaças predominantes de ataques de malware, hacking e ataques de força bruta. Para neutralizar esses riscos, o MFA é introduzido como um mecanismo para garantir a verificação de identidade usando dois conjuntos de credenciais: algo que você conhece (nome de usuário e senha) e algo que você possui (um pin de senha única gerado em um dispositivo pessoal).

A recomendação para configurar o MFA para a conta do usuário raiz é enfatizada. O processo de configuração do MFA é explicado em detalhes e os leitores são guiados pelas etapas. Sugere-se usar autenticadores baseados em smartphone suportados pela AWS, como Google Authenticator ou Microsoft Authenticator.

As etapas para configurar o MFA envolvem acessar o console de gerenciamento do IAM e ativar o MFA, seguido pela ativação de um dispositivo MFA virtual. O processo inclui a digitalização de um código QR usando o aplicativo autenticador escolhido e a inserção dos códigos MFA gerados para concluir a configuração. Isso garante que a conta do usuário root esteja agora protegida por MFA.

Os benefícios do MFA são reiterados, enfatizando que, ao fazer login como usuário root, além do endereço de e-mail e senha, será necessário o código MFA do aplicativo autenticador. A natureza temporária do código MFA é observada, exigindo entrada imediata. Depois que o código MFA é fornecido, o login bem-sucedido leva ao acesso ao Console de gerenciamento da AWS.

A seção também recapitula os tópicos abordados, incluindo uma introdução ao AWS Management Console básico e AWS IAM, bem como a implementação prática do MFA para a conta do usuário root. O próximo foco é sugerido: políticas de senha para impor senhas robustas e complexas para usuários IAM criados na conta AWS.

## A IMPORTÂNCIA DE DEFINIR AS POLÍTICAS DE SENHAS DO IAM

O foco muda para a importância de estabelecer políticas robustas de senha IAM (gerenciamento de identidade e acesso) em um ambiente AWS (Amazon Web Services). Depois de proteger a conta de usuário raiz usando autenticação multifator (MFA), a próxima etapa envolve a criação de contas de usuário IAM para membros de uma organização que necessitam de acesso aos serviços da AWS. Os privilégios elevados do usuário raiz exigem que se evite seu uso nas operações do dia-a-dia.

O texto antecipa a necessidade de configuração de senhas para contas de usuário do IAM. A importância de impor políticas de senha é destacada, principalmente ao lidar com várias contas de usuário do IAM. A AWS oferece recursos de política de senha que permitem aos administradores definir regras que aumentam a complexidade da senha. Ao fazer isso, os usuários são obrigados a selecionar senhas que cumpram as regras de complexidade estipuladas, promovendo assim o uso de senhas fortes em todas as contas de usuários do IAM.

O processo de configuração dessas políticas de senha é descrito para ser acessível na seção Account Settings do painel do IAM. Isso permite que os administradores mantenham o controle sobre a segurança das contas de usuário do IAM.

A seção a seguir é sugerida, com foco na criação de usuários IAM adicionais e no estabelecimento de grupos IAM. Os usuários do IAM são identidades distintas que podem ser geradas além da conta do usuário raiz. Esses usuários representam indivíduos reais dentro da organização que precisam de acesso aos serviços da AWS para suas respectivas funções, como desenvolvedores ou administradores de servidor.

Em resumo, esta parte do texto enfatiza a importância de impor políticas de senha do IAM para garantir medidas de segurança sólidas nas contas de usuário do IAM da organização, além de apresentar o conceito de usuários do IAM e sua relevância no ambiente da AWS.

## PRINCIPAIS DIFERENÇAS ENTRE USUÁRIOS DO IAM E GRUPOS DO IAM

Nesta seção do livro, o foco está nas principais distinções entre usuários IAM (Identity and Access Management) e grupos IAM dentro do ecossistema AWS (Amazon Web Services).

**Usuários IAM**:
Conforme explicado anteriormente, os usuários do IAM são contas adicionais que podem ser criadas juntamente com o usuário raiz. Esses usuários podem representar indivíduos reais em uma organização, como membros de uma equipe de desenvolvimento ou administradores de servidor. Os usuários do IAM recebem suas próprias credenciais e podem usá-las para fazer login na conta da AWS, realizando tarefas com base nas permissões atribuídas a eles.

As contas de usuário do IAM também podem ser empregadas por aplicativos e serviços que precisam se autenticar com os serviços da AWS. Por exemplo, um aplicativo que precisa modificar um banco de dados do Amazon RDS pode receber uma conta de usuário do IAM com as permissões apropriadas. No entanto, essa abordagem não é ideal para a maioria das situações devido a questões de segurança associadas ao armazenamento de credenciais em texto simples e à necessidade de rotação regular de credenciais. A AWS apresenta as funções do IAM como uma alternativa melhor para esses casos, que são abordados posteriormente no capítulo.

O acesso aos serviços da AWS pode ser obtido por meio do console de gerenciamento baseado na web, CLI (Command Line Interface) ou SDKs da AWS. Os usuários do IAM podem usar combinações de nome de usuário e senha para acesso ao console, enquanto o acesso programático por meio da CLI requer chaves de acesso, incluindo um ID de chave de acesso e uma chave de acesso secreta.

**Grupos IAM**:
O conceito de grupos IAM é apresentado como um meio de gerenciar com eficiência as permissões para usuários que compartilham funções comuns na organização. Ao configurar permissões para um usuário do IAM, as políticas podem ser anexadas diretamente. No entanto, uma abordagem mais simplificada envolve o agrupamento de usuários com base em suas funções e, em seguida, a aplicação de políticas ao próprio grupo, permitindo que essas políticas sejam distribuídas em cascata aos usuários individuais dentro do grupo.

Por exemplo, se uma equipe de desenvolvedores exigir a capacidade de gerenciar depósitos de armazenamento do Amazon S3, em vez de atribuir manualmente a mesma permissão a cada desenvolvedor, uma única permissão poderá ser concedida a um grupo IAM chamado "Desenvolvedores". Todos os membros deste grupo herdarão a permissão especificada, simplificando o gerenciamento de permissões.

Em resumo, esta seção enfatiza o valor da configuração de usuários e grupos do IAM, o que permite um controle eficaz sobre o acesso e as permissões na conta da AWS. Os grupos IAM são destacados como uma maneira de gerenciar com eficiência as permissões para usuários que compartilham funções de trabalho semelhantes.

A próxima seção é visualizada para aprofundar as políticas do IAM em detalhes, elucidando como essas políticas capacitam os administradores a definir permissões para várias identidades, controlando assim suas ações na conta da AWS.

## DEFININDO PERMISSÕES COM POLÍTICAS IAM

Nesta seção, o livro discute o conceito de políticas IAM (Identity and Access Management) dentro do ecossistema AWS (Amazon Web Services) e como elas são usadas para definir permissões para várias identidades IAM, como usuários, grupos e funções IAM. As políticas do IAM desempenham um papel crucial na aplicação do princípio do menor privilégio, garantindo que as identidades recebam apenas o acesso necessário para suas funções.

**Visão geral das políticas do IAM**:
As políticas do IAM são documentos JSON anexados às identidades do IAM, especificando as ações que uma identidade pode executar na conta da AWS. O livro apresenta uma ilustração de Bob, um membro do grupo de desenvolvedores, e como seu acesso ao bucket S3 "Marketing Documents" é controlado por uma política IAM anexada.

**Tipos de políticas IAM**:
O livro apresenta seis tipos de políticas IAM:

1. **Políticas baseadas em identidade**: anexadas a identidades do IAM, como usuários, grupos e funções, para definir suas permissões na conta da AWS.
2. **Políticas baseadas em recursos**: anexadas a recursos, concedendo permissões a principais (identidades) dentro ou fora da conta da AWS.
3. **Limites de permissão**: uma política que define o máximo de permissões para uma entidade IAM, controlando o que uma política baseada em identidade pode conceder.
4. **Organization Service Control Policies (SCPs)**: Defina as permissões máximas para os membros da organização, restringindo o que as políticas do IAM podem permitir.
5. **Listas de controle de acesso (ACLs)**: gerencie o acesso a recursos específicos, como baldes e objetos do Amazon S3, concedendo permissões a contas da AWS.
6. **Políticas de sessão**: aprovadas durante o acesso programático, limitando as permissões para uma sessão específica.

**Tipos de políticas baseadas em identidade**:
As políticas baseadas em identidade podem ser categorizadas em três tipos:

1. **Políticas gerenciadas da AWS**: políticas pré-configuradas com permissões específicas fornecidas pela AWS. Eles podem ser anexados a múltiplas identidades.
2. **Políticas gerenciadas pelo cliente**: políticas criadas por clientes, oferecendo mais granularidade nos conjuntos de permissões.
3. **Políticas em linha**: políticas criadas e anexadas diretamente a uma identidade IAM, mantendo uma relação um-para-um.


**Exemplo de política IAM**:
Um exemplo de política IAM é fornecido, demonstrando uma política gerenciada da AWS chamada "AmazonS3ReadOnlyAccess". A estrutura JSON da política inclui componentes como versão, declarações, efeitos, ações, recursos e condições. A política de exemplo concede acesso de leitura a todos os buckets do S3.

**Simulador de política IAM**:
O livro apresenta o simulador de políticas IAM, uma ferramenta para testar e solucionar problemas de políticas sem fazer chamadas de API reais. Essa ferramenta ajuda a identificar as permissões concedidas ou negadas com base nas políticas anexadas às identidades do IAM.

**Funções do IAM e credenciais temporárias**:
As funções do IAM são discutidas como identidades independentes que podem ser assumidas por outras entidades, oferecendo acesso seguro aos serviços e recursos da AWS. As funções do IAM são usadas para cenários como acesso entre contas, usuários federados e acesso a serviços da AWS. As funções usam credenciais temporárias atribuídas pelo Security Token Service (STS), fornecendo acesso de curto prazo a recursos sem armazenar credenciais de longo prazo. Uma política de confiança define entidades que podem assumir a função, e o livro enfatiza o uso de funções em vez de contas de usuário do IAM para maior segurança.

Concluindo, esta seção explora a importância das políticas do IAM no controle de acesso e permissões na AWS. Ele apresenta os vários tipos de políticas e se aprofunda nas políticas baseadas em identidade em detalhes. O simulador de política IAM e o uso de funções IAM com credenciais temporárias também são discutidos. A próxima seção é uma visualização dos relatórios de credenciais e sua função na auditoria de identidades do IAM.

## REVISÃO DE RELATÓRIOS DE CREDENCIAIS

Nesta seção, o livro discute a importância dos relatórios de credenciais no serviço IAM (Identity and Access Management) da AWS. Os relatórios de credenciais fornecem informações valiosas sobre o estado de segurança dos usuários do IAM, permitindo que os administradores revisem e auditem as principais informações sobre suas identidades e status de acesso.

**Visão geral dos relatórios de credenciais**:
A AWS oferece a capacidade de baixar relatórios de credenciais no formato CSV. Esses relatórios são atualizados a cada 4 horas e fornecem aos administradores uma visão abrangente dos usuários do IAM em suas contas da AWS. Os relatórios contêm detalhes essenciais, como nomes de usuário, status de credenciais (senhas e chaves de acesso) e se os usuários têm autenticação multifator (MFA) configurada.

**Casos de uso para relatórios de credenciais**:
Monitorar e analisar relatórios de credenciais pode oferecer vários benefícios:

1. **Auditoria de usuários do IAM**: os relatórios permitem revisar e auditar o status de segurança de seus usuários do IAM. Você pode avaliar se suas credenciais estão configuradas corretamente, incluindo senhas e chaves de acesso.

2. **Verificação MFA**: Os relatórios destacam se os usuários configuraram a autenticação multifator (MFA), adicionando uma camada extra de segurança às suas contas.

3. **Atividade do usuário**: ao rastrear a atividade do usuário, você pode identificar usuários do IAM que não acessaram recursos em sua conta da AWS recentemente. Isso ajuda a avaliar se esses usuários ainda precisam de acesso e se as contas não utilizadas podem ser removidas, melhorando a segurança geral.

4. **Revisão do controle de acesso**: os relatórios de credenciais ajudam a manter uma visão geral clara dos padrões de acesso dos usuários do IAM e suas credenciais correspondentes, auxiliando no melhor gerenciamento do controle de acesso.

5. **Conformidade de segurança**: a revisão regular dos relatórios de credenciais oferece suporte aos esforços de conformidade de segurança da sua organização, garantindo que os usuários sigam as melhores práticas e políticas de segurança.

**Conclusão da Seção de Relatórios de Credenciais**:
Nesta seção, o livro apresenta o conceito de relatórios de credenciais como uma ferramenta valiosa para administradores de IAM. Ele enfatiza a importância de monitorar regularmente esses relatórios para manter a segurança dos usuários do IAM, rastrear seu status de acesso e identificar quaisquer contas não utilizadas ou desnecessárias. As próximas seções fornecerão exercícios práticos para ajudar os leitores a obter experiência prática no uso do AWS IAM para aumentar a segurança em suas contas da AWS.
