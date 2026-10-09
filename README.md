# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_08:17:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,992 measurements** from **39** stations.
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
| 2026-10-09 08:17:51 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-10-09 08:13:47 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.026 |  |
| 2026-10-09 08:10:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:06:55 | Badalgama (Maha Oya) | 4.80 | 🟢 Normal | -0.130 |  |
| 2026-10-09 08:05:40 | Baddegama (Gin Ganga) | 2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-09 08:04:54 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.081 |  |
| 2026-10-09 08:04:42 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.180 |  |
| 2026-10-09 08:04:41 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 08:04:23 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.114 |  |
| 2026-10-09 08:04:19 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.056 |  |
| 2026-10-09 08:04:11 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-09 08:04:10 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-10-09 08:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-09 08:03:47 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.038 |  |
| 2026-10-09 08:03:46 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 08:03:41 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.019 |  |
| 2026-10-09 08:03:39 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.164 |  |
| 2026-10-09 08:03:27 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.031 |  |
| 2026-10-09 08:03:20 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-10-09 08:02:36 | Giriulla (Maha Oya) | 3.59 | 🟢 Normal | -0.149 |  |
| 2026-10-09 08:02:36 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:02:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.068 |  |
| 2026-10-09 08:02:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 08:02:17 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-09 08:02:01 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 08:01:58 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:45 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:43 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:42 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:38 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:23 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | -0.146 |  |
| 2026-10-09 08:01:21 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.093 |  |
| 2026-10-09 08:01:17 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.062 |  |
| 2026-10-09 08:00:49 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-10-09 08:00:46 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:00:44 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:00:15 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 08:02:01 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 08:02:17 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-09 08:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 08:05:40 | Baddegama (Gin Ganga) | 2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-09 08:04:41 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 08:03:46 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 08:00:44 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:02:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:00:46 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:02:36 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:38 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:42 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:43 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:01:45 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:10:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-09 08:17:51 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-10-09 08:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-09 08:04:10 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-10-09 08:04:11 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-09 08:00:49 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-10-09 08:03:41 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.019 |  |
| 2026-10-09 08:03:20 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-10-09 08:13:47 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.026 |  |
| 2026-10-09 08:00:15 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-10-09 08:03:27 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.031 |  |
| 2026-10-09 08:03:47 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.038 |  |
| 2026-10-09 08:04:19 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.056 |  |
| 2026-10-09 08:01:17 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.062 |  |
| 2026-10-09 07:08:40 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.066 |  |
| 2026-10-09 08:02:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.068 |  |
| 2026-10-09 08:04:54 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.081 |  |
| 2026-10-09 08:01:21 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.093 |  |
| 2026-10-09 08:04:23 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.114 |  |
| 2026-10-09 08:06:55 | Badalgama (Maha Oya) | 4.80 | 🟢 Normal | -0.130 |  |
| 2026-10-09 08:01:23 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | -0.146 |  |
| 2026-10-09 08:02:36 | Giriulla (Maha Oya) | 3.59 | 🟢 Normal | -0.149 |  |
| 2026-10-09 08:03:39 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.164 |  |
| 2026-10-09 08:04:42 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)