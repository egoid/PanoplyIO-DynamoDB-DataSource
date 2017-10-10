// Usage: go run export.go -k [AWS-KEY] -s [AWS-SECRET] -t [TABLE-NAME] > table.json
//
// Exports a DynamoDB table into a JSON file

package main

import (
  "bytes"
  "flag"
  "fmt"
  "github.com/bmizerany/aws4"
  "io/ioutil"
  "log"
  "net/http"
  "time"
)

var (
  t = flag.String("t", "", "Table Name")
  k = flag.String("k", "", "AWS Key")
  s = flag.String("s", "", "AWS Secret")

  keys *aws4.Keys
  svc  *aws4.Service
)


func init() {
  fmt.Println("Beginning Init")
  flag.Parse()
  keys = &aws4.Keys{
    AccessKey: *k,
    SecretKey: *s,
  }

  svc = &aws4.Service{
    Name:   "dynamodb",
    Region: "us-east-1",
  }
}

func main() {
  fmt.Println("Beginning Main")
  q := fmt.Sprintf(`{ "TableName": %q }`, *t)
  buf := bytes.NewReader([]byte(q))
  url := "https://dynamodb.us-east-1.amazonaws.com/"
  req, _ := http.NewRequest("POST", url, buf)

  req.Header.Set("Date", time.Now().UTC().Format(http.TimeFormat))
  req.Header.Set("X-Amz-Target", "DynamoDB_20111205.Scan")
  req.Header.Set("Content-Type", "application/x-amz-json-1.0")

  err := svc.Sign(keys, req)
  if err != nil {
    log.Fatalf("fn=Sign error=%q", err)
  }

  res, err := http.DefaultClient.Do(req)
  if err != nil {
    log.Fatalf("fn=Do error=%q", err)
  }

  defer res.Body.Close()
  payload, err := ioutil.ReadAll(res.Body)
  if err != nil {
    log.Fatalf("fn=ReadAll error=%q", err)
  }

  fmt.Printf("%s", payload)
}