# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_06:09:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,450 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 06:09:53 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.070 |  |
| 2026-11-13 06:09:47 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-13 06:07:53 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.082 |  |
| 2026-11-13 06:07:09 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 06:06:19 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-13 06:06:18 | Panadugama (Nilwala Ganga) | 6.36 | 🟠 Minor Flood | -0.019 |  |
| 2026-11-13 06:05:28 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.133 |  |
| 2026-11-13 06:04:55 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-13 06:04:49 | Badalgama (Maha Oya) | 3.58 | 🟢 Normal | -0.041 |  |
| 2026-11-13 06:04:45 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-13 06:04:44 | Urawa (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-11-13 06:04:15 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 06:03:53 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-13 06:03:47 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 06:03:38 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-13 06:03:38 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | -0.060 |  |
| 2026-11-13 06:03:36 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.020 |  |
| 2026-11-13 06:03:34 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-11-13 06:03:10 | Thawalama (Gin Ganga) | 3.09 | 🟢 Normal | -0.183 |  |
| 2026-11-13 06:02:59 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-11-13 06:02:22 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.051 |  |
| 2026-11-13 06:02:19 | Thanamalwila (Kirindi Oya) | 2.49 | 🟢 Normal | -0.080 |  |
| 2026-11-13 06:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-11-13 06:02:08 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-11-13 06:02:06 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.033 |  |
| 2026-11-13 06:02:03 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 06:01:59 | Moraketiya (Walawe Ganga) | 3.14 | 🟡 Alert | 0.000 |  |
| 2026-11-13 06:01:57 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | -0.032 |  |
| 2026-11-13 06:01:50 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-13 06:01:43 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.230 |  |
| 2026-11-13 06:01:25 | Kuda Oya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.052 |  |
| 2026-11-13 06:01:12 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-11-13 06:00:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | -0.056 |  |
| 2026-11-13 06:00:19 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-13 06:00:05 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-11-13 05:55:10 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | -96.000 |  |
| 2026-11-13 05:55:07 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -96.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 06:07:09 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 06:03:47 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 06:06:18 | Panadugama (Nilwala Ganga) | 6.36 | 🟠 Minor Flood | -0.019 |  |
| 2026-11-13 06:01:59 | Moraketiya (Walawe Ganga) | 3.14 | 🟡 Alert | 0.000 |  |
| 2026-11-13 06:01:57 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | -0.032 |  |
| 2026-11-13 06:00:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | -0.056 |  |
| 2026-11-13 05:55:10 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | -96.000 |  |
| 2026-11-13 06:06:19 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-13 06:01:50 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-13 06:03:53 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-13 06:00:19 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 06:02:03 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 06:09:47 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-13 06:04:45 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-13 06:04:15 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-13 05:02:15 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-13 06:04:55 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-13 06:04:44 | Urawa (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-11-13 06:03:34 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-11-13 06:02:59 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-11-13 06:03:36 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.020 |  |
| 2026-11-13 06:01:12 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-11-13 06:03:38 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-13 06:00:05 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-11-13 06:02:08 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-11-13 06:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-11-13 06:02:06 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.033 |  |
| 2026-11-13 06:04:49 | Badalgama (Maha Oya) | 3.58 | 🟢 Normal | -0.041 |  |
| 2026-11-13 06:02:22 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.051 |  |
| 2026-11-13 06:01:25 | Kuda Oya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.052 |  |
| 2026-11-13 06:03:38 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | -0.060 |  |
| 2026-11-13 06:09:53 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.070 |  |
| 2026-11-13 06:02:19 | Thanamalwila (Kirindi Oya) | 2.49 | 🟢 Normal | -0.080 |  |
| 2026-11-13 06:07:53 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.082 |  |
| 2026-11-13 06:05:28 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.133 |  |
| 2026-11-13 06:03:10 | Thawalama (Gin Ganga) | 3.09 | 🟢 Normal | -0.183 |  |
| 2026-11-13 06:01:43 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.230 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)