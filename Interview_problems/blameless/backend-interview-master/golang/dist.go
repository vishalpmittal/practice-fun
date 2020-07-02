package main

import (
	"math/rand"
)

// UniformDist is a wrapper around a seeded instance of Rand
type UniformDist struct {
	r *rand.Rand
}

// NewUniformDist will return a seeded instance of UniformDist
func NewUniformDist(seed int64) *UniformDist {
	r := rand.New(rand.NewSource(seed))
	return &UniformDist{
		r: r,
	}
}

// Random will return a random number between low and high
func (dist *UniformDist) Random(low, high float64) float64 {
	return (rand.Float64() * (high - low)) + low
}

// Shuffle will return a copy of ary shuffled
func (dist *UniformDist) Shuffle(ary []interface{}) []interface{} {
	out := ary[:]
	dist.r.Shuffle(len(ary), func (i, j int) { out[i], out[j] = out[j], out[i] })

	return out
}

// RandomInt will return a random in between [0, n)
func (dist *UniformDist) RandomInt(n int) int {
	return dist.r.Intn(n)
}
