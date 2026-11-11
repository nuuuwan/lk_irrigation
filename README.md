# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_17:32:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,083 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 17:32:16 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-11 17:14:43 | Magura (Kalu Ganga) | 3.89 | 🟢 Normal | 0.510 | 🔺 Rising |
| 2026-11-11 17:14:16 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.017 |  |
| 2026-11-11 17:12:44 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-11-11 17:11:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:10:11 | Panadugama (Nilwala Ganga) | 5.42 | 🟡 Alert | -0.038 |  |
| 2026-11-11 17:10:06 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-11 17:09:25 | Baddegama (Gin Ganga) | 4.12 | 🟠 Minor Flood | -0.019 |  |
| 2026-11-11 17:08:41 | Thanamalwila (Kirindi Oya) | 2.02 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-11-11 17:07:22 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-11 17:06:57 | Moragaswewa (Deduru Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:06:52 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-11 17:06:41 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-11-11 17:06:35 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 17:06:33 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.038 |  |
| 2026-11-11 17:06:11 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.021 |  |
| 2026-11-11 17:04:48 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.029 |  |
| 2026-11-11 17:04:36 | Rathnapura (Kalu Ganga) | 4.18 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-11 17:04:28 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-11 17:04:27 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:04:14 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-11 17:03:51 | Moragaswewa (Deduru Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:03:43 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.50 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-11 17:02:59 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:02:52 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-11 17:02:41 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-11 17:02:36 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-11 17:02:28 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.053 |  |
| 2026-11-11 17:02:24 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:02:23 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:02:07 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-11-11 17:01:57 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-11-11 17:01:48 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:01:27 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.020 |  |
| 2026-11-11 17:01:11 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:01:07 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-11 17:01:05 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.050 |  |
| 2026-11-11 17:00:57 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:00:25 | Moraketiya (Walawe Ganga) | 2.40 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-11-11 17:00:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 16:59:46 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 16:56:42 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 17:06:35 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 17:09:25 | Baddegama (Gin Ganga) | 4.12 | 🟠 Minor Flood | -0.019 |  |
| 2026-11-11 17:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.50 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-11 17:14:16 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.017 |  |
| 2026-11-11 17:10:11 | Panadugama (Nilwala Ganga) | 5.42 | 🟡 Alert | -0.038 |  |
| 2026-11-11 17:14:43 | Magura (Kalu Ganga) | 3.89 | 🟢 Normal | 0.510 | 🔺 Rising |
| 2026-11-11 17:01:57 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-11-11 17:00:25 | Moraketiya (Walawe Ganga) | 2.40 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-11-11 17:06:41 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-11-11 17:08:41 | Thanamalwila (Kirindi Oya) | 2.02 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-11-11 17:07:22 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-11 17:04:14 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-11 17:10:06 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-11 17:04:36 | Rathnapura (Kalu Ganga) | 4.18 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-11 17:06:52 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-11 17:02:36 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-11 17:02:41 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-11 17:32:16 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-11 17:04:28 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-11 17:01:07 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-11 17:00:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:06:57 | Moragaswewa (Deduru Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:11:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:04:27 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:01:48 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:02:24 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:02:59 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:03:43 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:00:57 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:01:11 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-11-11 17:12:44 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-11-11 17:02:52 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-11 17:02:07 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-11-11 17:01:27 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.020 |  |
| 2026-11-11 17:06:11 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.021 |  |
| 2026-11-11 17:04:48 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.029 |  |
| 2026-11-11 17:06:33 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.038 |  |
| 2026-11-11 17:01:05 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.050 |  |
| 2026-11-11 17:02:28 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)