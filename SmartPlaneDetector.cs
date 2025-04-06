using UnityEngine;
using UnityEngine.XR.ARFoundation;
using System.Collections.Generic;
using UnityEngine.XR.ARSubsystems;

public class SmartPlaneDetector : MonoBehaviour
{
    private ARPlaneManager _arPlaneManager;
    private List<ARPlane> _trackedPlanes = new List<ARPlane>();
    private float _similarityThreshold = 0.1f;

    void OnEnable()
    {
        _arPlaneManager = GetComponent<ARPlaneManager>();
        if (_arPlaneManager == null)
        {
            Debug.LogError("ARPlaneManager não encontrado!");
            return;
        }

        // Nova forma correta de assinar eventos na versão 6.0+
        _arPlaneManager.trackablesChanged += OnTrackablesChanged;
    }

    void OnDisable()
    {
        if (_arPlaneManager != null)
            _arPlaneManager.trackablesChanged -= OnTrackablesChanged;
    }

    void OnTrackablesChanged(ARTrackablesChangedEventArgs<ARPlane> args)
    {
        // Adiciona novos planos à lista (se forem realmente novos)
        foreach (var newPlane in args.added)
        {
            if (!IsPlaneSimilarToTracked(newPlane))
            {
                _trackedPlanes.Add(newPlane);
                Debug.Log($"Plano adicionado: {newPlane.trackableId}");
            }
            else
            {
                Destroy(newPlane.gameObject);
            }
        }

        // Remove planos que foram destruídos pelo sistema
        foreach (var removedPlane in args.removed)
        {
            _trackedPlanes.Remove(removedPlane);
        }
    }

    private bool IsPlaneSimilarToTracked(ARPlane plane)
    {
        foreach (var trackedPlane in _trackedPlanes)
        {
            float distance = Vector3.Distance(plane.center, trackedPlane.center);
            if (distance < _similarityThreshold)
            {
                Debug.Log($"Plano similar encontrado! Distância: {distance}");
                return true;
            }
        }
        return false;
    }

    public List<ARPlane> GetTrackedPlanes()
    {
        return new List<ARPlane>(_trackedPlanes);
    }
}