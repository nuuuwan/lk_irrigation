# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_22:05:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,599 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 22:05:17 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.064 |  |
| 2026-09-18 22:05:05 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:04:54 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-18 22:04:17 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 22:03:33 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-18 22:03:32 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:03:29 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:03:28 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:03:15 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-09-18 22:03:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:02:58 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:49 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:02:46 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:38 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-18 22:02:38 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-09-18 22:02:30 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-18 22:02:16 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:15 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:02:09 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:07 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:01:21 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:01:01 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:00:25 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 21:04:09 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-09-18 22:02:38 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-09-18 22:02:38 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-18 21:01:02 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-18 22:03:33 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-18 22:04:54 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-18 22:02:30 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-18 21:03:22 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-18 22:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 22:01:01 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 21:02:08 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:03:28 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 21:04:14 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:46 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:09 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-09-18 21:10:51 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:00:25 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:01:21 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 21:05:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-18 21:07:28 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:58 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 21:01:40 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:16 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:03:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:04:17 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:03:32 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:05:05 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-18 21:02:53 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.012 |  |
| 2026-09-18 22:02:49 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:02:07 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:02:15 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:03:29 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-09-18 22:03:15 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-09-18 21:03:07 | Baddegama (Gin Ganga) | 2.85 | 🟢 Normal | -0.053 |  |
| 2026-09-18 22:05:17 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)