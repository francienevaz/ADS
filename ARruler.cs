using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
using UnityEngine.UI;

public class ARRuler : MonoBehaviour
{
    [Header("UI")]
    public Button measureButton;
    public Text resultText;

    [Header("AR")]
    public ARRaycastManager arRaycastManager;
    public GameObject markerPrefab; // Prefab de uma esfera ou ícone para marcar pontos

    private List<ARRaycastHit> hits = new List<ARRaycastHit>();
    private List<GameObject> markers = new List<GameObject>();
    private LineRenderer lineRenderer;

    void Start()
    {
        lineRenderer = GetComponent<LineRenderer>();
        measureButton.onClick.AddListener(CalculateDistance);
    }

    void Update()
    {
        // Detecta toques para colocar marcadores
        if (Input.touchCount > 0 && Input.GetTouch(0).phase == TouchPhase.Began)
        {
            Touch touch = Input.GetTouch(0);
            
            if (arRaycastManager.Raycast(touch.position, hits, TrackableType.PlaneWithinPolygon))
            {
                Pose hitPose = hits[0].pose;
                
                // Limpa marcadores anteriores se já houver 2
                if (markers.Count >= 2)
                {
                    ClearMarkers();
                }

                // Cria um novo marcador
                GameObject marker = Instantiate(markerPrefab, hitPose.position, Quaternion.identity);
                markers.Add(marker);
            }
        }

        // Atualiza a linha entre os marcadores
        if (markers.Count == 2)
        {
            lineRenderer.positionCount = 2;
            lineRenderer.SetPosition(0, markers[0].transform.position);
            lineRenderer.SetPosition(1, markers[1].transform.position);
        }
    }

    void CalculateDistance()
    {
        if (markers.Count == 2)
        {
            float distance = Vector3.Distance(markers[0].transform.position, markers[1].transform.position);
            resultText.text = $"Distância: {distance:F2}m | {distance * 100:F1}cm";
        }
    }

    void ClearMarkers()
    {
        foreach (GameObject marker in markers)
        {
            Destroy(marker);
        }
        markers.Clear();
        lineRenderer.positionCount = 0;
        resultText.text = "";
    }
}
