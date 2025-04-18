using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
using System.Collections.Generic;

[RequireComponent(typeof(ARPlaneManager))]
public class SmartPlaneDetector : MonoBehaviour
{
    private ARPlaneManager _arPlaneManager;
    private List<ARPlane> _trackedPlanes = new List<ARPlane>();
    private ARPlane _currentActivePlane;
    private float _similarityThreshold = 0.1f;
    private float _planeActivationDistance = 0.5f;

    void OnEnable()
    {
        _arPlaneManager = GetComponent<ARPlaneManager>();
        if (_arPlaneManager == null)
        {
            Debug.LogError("ARPlaneManager não encontrado!");
            return;
        }

        // AR FOUNDATION 5.x: correto
        _arPlaneManager.planesChanged += OnPlanesChanged;
    }

    void OnDisable()
    {
        if (_arPlaneManager != null)
            _arPlaneManager.planesChanged -= OnPlanesChanged;
    }

    void Update()
    {
        if (_currentActivePlane != null)
        {
            float distanceToPlane = Vector3.Distance(
                Camera.main.transform.position,
                _currentActivePlane.transform.position
            );

            if (distanceToPlane > _planeActivationDistance * 2f)
            {
                SetPlaneActive(_currentActivePlane, false);
                _currentActivePlane = null;
            }
        }

        foreach (var tracked in _trackedPlanes)
        {
            if (tracked == _currentActivePlane) continue;

            float distance = Vector3.Distance(
                Camera.main.transform.position,
                tracked.transform.position
            );

            if (distance < _planeActivationDistance)
            {
                ActivateSinglePlane(tracked);
                break;
            }
        }
    }

    private void OnPlanesChanged(ARPlanesChangedEventArgs args)
    {
        foreach (var newPlane in args.added)
        {
            if (!IsPlaneSimilarToTracked(newPlane))
            {
                _trackedPlanes.Add(newPlane);
                Debug.Log($"Plano adicionado: {newPlane.trackableId}");
                SetPlaneActive(newPlane, false);
            }
            else
            {
                Destroy(newPlane.gameObject);
            }
        }

        foreach (var removed in args.removed)
        {
            _trackedPlanes.Remove(removed);
            if (_currentActivePlane == removed)
                _currentActivePlane = null;
        }
    }

    private void ActivateSinglePlane(ARPlane plane)
    {
        foreach (var p in _trackedPlanes)
        {
            SetPlaneActive(p, false);
        }

        SetPlaneActive(plane, true);
        _currentActivePlane = plane;
    }

    private void SetPlaneActive(ARPlane plane, bool active)
    {
        if (plane == null) return;

        var meshRenderer = plane.GetComponent<MeshRenderer>();
        if (meshRenderer != null) meshRenderer.enabled = active;

        var lineRenderer = plane.GetComponent<LineRenderer>();
        if (lineRenderer != null) lineRenderer.enabled = active;
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

    public ARPlane GetCurrentActivePlane()
    {
        return _currentActivePlane;
    }

    public List<ARPlane> GetTrackedPlanes()
    {
        return new List<ARPlane>(_trackedPlanes);
    }
}
