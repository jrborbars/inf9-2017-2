<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8"/>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>{{title or 'WEB'}}</title>
		<link href="/static/bootstrap.css" rel="stylesheet" type="text/css"/>
		<link href="/static/bootstrap.min.css" rel="stylesheet" type="text/css"/>
		<link href="/static/bootstrap-responsive.css" rel="stylesheet" type="text/css"/>
		<link href="/static/bootstrap-responsive.min.css" rel="stylesheet" type="text/css"/>
		<script type="text/js" src="/static/jquery.min.js"></script>
		<script type="text/js" src="/static/bootstrap.js"></script>
   		<script type="text/js" src="/static/bootstrap.min.js"></script>
	</head>
	<body>
		<div class="container">
			<header>
				<nav class="navbar navbar-default">
				  <div class="container-fluid">
				    <div class="navbar-header">
				      <a class="navbar-brand" href="#">Brand</a>
				      <button type="button" class="btn btn-default navbar-btn">Sign in</button>
				    </div>
				  </div>
				</nav>
			</header>
			<article class="content">
				{{!base}}
			</article>
		</div>
	</body>
</html>