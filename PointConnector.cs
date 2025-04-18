using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class PointConnector : MonoBehaviour
{
    public GameObject pointPrefab;
    public LineRenderer linePrefab;
    public TextMeshPro textPrefab;

    private List<GameObject> points = new List<GameObject>();
    private LineRenderer currentLine;
    private TextMeshPro distanceText;

    public void AddPoint(Vector3 position)
    {
        // Se já houver 2 pontos, resetar tudo
        if (points.Count >= 2)
        {
            foreach (var p in points)
                Destroy(p);
            points.Clear();

            if (currentLine != null)
                Destroy(currentLine.gameObject);

            if (distanceText != null)
                Destroy(distanceText.gameObject);
        }

        // Criar novo ponto
        GameObject point = Instantiate(pointPrefab, position, Quaternion.identity);
        points.Add(point);

        // Quando tiver 2 pontos, desenhar a linha e mostrar distância
        if (points.Count == 2)
        {
            Vector3 posA = points[0].transform.position;
            Vector3 posB = points[1].transform.position;

            // Criar linha
            currentLine = Instantiate(linePrefab);
            currentLine.positionCount = 2;
            currentLine.SetPosition(0, posA);
            currentLine.SetPosition(1, posB);

            ShowDistance(posA, posB);
        }
    }

    private void ShowDistance(Vector3 posA, Vector3 posB)
    {
        float distance = Vector3.Distance(posA, posB);
        string formatted = (distance * 100f).ToString("F1") + " cm"; // Converte para centímetros

        // Instanciar texto
        distanceText = Instantiate(textPrefab);
        distanceText.text = formatted;

        // Posicionar no meio da linha, levemente acima
        Vector3 middle = (posA + posB) / 2f;
        distanceText.transform.position = middle + Vector3.up * 0.01f;
    }
}