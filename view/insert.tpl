% rebase('view/base.tpl', title='Login')
<form action="/insert" method="post">
	<div class="form-group">
	  <input name="nome" type="text" placeholder="NOME">
	</div>
	<div class="form-group">
	  <input name="email" type="text" placeholder="E-MAIL" >
	</div>
	<div class="form-group">
	  <input name="senha" type="password" placeholder="SENHA">
	</div>
	<button class="btn">Registrar</button>
</form>