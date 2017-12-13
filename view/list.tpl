% rebase('view/base.tpl', title='Page Title')
<p>
	<a href = "/insert" class="btn">insert</a>
</p>
<table class="table table-striped">
	<thead>
		<tr>
			<th>#</th>
			<th>Nome</th>
		</tr>
	</thead>
	<tbody>
		%for row in dados:
		<tr>
			%for col in row:
			<td>{{ col }}</td>
			%end
			<td><a href = "profile/{{row[0]}}" class="btn">Info</a></td>
		</tr>
		%end
	</tbody>
</table>