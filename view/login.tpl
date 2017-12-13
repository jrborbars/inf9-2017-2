% rebase('view/base.tpl', title='Login')
<form action="/login" method="post">
	<div class="form-group">
	  <input name="email" type="text" placeholder="EMAIL" >
	</div>
	<div class="form-group">
	  <input name="senha" type="password" placeholder="SENHA">
	</div>
	<button class="btn"> Logar </button>
</form>