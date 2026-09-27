# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_15:05:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,475 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 15:05:37 | Baddegama (Gin Ganga) | 4.60 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-27 15:05:24 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:05:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.005 |  |
| 2026-09-27 15:05:04 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-09-27 15:05:02 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-09-27 15:04:45 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.091 |  |
| 2026-09-27 15:04:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:04:41 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:04:11 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-09-27 15:04:07 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:03:55 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:03:55 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | -0.073 |  |
| 2026-09-27 15:03:37 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:03:34 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:03:27 | Putupaula (Kalu Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:03:14 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.031 |  |
| 2026-09-27 15:03:05 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:03:04 | Rathnapura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.060 |  |
| 2026-09-27 15:02:42 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:02:41 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:02:36 | Ellagawa (Kalu Ganga) | 8.21 | 🟢 Normal | -0.072 |  |
| 2026-09-27 15:02:33 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-09-27 15:02:29 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.021 |  |
| 2026-09-27 15:02:10 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:02:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:01:57 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.051 |  |
| 2026-09-27 15:01:50 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:01:40 | Weraganthota (Mahaweli Ganga) | -3.52 | 🟢 Normal | -0.020 |  |
| 2026-09-27 15:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:01:20 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:01:18 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 15:00:53 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:00:44 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:00:10 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:29:14 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 15:01:18 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 15:05:37 | Baddegama (Gin Ganga) | 4.60 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-27 14:18:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | -0.017 |  |
| 2026-09-27 15:03:14 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.031 |  |
| 2026-09-27 14:03:59 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-09-27 15:00:10 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:00:44 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:04:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:02:10 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:02:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:05:24 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:00:53 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:01:50 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:02:41 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:03:55 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:01:20 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:02:42 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:03:37 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:05:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.005 |  |
| 2026-09-27 15:05:02 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-09-27 15:04:07 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:03:27 | Putupaula (Kalu Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:04:41 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:03:05 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:03:34 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-27 14:00:48 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-09-27 15:02:33 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-09-27 15:04:11 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-09-27 15:05:04 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-09-27 15:01:40 | Weraganthota (Mahaweli Ganga) | -3.52 | 🟢 Normal | -0.020 |  |
| 2026-09-27 15:02:29 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.021 |  |
| 2026-09-27 14:02:11 | Magura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.049 |  |
| 2026-09-27 15:01:57 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.051 |  |
| 2026-09-27 15:03:04 | Rathnapura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.060 |  |
| 2026-09-27 15:02:36 | Ellagawa (Kalu Ganga) | 8.21 | 🟢 Normal | -0.072 |  |
| 2026-09-27 15:03:55 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | -0.073 |  |
| 2026-09-27 15:04:45 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.091 |  |
| 2026-09-27 14:12:15 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -1.317 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)