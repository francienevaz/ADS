using UnityEngine;
using UnityEngine.XR.ARFoundation;
using TMPro;
using System.Collections.Generic;
using UnityEngine.XR.ARSubsystems;

public class MedicaoAR : MonoBehaviour
{
    [Header("Referências")]
    public ARRaycastManager raycastManager;
    public SmartPlaneDetector planeDetector;
    public GameObject initialPointPrefab;
    public GameObject finalPointPrefab;
    public LineRenderer measurementLine;
    public TextMeshProUGUI distanceTextTMP;

    [Header("Configurações")]
    public float maxTouchDistance = 100f; // Distância máxima em pixels para considerar toque em um plano
    public float minMeasurementDistance = 0.05f; // Distância mínima entre pontos em metros
    public float verticalOffset = 0.1f; // Offset vertical para posicionar os pontos acima do plano

    private GameObject initialPointInstance;
    private GameObject finalPointInstance;
    private bool isMeasuring = false;
    private bool measurementValid = false;

    void Start()
    {
        // Inicializa o texto
        if (distanceTextTMP != null)
        {
            distanceTextTMP.text = "Toque para colocar o primeiro ponto";
        }

        // Configura escala inicial dos prefabs (opcional)
        if (initialPointPrefab != null)
            initialPointPrefab.transform.localScale = new Vector3(0.1f, 0.1f, 0.1f);
        if (finalPointPrefab != null)
            finalPointPrefab.transform.localScale = new Vector3(0.1f, 0.1f, 0.1f);
    }

    void Update()
    {
        if (Input.touchCount == 0) return;

        Touch touch = Input.GetTouch(0);
        if (touch.phase != TouchPhase.Began) return;

        // Verifica primeiro os planos já rastreados
        if (planeDetector != null)
        {
            foreach (var plane in planeDetector.GetTrackedPlanes())
            {
                Vector2 screenPoint = Camera.main.WorldToScreenPoint(plane.center);
                if (Vector2.Distance(touch.position, screenPoint) < maxTouchDistance)
                {
                    ProcessHit(new Pose(plane.center, plane.transform.rotation));
                    return;
                }
            }
        }

        // Fallback para raycast tradicional
        List<ARRaycastHit> hits = new List<ARRaycastHit>();
        if (raycastManager.Raycast(touch.position, hits, TrackableType.PlaneWithinPolygon))
        {
            ProcessHit(hits[0].pose);
        }
        else
        {
            Debug.Log("Nenhum plano detectado.");
            if (distanceTextTMP != null)
            {
                distanceTextTMP.text = "Nenhum plano detectado. Aponte para uma superfície plana.";
            }
        }
    }

    private bool IsPointOnActivePlane(Vector3 position)
    {
        if (planeDetector == null) return true;
        
        var activePlane = planeDetector.GetCurrentActivePlane();
        if (activePlane == null) return true;
        
        // Verifica se o ponto está próximo o suficiente do plano ativo
        return Vector3.Distance(position, activePlane.center) < 0.3f;
    }

    private void ProcessHit(Pose hitPose)
    {
        // Ajusta a posição com offset vertical
        Vector3 adjustedPosition = hitPose.position + Vector3.up * verticalOffset;

        if (!IsPointOnActivePlane(hitPose.position))
        {
            Debug.Log("Ponto fora do plano ativo");
            if (distanceTextTMP != null)
            {
                distanceTextTMP.text = "Toque no plano ativo para medir";
            }
            return;
        }

        if (!isMeasuring)
        {
            // Primeiro ponto
            if (initialPointInstance == null)
            {
                initialPointInstance = Instantiate(initialPointPrefab, adjustedPosition, hitPose.rotation);
            }
            else
            {
                initialPointInstance.transform.position = adjustedPosition;
            }
            
            isMeasuring = true;
            measurementValid = false;
            
            if (distanceTextTMP != null)
            {
                distanceTextTMP.text = "Toque para colocar o segundo ponto";
            }
        }
        else
        {
            // Segundo ponto
            // Verifica distância mínima
            float distance = Vector3.Distance(initialPointInstance.transform.position, adjustedPosition);
            if (distance < minMeasurementDistance)
            {
                Debug.Log("Distância muito pequena entre os pontos");
                if (distanceTextTMP != null)
                {
                    distanceTextTMP.text = "Mova mais para colocar o segundo ponto";
                }
                return;
            }

            if (finalPointInstance == null)
            {
                finalPointInstance = Instantiate(finalPointPrefab, adjustedPosition, hitPose.rotation);
            }
            else
            {
                finalPointInstance.transform.position = adjustedPosition;
            }
            
            isMeasuring = false;
            measurementValid = true;
            UpdateMeasurement();
        }
    }

    private void UpdateMeasurement()
    {
        if (measurementValid && initialPointInstance != null && finalPointInstance != null)
        {
            // Atualiza a linha
            measurementLine.positionCount = 2;
            measurementLine.SetPosition(0, initialPointInstance.transform.position);
            measurementLine.SetPosition(1, finalPointInstance.transform.position);

            // Calcula distância
            float distance = Vector3.Distance(
                initialPointInstance.transform.position,
                finalPointInstance.transform.position
            );

            // Converte para cm se menor que 1m
            string unit = "m";
            if (distance < 1f)
            {
                distance *= 100f;
                unit = "cm";
            }

            if (distanceTextTMP != null)
            {
                distanceTextTMP.text = $"Distância: {distance:F2} {unit}";
            }
        }
        else
        {
            // Reseta a linha se não houver medição válida
            measurementLine.positionCount = 0;
        }
    }

    public void ResetMeasurement()
    {
        if (initialPointInstance != null) Destroy(initialPointInstance);
        if (finalPointInstance != null) Destroy(finalPointInstance);
        
        measurementLine.positionCount = 0;
        isMeasuring = false;
        measurementValid = false;
        
        if (distanceTextTMP != null)
        {
            distanceTextTMP.text = "Toque para colocar o primeiro ponto";
        }
    }

    // Método para ajustar a escala dos pontos (pode ser chamado externamente se necessário)
    public void SetPointsScale(float scale)
    {
        if (initialPointInstance != null)
            initialPointInstance.transform.localScale = new Vector3(scale, scale, scale);
        if (finalPointInstance != null)
            finalPointInstance.transform.localScale = new Vector3(scale, scale, scale);
    }
}