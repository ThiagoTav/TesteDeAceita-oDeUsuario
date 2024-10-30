Feature: Teste de Aceitação - Login de Usuário
  Como usuário, quero acessar o sistema com meu login e senha válidos.

  Scenario: Login com credenciais válidas
    Given que estou na página de login
    When insiro "standard_user" e "secret_sauce"
    Then devo ser redirecionado para o painel principal