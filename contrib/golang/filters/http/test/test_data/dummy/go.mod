module example.com/dummy

go 1.23

toolchain go1.23.10

require github.com/envoyproxy/envoy v1.24.0

require google.golang.org/protobuf v1.36.10 // indirect

replace github.com/envoyproxy/envoy => ../../../../../../../
