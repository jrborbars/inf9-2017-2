% rebase('./view/base.tpl', title='Edit')
<form action="/update/{{dados[0]}}" method="post">
	<table class="table">
		<tbody>
			<tr>
				<td>Nome:</td>
				<td><input name="nome" type="text" value="{{dados[1]}}"></td>
			</tr>
			<tr>
				<td>Email:</td>
				<td><input name="email" type="text" value="{{dados[2]}}"></td>
			<tr>
				<td><a href="#" class="btn btn-right">reset password</a></td>
				<td><button class="btn btn-primary">Aplicar</button></td>
			</tr>
		</tbody>
	</table>
</form>