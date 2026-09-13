# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_10:07:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,648 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 10:07:43 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 10:07:38 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:07:18 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:07:02 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:06:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.72 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-13 10:06:41 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.059 |  |
| 2026-09-13 10:06:40 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.053 |  |
| 2026-09-13 10:05:40 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:05:22 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-13 10:05:03 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:04:42 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.128 |  |
| 2026-09-13 10:04:37 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.078 |  |
| 2026-09-13 10:04:26 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.059 |  |
| 2026-09-13 10:04:14 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 10:04:13 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:03:15 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 10:02:57 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.041 |  |
| 2026-09-13 10:02:55 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:02:42 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:02:42 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-13 10:02:25 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:02:20 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-13 10:02:15 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-13 10:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:01:40 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 10:01:35 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:01:21 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:01:14 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.135 |  |
| 2026-09-13 10:01:13 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:00:51 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:00:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:00:23 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-13 09:20:27 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 09:17:14 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 10:02:15 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-13 10:02:42 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-13 10:06:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.72 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-13 10:05:22 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-13 10:02:20 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-13 10:03:15 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 10:04:14 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 10:01:40 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 10:07:43 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 09:13:26 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 10:01:35 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:02:55 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:00:23 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:01:13 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 09:01:05 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:01:21 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 09:09:33 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:05:03 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:07:18 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:02:42 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:00:51 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:07:02 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:00:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:02:25 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:07:38 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:05:40 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:04:13 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 09:03:49 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 10:02:57 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.041 |  |
| 2026-09-13 09:12:44 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.044 |  |
| 2026-09-13 10:06:40 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.053 |  |
| 2026-09-13 10:06:41 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.059 |  |
| 2026-09-13 10:04:26 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.059 |  |
| 2026-09-13 10:04:37 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.078 |  |
| 2026-09-13 09:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.095 |  |
| 2026-09-13 10:04:42 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.128 |  |
| 2026-09-13 10:01:14 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.135 |  |
| 2026-09-13 09:09:46 | Magura (Kalu Ganga) | 3.59 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)