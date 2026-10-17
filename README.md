# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_02:05:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,853 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 02:05:11 | Holombuwa (Kelani Ganga) | 1.53 | 🟢 Normal | -0.212 |  |
| 2026-10-18 02:04:58 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.077 |  |
| 2026-10-18 02:04:37 | Moraketiya (Walawe Ganga) | 1.58 | 🟢 Normal | -0.043 |  |
| 2026-10-18 02:04:13 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -180.000 |  |
| 2026-10-18 02:04:11 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -180.000 |  |
| 2026-10-18 02:04:10 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-18 02:04:07 | Rathnapura (Kalu Ganga) | 5.35 | 🟡 Alert | -0.301 |  |
| 2026-10-18 02:03:59 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | -0.258 |  |
| 2026-10-18 02:03:30 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.428 |  |
| 2026-10-18 02:03:07 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -288.000 |  |
| 2026-10-18 02:03:07 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-10-18 02:03:06 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -288.000 |  |
| 2026-10-18 02:02:53 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-10-18 02:02:33 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-18 02:02:08 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-10-18 02:01:53 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 02:01:51 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-18 02:01:28 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-18 02:00:26 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-10-18 01:36:54 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 01:09:55 | Panadugama (Nilwala Ganga) | 6.21 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-10-17 23:03:38 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 00:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.44 | 🟡 Alert | -0.023 |  |
| 2026-10-18 02:04:07 | Rathnapura (Kalu Ganga) | 5.35 | 🟡 Alert | -0.301 |  |
| 2026-10-18 02:03:07 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-10-18 01:07:50 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-10-18 00:04:40 | Thawalama (Gin Ganga) | 3.86 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-18 02:04:10 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-18 01:02:32 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-18 01:07:48 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-18 00:09:54 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-18 02:01:53 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 01:02:04 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 02:01:28 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-18 01:14:02 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-18 01:06:45 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 01:09:43 | Urawa (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-18 01:06:53 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | -0.009 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-18 02:01:51 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-18 02:02:33 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-18 02:02:08 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-10-18 01:04:04 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-10-18 02:02:53 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-10-18 01:01:56 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.022 |  |
| 2026-10-18 02:00:26 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-18 02:04:37 | Moraketiya (Walawe Ganga) | 1.58 | 🟢 Normal | -0.043 |  |
| 2026-10-18 00:03:42 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.050 |  |
| 2026-10-18 02:04:58 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.077 |  |
| 2026-10-18 01:05:32 | Glencourse (Kelani Ganga) | 13.21 | 🟢 Normal | -0.086 |  |
| 2026-10-18 01:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.208 |  |
| 2026-10-18 02:05:11 | Holombuwa (Kelani Ganga) | 1.53 | 🟢 Normal | -0.212 |  |
| 2026-10-18 02:03:59 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | -0.258 |  |
| 2026-10-18 02:03:30 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.428 |  |
| 2026-10-18 01:11:36 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.919 |  |
| 2026-10-18 02:04:13 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -180.000 |  |
| 2026-10-18 02:03:07 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -288.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)