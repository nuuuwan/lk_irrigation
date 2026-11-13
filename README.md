# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_05:30:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,413 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 05:30:23 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.048 |  |
| 2026-11-13 05:24:47 | Norwood (Kelani Ganga) | 1.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-13 05:23:10 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.007 |  |
| 2026-11-13 05:18:10 | Rathnapura (Kalu Ganga) | 4.26 | 🟢 Normal | -0.088 |  |
| 2026-11-13 05:16:50 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | -0.078 |  |
| 2026-11-13 05:13:20 | Ellagawa (Kalu Ganga) | 8.15 | 🟢 Normal | -0.026 |  |
| 2026-11-13 05:10:47 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | -0.089 |  |
| 2026-11-13 05:08:21 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.213 |  |
| 2026-11-13 05:07:45 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.046 |  |
| 2026-11-13 05:07:39 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-13 05:07:02 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-13 05:06:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.009 |  |
| 2026-11-13 05:06:04 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | -0.030 |  |
| 2026-11-13 05:05:52 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-11-13 05:05:21 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-11-13 05:05:04 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | -0.092 |  |
| 2026-11-13 05:03:55 | Panadugama (Nilwala Ganga) | 6.38 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-13 05:03:53 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.049 |  |
| 2026-11-13 05:03:49 | Kuda Oya (Kirindi Oya) | 2.70 | 🟢 Normal | -0.118 |  |
| 2026-11-13 05:03:45 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.038 |  |
| 2026-11-13 05:03:16 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-11-13 05:03:06 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-11-13 05:03:05 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.029 |  |
| 2026-11-13 05:02:52 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.021 |  |
| 2026-11-13 05:02:37 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-13 05:02:27 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 05:02:26 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-13 05:02:15 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-13 05:02:12 | Thanamalwila (Kirindi Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-11-13 05:01:40 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 05:01:36 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 05:01:31 | Moraketiya (Walawe Ganga) | 3.14 | 🟡 Alert | 0.000 |  |
| 2026-11-13 05:01:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 05:02:27 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 05:01:36 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 05:03:55 | Panadugama (Nilwala Ganga) | 6.38 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-13 05:01:31 | Moraketiya (Walawe Ganga) | 3.14 | 🟡 Alert | 0.000 |  |
| 2026-11-13 04:14:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.18 | 🟡 Alert | 0.000 |  |
| 2026-11-13 04:12:55 | Magura (Kalu Ganga) | 4.26 | 🟡 Alert | -0.084 |  |
| 2026-11-13 05:05:04 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | -0.092 |  |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-13 05:24:47 | Norwood (Kelani Ganga) | 1.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-13 05:02:37 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-13 05:02:26 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 05:01:40 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 05:07:02 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-13 05:23:10 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.007 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-13 05:06:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.009 |  |
| 2026-11-13 05:07:39 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-13 05:02:15 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-13 05:02:12 | Thanamalwila (Kirindi Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-11-13 05:05:52 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-11-13 05:05:21 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-11-13 05:02:52 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.021 |  |
| 2026-11-13 05:13:20 | Ellagawa (Kalu Ganga) | 8.15 | 🟢 Normal | -0.026 |  |
| 2026-11-13 05:03:06 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-11-13 05:03:05 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.029 |  |
| 2026-11-13 05:06:04 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | -0.030 |  |
| 2026-11-13 05:03:16 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-11-13 05:01:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.034 |  |
| 2026-11-13 05:03:45 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.038 |  |
| 2026-11-13 05:07:45 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.046 |  |
| 2026-11-13 05:30:23 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.048 |  |
| 2026-11-13 05:03:53 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.049 |  |
| 2026-11-13 05:16:50 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | -0.078 |  |
| 2026-11-13 05:00:11 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.088 |  |
| 2026-11-13 05:18:10 | Rathnapura (Kalu Ganga) | 4.26 | 🟢 Normal | -0.088 |  |
| 2026-11-13 05:10:47 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | -0.089 |  |
| 2026-11-13 05:03:49 | Kuda Oya (Kirindi Oya) | 2.70 | 🟢 Normal | -0.118 |  |
| 2026-11-13 05:08:21 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)