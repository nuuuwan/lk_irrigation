# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_10:27:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,285 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 10:27:00 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:23:55 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:21:09 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.008 |  |
| 2026-09-27 10:18:05 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 10:16:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:15:35 | Thawalama (Gin Ganga) | 2.56 | 🟢 Normal | -0.035 |  |
| 2026-09-27 10:15:34 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:12:15 | Baddegama (Gin Ganga) | 4.69 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-27 10:12:08 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.054 |  |
| 2026-09-27 10:08:59 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-27 10:07:46 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.049 |  |
| 2026-09-27 10:06:54 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.105 |  |
| 2026-09-27 10:06:42 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-27 10:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.52 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-27 10:06:11 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-09-27 10:06:03 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:05:58 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.030 |  |
| 2026-09-27 10:05:34 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:05:16 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.067 |  |
| 2026-09-27 10:05:00 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.030 |  |
| 2026-09-27 10:04:24 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 10:04:04 | Panadugama (Nilwala Ganga) | 5.37 | 🟡 Alert | -0.030 |  |
| 2026-09-27 10:04:03 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-09-27 10:04:00 | Hanwella (Kelani Ganga) | 4.41 | 🟢 Normal | -0.060 |  |
| 2026-09-27 10:03:35 | Ellagawa (Kalu Ganga) | 8.48 | 🟢 Normal | -0.050 |  |
| 2026-09-27 10:03:20 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-09-27 10:03:17 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:03:04 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-09-27 10:02:54 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 10:02:52 | Rathnapura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.100 |  |
| 2026-09-27 10:02:27 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.189 |  |
| 2026-09-27 10:01:52 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.030 |  |
| 2026-09-27 10:01:46 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.040 |  |
| 2026-09-27 10:01:37 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:01:09 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-27 10:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-09-27 10:01:05 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-09-27 10:01:02 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:00:44 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 10:18:05 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 10:12:15 | Baddegama (Gin Ganga) | 4.69 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-27 10:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.52 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-27 10:04:04 | Panadugama (Nilwala Ganga) | 5.37 | 🟡 Alert | -0.030 |  |
| 2026-09-27 10:08:59 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-27 10:06:42 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-27 10:04:24 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 10:02:54 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 10:00:44 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:06:03 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:16:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:23:55 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:15:34 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:03:17 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:27:00 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:05:34 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:01:37 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:01:02 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 10:21:09 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.008 |  |
| 2026-09-27 10:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-09-27 10:03:04 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-09-27 10:01:09 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-27 10:01:05 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-09-27 10:06:11 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-09-27 10:04:03 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-09-27 10:03:20 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-09-27 10:05:00 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.030 |  |
| 2026-09-27 10:05:58 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.030 |  |
| 2026-09-27 10:01:52 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.030 |  |
| 2026-09-27 10:15:35 | Thawalama (Gin Ganga) | 2.56 | 🟢 Normal | -0.035 |  |
| 2026-09-27 10:01:46 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.040 |  |
| 2026-09-27 10:07:46 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.049 |  |
| 2026-09-27 10:03:35 | Ellagawa (Kalu Ganga) | 8.48 | 🟢 Normal | -0.050 |  |
| 2026-09-27 10:12:08 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.054 |  |
| 2026-09-27 10:04:00 | Hanwella (Kelani Ganga) | 4.41 | 🟢 Normal | -0.060 |  |
| 2026-09-27 10:05:16 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.067 |  |
| 2026-09-27 10:02:52 | Rathnapura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.100 |  |
| 2026-09-27 10:06:54 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.105 |  |
| 2026-09-27 10:02:27 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)