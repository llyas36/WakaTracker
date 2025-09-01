package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
)

func handle(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	password := ""
	credentials := fmt.Sprintf("%s:%s", username, password)
	//	encodedCredentials := base64.StdEncoding.EncodeToString([]byte(credentials))

	url := "https://wakatime.com/api/v1/users/current/stats/last_7_days"

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		log.Fatal(err)

	}
	req.Header.Set("Authorization", "Basic "+credentials)

	client := http.Client{}
	res, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	body, err := io.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Fprintf(w, string(body))

}

func Day_7(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	url := "https://wakatime.com/api/v1/users/current/stats/last_7_days"
	auth := fmt.Sprintf("%s:%s", "", "")

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		panic(err)
	}

	req.Header.Set("Authorization", "Basic "+auth)

	client := http.DefaultClient
	res, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	body, err := io.ReadAll(res.Body)
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()
	var data map[string]any
	err = json.Unmarshal(body, &data)
	if err != nil {
		panic(err)
	}
	assertData := data["data"].(map[string]interface{})
	//categories := assertData["categories"].([]interface{})
	//languages := assertData["languages"].([]interface{})
	projects := assertData["projects"].([]interface{})
	jsonDD, err := json.Marshal(projects)

	if err != nil {
		panic(err)
	}
	type Activity struct {
		Name    string  `json:"name"`
		Percent float64 `json:"percent"`
		Text    string  `json:"text"`
	}
	var activity []Activity
	jsonerr := json.Unmarshal([]byte(jsonDD), &activity)
	if jsonerr != nil {
		panic(jsonerr)
	}

	for _, a := range activity {
		fmt.Printf("%s → %s\nPercent → %v\n", a.Name, a.Text, a.Percent)
	}

	container, _ := json.Marshal(activity)

	fmt.Fprintf(w, string(container))

}

func dailyAverage(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	url := "https://wakatime.com/api/v1/users/current/stats/last_7_days"
	auth := fmt.Sprintf("%s:%s", "waka_be54f6f1-3b2b-4785-8ad8-2f9ba0b920f6", "")

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		panic(err)
	}

	req.Header.Set("Authorization", "Basic "+auth)
}
func main() {

	http.HandleFunc("/", handle)
	fmt.Println("server running")

	http.ListenAndServe(":8080", nil)

}
