% rebase('./view/base.tpl', title='Profile')
<table class="table">
	<tbody>
		<tr>
			<td>Nome:</td>
			<td>{{ dados[1] }}</td>
		</tr>
		<tr>
			<td>Email:</td>
			<td>{{ dados[2] }}</td>
		</tr>
			<td>Senha:</td>
			<td>{{ dados[3] }}</td>
		</tr>
		<tr>
			<td colspan="2"><a href="/update/{{dados[0]}}" class="btn btn-right">edit</a></td>
			<td><a href="/delete/{{dados[0]}}" class="btn">delete</a></td>
		</tr>
	</tbody>
</table>
