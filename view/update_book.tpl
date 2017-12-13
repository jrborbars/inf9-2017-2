% rebase('./view/base.tpl', title='Edit')
% rebase('view/base.tpl', title='Insert book')
<form action="/update_book/{{dados[0]}}" method="post">
	<div class="form-group">
	  <input name="titulo" type="text" value="{{dados[1]}}">
	</div>
	<div class="form-group">
	  <input name="autor" type="text" value="{{dados[2]}}" >
	</div>
	<div class="form-group">
	  <input name="ano" type="text" value="{{dados[3]}}">
	</div>
	<div class="form-group">
	  <input name="editora" type="text" value="{{dados[4]}}">
	</div>
	<div class="form-group">
	  <input name="isbn" type="text" value="{{dados[5]}}">
	</div>
	<div class="form-group">
		  <textarea row="5" cols="40" name="sinopse">
		  	{{dados[6]}}
		  </textarea>
	</div>
	<div class="form-group">
		  <input name="sit" type="password" value="{{dados[7]}}">
	</div>
	<button class="btn">Registrar</button>
</form>