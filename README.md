# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_22:03:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,052 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 22:03:14 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:02:59 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-11-13 22:02:45 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 22:02:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:02:27 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-11-13 22:02:23 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:02:22 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2026-11-13 22:02:19 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:02:16 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:02:12 | Moraketiya (Walawe Ganga) | 3.30 | 🟡 Alert | -0.100 |  |
| 2026-11-13 22:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.70 | 🟡 Alert | -0.041 |  |
| 2026-11-13 22:01:51 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | -0.052 |  |
| 2026-11-13 22:01:47 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:01:37 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:01:37 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.030 |  |
| 2026-11-13 22:01:18 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.071 |  |
| 2026-11-13 22:00:47 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:00:37 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 21:05:06 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-13 21:15:34 | Baddegama (Gin Ganga) | 3.99 | 🟡 Alert | -0.017 |  |
| 2026-11-13 21:08:16 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | -0.037 |  |
| 2026-11-13 22:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.70 | 🟡 Alert | -0.041 |  |
| 2026-11-13 22:02:12 | Moraketiya (Walawe Ganga) | 3.30 | 🟡 Alert | -0.100 |  |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 22:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 22:02:45 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 22:00:47 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:02:16 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:02:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:01:37 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 22:00:37 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:07:10 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-13 21:16:58 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.008 |  |
| 2026-11-13 22:01:47 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:02:23 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:02:19 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:05:13 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:06:18 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:04:10 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:03:14 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:04:57 | Kuda Oya (Kirindi Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-11-13 21:03:33 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-11-13 22:02:59 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-11-13 21:03:03 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-11-13 21:05:03 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.024 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-13 22:01:37 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.030 |  |
| 2026-11-13 21:04:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-11-13 21:06:46 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.039 |  |
| 2026-11-13 22:02:27 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-11-13 22:02:22 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2026-11-13 22:01:51 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | -0.052 |  |
| 2026-11-13 21:20:04 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | -0.056 |  |
| 2026-11-13 22:01:18 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.071 |  |
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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)