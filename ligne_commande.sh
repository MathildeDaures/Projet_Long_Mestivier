for file in *.pov; do povray +O${file%.pov}.png $file +W1280 +H1024; done
mencoder mf://*.png -mf w=320:h=240:fps=10:type=png -ovc lavc -o simulation.avi
