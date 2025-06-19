import SwiftUI

struct Task: Codable, Identifiable {
    let id: Int
    let title: String
}

struct ContentView: View {
    @State private var tasks = [Task]()

    var body: some View {
        List(tasks) { task in
            Text(task.title)
        }
        .onAppear(perform: loadTasks)
    }

    func loadTasks() {
        guard let url = URL(string: "http://192.168.X.X:8000/get_tasks") else { return }

        URLSession.shared.dataTask(with: url) { data, _, _ in
            if let data = data {
                let decoded = try? JSONDecoder().decode([Task].self, from: data)
                DispatchQueue.main.async {
                    self.tasks = decoded ?? []
                }
            }
        }.resume()
    }
}

