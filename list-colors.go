package main

import (
	"fmt"
	"image/png"
	"log"
	"os"
	"sort"
)

type freq struct {
	color string
	count int
}

func (f freq) String() string {
	return fmt.Sprint(f.color, " ", f.count)
}

func main() {
	for _, filename := range os.Args[1:] {
		fmt.Println(filename)
		imgFile, err := os.Open(filename)
		if err != nil {
			log.Fatalln(err)
		}
		defer imgFile.Close()

		img, err := png.Decode(imgFile)
		if err != nil {
			log.Fatalln(err)
		}

		frequency := make(map[string]int)
		bounds := img.Bounds()
		for y := bounds.Min.Y; y < bounds.Max.Y; y++ {
			for x := bounds.Min.X; x < bounds.Max.X; x++ {
				r, g, b, a := img.At(x, y).RGBA()
				r, g, b, a = r>>8, g>>8, b>>8, a>>8
				frequency[fmt.Sprintf("#%02x%02x%02x%02x", r, g, b, a)]++
			}
		}

		sortedFrequency := make([]freq, 0, len(frequency))
		for k, v := range frequency {
			i := sort.Search(len(sortedFrequency), func(index int) bool {
				return sortedFrequency[index].count <= v
			})

			if i != len(sortedFrequency) {
				copy(sortedFrequency[i+1:], sortedFrequency[i:])
				sortedFrequency[i] = freq{k, v}
			} else {
				sortedFrequency = append(sortedFrequency, freq{k, v})
			}
		}

		max := 20
		for i, freq := range sortedFrequency {
			if i >= max {
				break
			}
			fmt.Println(freq)
		}
	}
}
