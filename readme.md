# botSorteiInstagram
  Com um arquivo onde tem uma classe "InstagramBot", essa classe tem:
  - um metodo login que faz o login da sua conta no instagram;
  - um metodo `pega_numero_seguidores` que vai até o seu perfil e pega a informação de quantos perfis te seguem
  - um metodo `pega_seguidores` que usa o metodo `pega_numero_seguidores` e para pegar todos seus seguidores do instagram e coloca em um arquivo `"users.txt"` (para ser usado as outras vezes que você rodar o bot)
  - um metodo `comente_nas_fotos_com_a_hashtag` que usa os dois metodos de cima para fazer uma lista de seguidores e depois gerar comentarios (se os comentarios precisarem ser perfis alheios)

## como começar:
  Coloque seu perfil e sua senha no final do código, esses dados vão ser usados para:
  - fazer o login no seu perfil;
  - pegar as informações de quantos seguidores você tem
  - pegar `quase todos` os seus seguidores

### `como colocar outro link de sorteio`:
  No inicio do metodo `comente_nas_fotos_com_a_hashtag` tem as variaveis que tem os links dos sorteios, ai que você controla qual sorteio quer usar, só atribuir a variavel do sorteio que quer para a variavel `sorteio_da_vez`

### `como alterar o que você vai comentar`:
  Pra alterar o que vai comentar você precisa alterar logo depois do `#GERA COMENTARIOS`, se precisar usar os perfis dos seus seguidores descomenta as linhas de baixo e faz sua menssagem 

### `como comentar`:
  Pra comentar você precisa descomentar as pertes do `#FAZ COMENTARIO` e atribuir o comentario que você criou lá em cima 
