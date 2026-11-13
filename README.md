# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_21:20:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,033 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 21:20:04 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | -0.056 |  |
| 2026-11-13 21:16:58 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.008 |  |
| 2026-11-13 21:15:34 | Baddegama (Gin Ganga) | 3.99 | 🟡 Alert | -0.017 |  |
| 2026-11-13 21:09:43 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | -0.103 |  |
| 2026-11-13 21:08:16 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | -0.037 |  |
| 2026-11-13 21:07:10 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:07:02 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:06:46 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.039 |  |
| 2026-11-13 21:06:18 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:05:20 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:05:13 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:05:06 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-13 21:05:03 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.024 |  |
| 2026-11-13 21:04:57 | Kuda Oya (Kirindi Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:04:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-11-13 21:04:20 | Putupaula (Kalu Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:04:19 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.040 |  |
| 2026-11-13 21:04:10 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:03:33 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-11-13 21:03:10 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.060 |  |
| 2026-11-13 21:03:03 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-11-13 21:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.74 | 🟡 Alert | -0.042 |  |
| 2026-11-13 21:02:52 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:02:47 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.050 |  |
| 2026-11-13 21:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 21:02:28 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.060 |  |
| 2026-11-13 21:02:26 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:02:11 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.071 |  |
| 2026-11-13 21:02:09 | Magura (Kalu Ganga) | 2.87 | 🟢 Normal | -180.000 |  |
| 2026-11-13 21:02:08 | Magura (Kalu Ganga) | 2.92 | 🟢 Normal | -180.000 |  |
| 2026-11-13 21:02:07 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:02:01 | Moraketiya (Walawe Ganga) | 3.40 | 🟡 Alert | -0.294 |  |
| 2026-11-13 21:01:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:01:25 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.039 |  |
| 2026-11-13 21:00:24 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:00:11 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:00:08 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 21:05:06 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-13 21:15:34 | Baddegama (Gin Ganga) | 3.99 | 🟡 Alert | -0.017 |  |
| 2026-11-13 21:08:16 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | -0.037 |  |
| 2026-11-13 21:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.74 | 🟡 Alert | -0.042 |  |
| 2026-11-13 21:02:01 | Moraketiya (Walawe Ganga) | 3.40 | 🟡 Alert | -0.294 |  |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 21:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 21:00:24 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:01:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:02:07 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:07:02 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:02:26 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:07:10 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:16:58 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.008 |  |
| 2026-11-13 21:05:20 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:05:13 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:06:18 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:00:11 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:02:52 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:04:20 | Putupaula (Kalu Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:04:10 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:00:08 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:04:57 | Kuda Oya (Kirindi Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:03:33 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-11-13 21:03:03 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-11-13 21:05:03 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.024 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-13 21:04:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-11-13 21:06:46 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.039 |  |
| 2026-11-13 21:01:25 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.039 |  |
| 2026-11-13 21:04:19 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.040 |  |
| 2026-11-13 21:02:47 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.050 |  |
| 2026-11-13 21:20:04 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | -0.056 |  |
| 2026-11-13 21:03:10 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.060 |  |
| 2026-11-13 21:02:28 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.060 |  |
| 2026-11-13 21:02:11 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.071 |  |
| 2026-11-13 21:09:43 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | -0.103 |  |
| 2026-11-13 21:02:09 | Magura (Kalu Ganga) | 2.87 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)