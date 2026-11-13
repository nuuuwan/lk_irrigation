# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_16:03:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,821 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 16:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -0.030 |  |
| 2026-11-13 16:02:42 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-11-13 16:02:40 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:02:35 | Thanamalwila (Kirindi Oya) | 2.07 | 🟢 Normal | -0.030 |  |
| 2026-11-13 16:02:29 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-11-13 16:01:52 | Kuda Oya (Kirindi Oya) | 2.31 | 🟢 Normal | -0.023 |  |
| 2026-11-13 16:01:48 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 16:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:01:35 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:01:31 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:01:28 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.054 |  |
| 2026-11-13 16:01:28 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:01:17 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | -0.133 |  |
| 2026-11-13 16:01:09 | Ellagawa (Kalu Ganga) | 7.69 | 🟢 Normal | -0.070 |  |
| 2026-11-13 16:01:02 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.051 |  |
| 2026-11-13 16:00:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.033 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 15:04:15 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 16:01:48 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 15:17:29 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | -0.017 |  |
| 2026-11-13 15:02:10 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-11-13 16:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -0.030 |  |
| 2026-11-13 16:00:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-13 15:01:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:01:31 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:01:35 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:03:15 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:33 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:28 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:26 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.012 |  |
| 2026-11-13 15:04:11 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-11-13 16:02:40 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:01:28 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-11-13 15:03:02 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:02:42 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-11-13 15:04:25 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | -0.021 |  |
| 2026-11-13 16:01:52 | Kuda Oya (Kirindi Oya) | 2.31 | 🟢 Normal | -0.023 |  |
| 2026-11-13 15:10:37 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.026 |  |
| 2026-11-13 15:05:37 | Pitabeddara (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-11-13 16:02:35 | Thanamalwila (Kirindi Oya) | 2.07 | 🟢 Normal | -0.030 |  |
| 2026-11-13 15:04:50 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | -0.037 |  |
| 2026-11-13 16:02:29 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-11-13 15:05:02 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.040 |  |
| 2026-11-13 15:00:07 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.042 |  |
| 2026-11-13 15:13:03 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.045 |  |
| 2026-11-13 15:12:11 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.045 |  |
| 2026-11-13 15:04:46 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.049 |  |
| 2026-11-13 16:01:02 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.051 |  |
| 2026-11-13 16:01:28 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.054 |  |
| 2026-11-13 15:04:50 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.060 |  |
| 2026-11-13 16:01:09 | Ellagawa (Kalu Ganga) | 7.69 | 🟢 Normal | -0.070 |  |
| 2026-11-13 15:02:20 | Peradeniya (Mahaweli Ganga) | 3.83 | 🟢 Normal | -0.096 |  |
| 2026-11-13 15:07:53 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.109 |  |
| 2026-11-13 16:01:17 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)