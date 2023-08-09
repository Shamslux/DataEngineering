<a href="https://www.goodreads.com/user/show/50697219-jo-o-paulo-m-ller-mamede">
    <img src="https://img.shields.io/badge/Goodreads-372213?style=for-the-badge&logo=goodreads&logoColor=white" alt="Goodreads Badge"/>
  </a>
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/13/United-kingdom_flag_icon_round.svg" width=25 height=25/> 
  
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

