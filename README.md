# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_15:17:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,805 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 15:17:29 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | -0.017 |  |
| 2026-11-13 15:13:03 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.045 |  |
| 2026-11-13 15:12:11 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.045 |  |
| 2026-11-13 15:10:37 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.026 |  |
| 2026-11-13 15:10:31 | Kuda Oya (Kirindi Oya) | 2.33 | 🟢 Normal | -0.009 |  |
| 2026-11-13 15:07:53 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.109 |  |
| 2026-11-13 15:05:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-13 15:05:37 | Pitabeddara (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-11-13 15:05:25 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:05:02 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.040 |  |
| 2026-11-13 15:04:50 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | -0.037 |  |
| 2026-11-13 15:04:50 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.060 |  |
| 2026-11-13 15:04:46 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.049 |  |
| 2026-11-13 15:04:25 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | -0.021 |  |
| 2026-11-13 15:04:18 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:04:15 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 15:04:11 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-11-13 15:03:33 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:26 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.012 |  |
| 2026-11-13 15:03:15 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:08 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 15:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -0.030 |  |
| 2026-11-13 15:03:02 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-11-13 15:02:58 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-13 15:02:39 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.078 |  |
| 2026-11-13 15:02:34 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.058 |  |
| 2026-11-13 15:02:33 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-11-13 15:02:27 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:02:20 | Peradeniya (Mahaweli Ganga) | 3.83 | 🟢 Normal | -0.096 |  |
| 2026-11-13 15:02:10 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-11-13 15:02:07 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.040 |  |
| 2026-11-13 15:01:53 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:01:35 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:01:32 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.050 |  |
| 2026-11-13 15:01:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:01:15 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.025 |  |
| 2026-11-13 15:01:11 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:28 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:07 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 15:02:58 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-13 15:04:15 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 15:17:29 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | -0.017 |  |
| 2026-11-13 15:02:10 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-11-13 15:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -0.030 |  |
| 2026-11-13 15:05:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-13 15:01:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:01:11 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:01:53 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:04:18 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:10:31 | Kuda Oya (Kirindi Oya) | 2.33 | 🟢 Normal | -0.009 |  |
| 2026-11-13 15:05:25 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:15 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:02:27 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:33 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:01:35 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:28 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:26 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.012 |  |
| 2026-11-13 15:04:11 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-11-13 15:03:02 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-11-13 15:04:25 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | -0.021 |  |
| 2026-11-13 15:01:15 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.025 |  |
| 2026-11-13 15:10:37 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.026 |  |
| 2026-11-13 15:05:37 | Pitabeddara (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-11-13 15:04:50 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | -0.037 |  |
| 2026-11-13 15:02:07 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.040 |  |
| 2026-11-13 15:05:02 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.040 |  |
| 2026-11-13 15:02:33 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-11-13 15:00:07 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.042 |  |
| 2026-11-13 15:13:03 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.045 |  |
| 2026-11-13 15:12:11 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.045 |  |
| 2026-11-13 15:04:46 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.049 |  |
| 2026-11-13 15:01:32 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.050 |  |
| 2026-11-13 15:02:34 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.058 |  |
| 2026-11-13 15:04:50 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.060 |  |
| 2026-11-13 15:02:39 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.078 |  |
| 2026-11-13 15:02:20 | Peradeniya (Mahaweli Ganga) | 3.83 | 🟢 Normal | -0.096 |  |
| 2026-11-13 15:07:53 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)