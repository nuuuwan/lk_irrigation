# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_16:17:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,746 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 16:17:41 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:15:28 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-02 16:10:08 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:10:07 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:08:49 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:08:37 | Katharagama (Menik Ganga) | 0.41 | 🟢 Normal | -0.018 |  |
| 2026-01-02 16:08:11 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:05:53 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:05:43 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-02 16:05:32 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:05:28 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:05:16 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-01-02 16:05:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.088 |  |
| 2026-01-02 16:04:14 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:03:58 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:03:55 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.182 |  |
| 2026-01-02 16:03:54 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 16:03:52 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:03:44 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 16:03:24 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:03:11 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-01-02 16:02:55 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-01-02 16:02:25 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:02:11 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.051 |  |
| 2026-01-02 16:01:36 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:01:31 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-02 16:01:26 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-01-02 16:01:21 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:01:11 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:00:57 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.040 |  |
| 2026-01-02 16:00:20 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | -0.060 |  |
| 2026-01-02 16:00:16 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-02 16:00:11 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:00:07 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 16:01:31 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-02 16:05:43 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-02 15:12:23 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-02 16:15:28 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-02 16:03:54 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 16:03:44 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 16:03:58 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:05:28 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:00:07 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:03:24 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:10:08 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:08:49 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:01:11 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:08:11 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:05:32 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:05:53 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:17:41 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:03:52 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:04:14 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:02:55 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:01:21 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:01:36 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:02:25 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-02 16:00:11 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:02:44 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-01-02 16:08:37 | Katharagama (Menik Ganga) | 0.41 | 🟢 Normal | -0.018 |  |
| 2026-01-02 16:05:16 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-01-02 16:00:16 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-02 16:03:11 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-01-02 16:00:57 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.040 |  |
| 2026-01-02 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-01-02 16:01:26 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-01-02 16:02:11 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.051 |  |
| 2026-01-02 15:04:27 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-01-02 16:00:20 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | -0.060 |  |
| 2026-01-02 16:05:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.088 |  |
| 2026-01-02 16:03:55 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)