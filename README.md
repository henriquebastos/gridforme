# gridfor.me

Easy grid overlay for your perfect web design.


## What is it?

Grid overlays helps you to keep you design consistent. It allows you to maintain both vertical rhythm and horizontal alignment.

Using [gridfor.me](http://gridfor.me) you create an overlay by simply adding a stylesheet to your page:

`<link rel="stylesheet" href="http://gridfor.me/12/95/30/15/">`

Just like that. You'll get you a grid overlay with 12 columns, 95px width cells, 30px baseline and 15px gutter. Just like the one you can see on this page.


## Make it yours

You can customize every aspect of your grid.

Understand the parameters:

`http://gridfor.me/columns/cellwidth/baseline/[gutter]/?bg=R,G,B,A&h=R,G,B&v=HEX`

- *columns* defines how many columns there are on the grid.
- *cellwidth* defines how wide each cell is including gutters.
- *baseline* defines the height of each row on the grid.
- *gutter* defines the width of both left and right gutters. This is *optional* and *defaults to 0px*.
- *bg* is the background color.
- *h* is the horizontal lines color.
- *v* is the vertical lines color.

Colors are **RGBA** and can be expressed in the forms:

- `0067ff`
- `0067ffff`
- `255,0,255`
- `255,0,255,128`

*Note*: If you omit the alpha component it defaults to **opaque**.

## Grid examples

8 columns, 120px width cells, 24px baseline, no gutters, white transparent background, pink baseline and blue columns.

```
<link rel="stylesheet" href="http://gridfor.me/8/120/24/?bg=ffffffff&h=255,0,255&v=0,133,255">
```

16 columns, 80px width cells, 32px baseline, 16px gutters, blue half-transparet background, black baseline and ping columns.

```
<link rel="stylesheet" href="http://gridfor.me/16/80/32/16/?bg=0,0,255,127&h=000000&v=ff00ff">
```

## Getting only the grid image

If you just want the grid image to use in your own fashion, simply prepend the url path with an `i`:

`http://gridfor.me/i/12/95/30/15/`

So your CSS may be:

```
html { background-image: url(http://gridfor.me/i/12/95/30/15/); }
```

## Authors

Inspired by [basehold.it](http://basehold.it) and shared with you by [Henrique Bastos](http://henriquebastos.net/me) & [Vinícius Braga](http://viniciusbraga.info/).
