# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_18:08:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,380 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 18:08:32 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:07:31 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 18:06:20 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:05:06 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.013 |  |
| 2026-09-29 18:04:59 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:48 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 18:04:39 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:04:18 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:08 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | -0.059 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:03:58 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -0.073 |  |
| 2026-09-29 18:03:54 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:03:27 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:03:24 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:03:21 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.117 |  |
| 2026-09-29 18:02:58 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.068 |  |
| 2026-09-29 18:02:56 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:56 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:45 | Baddegama (Gin Ganga) | 2.91 | 🟢 Normal | -0.030 |  |
| 2026-09-29 18:02:37 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-09-29 18:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:24 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:14 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 18:02:13 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | -0.040 |  |
| 2026-09-29 18:02:07 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:01:48 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.103 |  |
| 2026-09-29 18:01:32 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:01:26 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2026-09-29 18:01:20 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-09-29 18:01:02 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:58 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.154 |  |
| 2026-09-29 18:00:28 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:59:25 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 18:01:26 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2026-09-29 18:04:48 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 18:07:31 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 18:02:14 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:03:54 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:58 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:03:24 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-29 17:59:25 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:24 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:56 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:07 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:59 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:06:20 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:01:02 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:03:27 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:18 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:28 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:56 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:08:32 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:01:32 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:04:39 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:05:06 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.013 |  |
| 2026-09-29 18:01:20 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-09-29 18:02:45 | Baddegama (Gin Ganga) | 2.91 | 🟢 Normal | -0.030 |  |
| 2026-09-29 18:02:13 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | -0.040 |  |
| 2026-09-29 18:02:37 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-09-29 18:04:08 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | -0.059 |  |
| 2026-09-29 18:02:58 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.068 |  |
| 2026-09-29 18:03:58 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -0.073 |  |
| 2026-09-29 18:01:48 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.103 |  |
| 2026-09-29 18:03:21 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.117 |  |
| 2026-09-29 18:00:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)