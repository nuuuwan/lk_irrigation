# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_15:09:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 15:09:26 | Panadugama (Nilwala Ganga) | 5.90 | 🟡 Alert | -0.009 |  |
| 2026-09-26 15:09:09 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 15:09:05 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-09-26 15:08:39 | Rathnapura (Kalu Ganga) | 5.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-26 15:08:08 | Thawalama (Gin Ganga) | 2.85 | 🟢 Normal | -0.028 |  |
| 2026-09-26 15:07:45 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | -0.072 |  |
| 2026-09-26 15:07:43 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-09-26 15:06:39 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-09-26 15:05:58 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 15:05:38 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:05:26 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-26 15:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 15:05:10 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.031 |  |
| 2026-09-26 15:04:46 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:04:28 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 15:04:27 | Deraniyagala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.171 |  |
| 2026-09-26 15:04:27 | Hanwella (Kelani Ganga) | 5.36 | 🟢 Normal | -0.030 |  |
| 2026-09-26 15:04:17 | Glencourse (Kelani Ganga) | 13.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:03:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:03:31 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:03:12 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 15:03:10 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.070 |  |
| 2026-09-26 15:03:02 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:54 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-09-26 15:02:51 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:46 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.112 |  |
| 2026-09-26 15:02:22 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:20 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-26 15:02:19 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:15 | Ellagawa (Kalu Ganga) | 8.97 | 🟢 Normal | -0.010 |  |
| 2026-09-26 15:02:10 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:05 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:01:47 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.105 |  |
| 2026-09-26 15:01:31 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:01:28 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:01:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:00:49 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:00:23 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:00:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 15:04:28 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 15:03:12 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 15:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 15:09:26 | Panadugama (Nilwala Ganga) | 5.90 | 🟡 Alert | -0.009 |  |
| 2026-09-26 15:08:39 | Rathnapura (Kalu Ganga) | 5.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-26 15:05:58 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 15:09:09 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 15:02:10 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:00:49 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:51 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:01:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:03:02 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:00:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:19 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:04:46 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:03:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:04:17 | Glencourse (Kelani Ganga) | 13.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:01:31 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:02:21 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:03:31 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:05:38 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:05 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:01:28 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:02:22 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 15:06:39 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-09-26 15:05:26 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-26 15:02:20 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-26 15:02:15 | Ellagawa (Kalu Ganga) | 8.97 | 🟢 Normal | -0.010 |  |
| 2026-09-26 15:02:54 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-09-26 15:09:05 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-09-26 15:08:08 | Thawalama (Gin Ganga) | 2.85 | 🟢 Normal | -0.028 |  |
| 2026-09-26 15:07:43 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-09-26 15:04:27 | Hanwella (Kelani Ganga) | 5.36 | 🟢 Normal | -0.030 |  |
| 2026-09-26 15:05:10 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.031 |  |
| 2026-09-26 15:03:10 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.070 |  |
| 2026-09-26 15:07:45 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | -0.072 |  |
| 2026-09-26 15:01:47 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.105 |  |
| 2026-09-26 15:02:46 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.112 |  |
| 2026-09-26 15:04:27 | Deraniyagala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)