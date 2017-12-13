% rebase('./view/base.tpl', title='Delete')
<form action="/delete/{{dados[0]}}" method="post">
	<div class="panel panel-default">
	  <div class="panel-heading">Deseja apagar a conta?</div>
	  <div class="panel-body">
	    <p>
	    	<button class="btn btn-primary">Next</button>
	    </p>
	  </div>
	</div>
</form>