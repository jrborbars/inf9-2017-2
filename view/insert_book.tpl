% rebase('view/base.tpl', title='Insert book')
<form action="/insert_book" method="post">
	<div class="form-group">
	  <input name="titulo" type="text" placeholder="titulo">
	</div>
	<div class="form-group">
	  <input name="autor" type="text" placeholder="autor" >
	</div>
	<div class="form-group">
	  <input name="ano" type="text" placeholder="ano">
	</div>
	<div class="form-group">
	  <input name="editora" type="text" placeholder="editora">
	</div>
	<div class="form-group">
	  <input name="isbn" type="text" placeholder="ISBN">
	</div>
	<div class="form-group">
		  <textarea name="sinopse">
		  	
		  </textarea>
	</div>
	<div class="form-group">
		  <input name="sit" type="password" placeholder="situação">
	</div>
	<button class="btn">Registrar</button>
</form>