# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_15:15:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,474 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 15:15:18 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | -0.056 |  |
| 2026-10-27 15:09:56 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:09:40 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | -0.049 |  |
| 2026-10-27 15:08:24 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-10-27 15:06:40 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-27 15:05:53 | Galgamuwa (Mee Oya) | 4.04 | 🟢 Normal | -0.021 |  |
| 2026-10-27 15:05:28 | Rathnapura (Kalu Ganga) | 8.10 | 🟠 Minor Flood | -0.078 |  |
| 2026-10-27 15:05:28 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 15:05:17 | Putupaula (Kalu Ganga) | 3.36 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 15:04:54 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:04:49 | Glencourse (Kelani Ganga) | 12.64 | 🟢 Normal | -0.121 |  |
| 2026-10-27 15:04:48 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-10-27 15:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.58 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-10-27 15:03:57 | Badalgama (Maha Oya) | 4.53 | 🟢 Normal | -0.126 |  |
| 2026-10-27 15:03:52 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-27 15:03:29 | Pitabeddara (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.030 |  |
| 2026-10-27 15:03:21 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:03:14 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.112 |  |
| 2026-10-27 15:03:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:03:02 | Ellagawa (Kalu Ganga) | 10.05 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 15:02:50 | Hanwella (Kelani Ganga) | 5.75 | 🟢 Normal | -0.119 |  |
| 2026-10-27 15:02:46 | Moragaswewa (Deduru Oya) | 4.96 | 🟡 Alert | -0.139 |  |
| 2026-10-27 15:02:34 | Panadugama (Nilwala Ganga) | 6.26 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-27 15:02:34 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-27 15:02:26 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 15:02:21 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | -0.050 |  |
| 2026-10-27 15:02:21 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:02:14 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-27 15:02:12 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.119 |  |
| 2026-10-27 15:01:56 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 15:01:53 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.010 |  |
| 2026-10-27 15:01:52 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 15:01:49 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:01:46 | Giriulla (Maha Oya) | 3.37 | 🟢 Normal | -0.068 |  |
| 2026-10-27 15:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.021 |  |
| 2026-10-27 15:01:33 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:01:01 | Moraketiya (Walawe Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-10-27 15:00:44 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:00:34 | Horowpothana (Yan Oya) | 3.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 15:00:10 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 15:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.58 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-10-27 15:06:40 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-27 15:05:28 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 15:02:34 | Panadugama (Nilwala Ganga) | 6.26 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-27 15:05:28 | Rathnapura (Kalu Ganga) | 8.10 | 🟠 Minor Flood | -0.078 |  |
| 2026-10-27 15:05:17 | Putupaula (Kalu Ganga) | 3.36 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 15:03:02 | Ellagawa (Kalu Ganga) | 10.05 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 15:02:26 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 15:15:18 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | -0.056 |  |
| 2026-10-27 15:02:46 | Moragaswewa (Deduru Oya) | 4.96 | 🟡 Alert | -0.139 |  |
| 2026-10-27 15:00:34 | Horowpothana (Yan Oya) | 3.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 15:01:52 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 15:01:56 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 15:00:44 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:01:49 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:03:21 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:04:54 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:00:10 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:03:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:09:56 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:02:21 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-27 15:02:34 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-27 15:02:14 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-27 15:03:52 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-27 15:01:53 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.010 |  |
| 2026-10-27 15:08:24 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-10-27 15:04:48 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-10-27 15:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.021 |  |
| 2026-10-27 15:05:53 | Galgamuwa (Mee Oya) | 4.04 | 🟢 Normal | -0.021 |  |
| 2026-10-27 15:01:01 | Moraketiya (Walawe Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-10-27 15:03:29 | Pitabeddara (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.030 |  |
| 2026-10-27 15:09:40 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | -0.049 |  |
| 2026-10-27 15:02:21 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | -0.050 |  |
| 2026-10-27 15:01:46 | Giriulla (Maha Oya) | 3.37 | 🟢 Normal | -0.068 |  |
| 2026-10-27 15:03:14 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.112 |  |
| 2026-10-27 15:02:50 | Hanwella (Kelani Ganga) | 5.75 | 🟢 Normal | -0.119 |  |
| 2026-10-27 15:02:12 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.119 |  |
| 2026-10-27 15:04:49 | Glencourse (Kelani Ganga) | 12.64 | 🟢 Normal | -0.121 |  |
| 2026-10-27 15:03:57 | Badalgama (Maha Oya) | 4.53 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)