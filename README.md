# READ: Use ImageMagick to ensure images render well in safari

Before adding your news‐logo images to the project, you can “flatten” them onto a white background so that browsers like Safari won’t introduce gray halos around transparent edges.

For instance, to convert the logo from pearc24, do: 
convert pearc24logo.png -background white -flatten pearc24logo.png
