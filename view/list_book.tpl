% rebase('view/base.tpl', title='Page Title')
<p>
	<a href="/insert_book" class="btn">insert</a>
</p>
<table class="table table-striped">
	<thead>
		<tr>
			<th>#</th>
			<th>titulo</th>
			<th>autor</th>
			<th>ano</th>
			<th>editora</th>
			<th>ISBN</th>
			<th>sinopse</th>
			<th>situação</th>
		</tr>
	</thead>
	<tbody>
		%for row in dados:
		<tr>
			%for col in row:
			<td>{{ col }}</td>
			%end
			<td><a href = "update_book/{{row[0]}}" class="btn">Edit</a></td>
			<td><a href = "delete_book/{{row[0]}}" class="btn">Delete</a></td>
		</tr>
		%end
	</tbody>
</table>