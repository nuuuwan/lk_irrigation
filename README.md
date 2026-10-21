# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_22:21:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,352 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 22:21:00 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:16:14 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-21 22:14:52 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-21 22:12:12 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-21 22:12:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-21 22:08:34 | Holombuwa (Kelani Ganga) | 1.89 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-10-21 22:08:33 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 22:07:44 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:07:36 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-21 22:07:26 | Rathnapura (Kalu Ganga) | 4.39 | 🟢 Normal | 0.893 | 🔺 Rising |
| 2026-10-21 22:06:53 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-21 22:04:59 | Deraniyagala (Kelani Ganga) | 2.71 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-10-21 22:04:46 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:04:43 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-21 22:04:29 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-21 22:04:23 | Siyambalanduwa (Heda Oya) | 3.19 | 🟢 Normal | 0.584 | 🔺 Rising |
| 2026-10-21 22:04:07 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 22:04:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:03:56 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 22:03:48 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-10-21 22:03:36 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 22:03:29 | Wellawaya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.060 |  |
| 2026-10-21 22:03:28 | Nakkala (Kumbukkan Oya) | 1.49 | 🟢 Normal | -0.112 |  |
| 2026-10-21 22:03:09 | Kithulgala (Kelani Ganga) | 2.65 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-21 22:02:38 | Yaka Wewa (Ma Oya) | 1.85 | 🟢 Normal | -0.049 |  |
| 2026-10-21 22:02:22 | Moragaswewa (Deduru Oya) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 22:02:13 | Nawalapitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.113 |  |
| 2026-10-21 22:02:10 | Thanamalwila (Kirindi Oya) | 2.23 | 🟢 Normal | 0.755 | 🔺 Rising |
| 2026-10-21 22:01:52 | Pitabeddara (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.021 |  |
| 2026-10-21 22:01:45 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:01:22 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 22:01:22 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-10-21 22:00:55 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:00:29 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 22:00:18 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 22:07:26 | Rathnapura (Kalu Ganga) | 4.39 | 🟢 Normal | 0.893 | 🔺 Rising |
| 2026-10-21 22:02:10 | Thanamalwila (Kirindi Oya) | 2.23 | 🟢 Normal | 0.755 | 🔺 Rising |
| 2026-10-21 22:04:23 | Siyambalanduwa (Heda Oya) | 3.19 | 🟢 Normal | 0.584 | 🔺 Rising |
| 2026-10-21 22:08:34 | Holombuwa (Kelani Ganga) | 1.89 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-10-21 22:01:22 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-10-21 22:04:59 | Deraniyagala (Kelani Ganga) | 2.71 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-10-21 22:03:09 | Kithulgala (Kelani Ganga) | 2.65 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-21 22:07:36 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-21 22:04:43 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-21 22:06:53 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-21 22:12:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-21 22:04:29 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-21 22:03:36 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 22:08:33 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 22:12:12 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-21 22:14:52 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-21 22:02:22 | Moragaswewa (Deduru Oya) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 22:01:22 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 22:04:07 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 22:00:29 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 22:03:56 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 22:16:14 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-21 20:04:28 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 22:04:46 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:00:55 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:01:45 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:04:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:21:00 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:01:52 | Pitabeddara (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.021 |  |
| 2026-10-21 22:03:48 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-10-21 22:00:18 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-10-21 22:02:38 | Yaka Wewa (Ma Oya) | 1.85 | 🟢 Normal | -0.049 |  |
| 2026-10-21 22:03:29 | Wellawaya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.060 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-21 21:07:16 | Peradeniya (Mahaweli Ganga) | 4.12 | 🟢 Normal | -0.074 |  |
| 2026-10-21 22:03:28 | Nakkala (Kumbukkan Oya) | 1.49 | 🟢 Normal | -0.112 |  |
| 2026-10-21 22:02:13 | Nawalapitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)