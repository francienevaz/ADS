using UnityEngine;
using UnityEngine.XR.ARFoundation;
using TMPro;
using System.Collections.Generic;

public class MedicaoAR : MonoBehaviour
{   
    public ARRaycastManager raycastManager;
    public GameObject initialPointPrefab;
    public GameObject finalPointPrefab;
    public LineRenderer measurementLine;
    public TextMeshProUGUI distanceTextTMP;
    public SmartPlaneDetector planeDetector; 

    private GameObject initialPointInstance;
    private GameObject finalPointInstance;
    private int pointsPlaced = 0;

    void Update()
    {
        // Modo otimizado (usa planos já rastreados)
        if (Input.touchCount > 0 && planeDetector != null)
        {
            Touch touch = Input.GetTouch(0);

            if (touch.phase == TouchPhase.Began)
            {
                bool planeFound = false;
                
                // Primeiro verifica se tocou em um plano já rastreado
                foreach (var plane in planeDetector.GetTrackedPlanes())
                {
                    Vector2 screenPoint = Camera.main.WorldToScreenPoint(plane.center);
                    if (Vector2.Distance(touch.position, screenPoint) < 100f) // Distância em pixels
                    {
                        planeFound = true;
                        ProcessHit(new Pose(plane.center, plane.transform.rotation));
                        break;
                    }
                }

                // Se não encontrou um plano rastreado, usa raycast tradicional
                if (!planeFound)
                {
                    List<ARRaycastHit> hits = new List<ARRaycastHit>();
                    if (raycastManager.Raycast(touch.position, hits, UnityEngine.XR.ARSubsystems.TrackableType.PlaneWithinPolygon))
                    {
                        ProcessHit(hits[0].pose);
                    }
                    else
                    {
                        Debug.Log("❌ Nenhum plano detectado.");
                    }
                }
            }
        }

        // Atualiza a linha e texto de distância
        UpdateMeasurement();
    }

    private void ProcessHit(Pose hitPose)
    {
        Debug.Log("✅ Hit em plano detectado!");
        
        if (pointsPlaced == 0)
        {
            if (initialPointInstance == null)
            {
                initialPointInstance = Instantiate(initialPointPrefab, hitPose.position, hitPose.rotation);
            }
            else
            {
                initialPointInstance.transform.position = hitPose.position;
            }
            pointsPlaced = 1;
        }
        else if (pointsPlaced == 1)
        {
            if (finalPointInstance == null)
            {
                finalPointInstance = Instantiate(finalPointPrefab, hitPose.position, hitPose.rotation);
            }
            else
            {
                finalPointInstance.transform.position = hitPose.position;
            }
            pointsPlaced = 2;
        }
        else if (pointsPlaced == 2)
        {
            // Reset para nova medição
            Destroy(initialPointInstance);
            Destroy(finalPointInstance);
            pointsPlaced = 0;
        }
    }

    private void UpdateMeasurement()
    {
        if (pointsPlaced == 2 && initialPointInstance != null && finalPointInstance != null)
        {
            measurementLine.SetPosition(0, initialPointInstance.transform.position);
            measurementLine.SetPosition(1, finalPointInstance.transform.position);

            float distance = Vector3.Distance(initialPointInstance.transform.position, finalPointInstance.transform.position);
            string unit = "m";
            if (distance < 1f)
            {
                distance *= 100f;
                unit = "cm";
            }

            if (distanceTextTMP != null)
            {
                distanceTextTMP.text = $"{distance:F2} {unit}";
            }
        }
        else if (pointsPlaced < 2 && measurementLine != null)
        {
            measurementLine.SetPosition(0, Vector3.zero);
            measurementLine.SetPosition(1, Vector3.zero);

            if (distanceTextTMP != null)
            {
                distanceTextTMP.text = "";
            }
        }
    }
}