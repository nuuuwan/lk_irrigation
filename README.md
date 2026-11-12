# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_20:33:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,096 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 20:33:19 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 20:18:23 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | -0.032 |  |
| 2026-11-12 20:17:38 | Magura (Kalu Ganga) | 4.85 | 🟡 Alert | -0.040 |  |
| 2026-11-12 20:10:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-11-12 20:09:50 | Panadugama (Nilwala Ganga) | 6.38 | 🟠 Minor Flood | 0.080 | 🔺 Rising |
| 2026-11-12 20:07:48 | Urawa (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.442 | 🔺 Rising |
| 2026-11-12 20:07:22 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.061 |  |
| 2026-11-12 20:07:11 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.019 |  |
| 2026-11-12 20:06:40 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 20:05:44 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | -0.142 |  |
| 2026-11-12 20:05:12 | Rathnapura (Kalu Ganga) | 4.90 | 🟢 Normal | -0.043 |  |
| 2026-11-12 20:04:46 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-12 20:04:34 | Thaldena (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.192 |  |
| 2026-11-12 20:03:58 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.041 |  |
| 2026-11-12 20:03:52 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.090 |  |
| 2026-11-12 20:03:38 | Siyambalanduwa (Heda Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-11-12 20:03:36 | Kuda Oya (Kirindi Oya) | 3.15 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-12 20:03:27 | Peradeniya (Mahaweli Ganga) | 4.69 | 🟢 Normal | -0.046 |  |
| 2026-11-12 20:03:27 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | -0.099 |  |
| 2026-11-12 20:03:13 | Glencourse (Kelani Ganga) | 11.99 | 🟢 Normal | -0.010 |  |
| 2026-11-12 20:03:11 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-11-12 20:02:58 | Norwood (Kelani Ganga) | 1.62 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-11-12 20:02:48 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.051 |  |
| 2026-11-12 20:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 20:02:27 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2026-11-12 20:02:23 | Pitabeddara (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.105 |  |
| 2026-11-12 20:02:17 | Wellawaya (Kirindi Oya) | 2.23 | 🟢 Normal | -0.108 |  |
| 2026-11-12 20:02:16 | Katharagama (Menik Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-12 20:02:13 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 20:02:07 | Putupaula (Kalu Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-11-12 20:02:00 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | -0.020 |  |
| 2026-11-12 20:01:58 | Thanamalwila (Kirindi Oya) | 2.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-12 20:01:41 | Moragaswewa (Deduru Oya) | 2.32 | 🟢 Normal | -0.155 |  |
| 2026-11-12 20:01:25 | Nakkala (Kumbukkan Oya) | 2.45 | 🟢 Normal | 0.410 | 🔺 Rising |
| 2026-11-12 20:00:51 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | -0.085 |  |
| 2026-11-12 20:00:11 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 20:09:50 | Panadugama (Nilwala Ganga) | 6.38 | 🟠 Minor Flood | 0.080 | 🔺 Rising |
| 2026-11-12 20:02:13 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 20:33:19 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 20:02:58 | Norwood (Kelani Ganga) | 1.62 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-11-12 20:10:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-11-12 20:18:23 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | -0.032 |  |
| 2026-11-12 20:17:38 | Magura (Kalu Ganga) | 4.85 | 🟡 Alert | -0.040 |  |
| 2026-11-12 20:05:44 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | -0.142 |  |
| 2026-11-12 20:07:48 | Urawa (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.442 | 🔺 Rising |
| 2026-11-12 20:01:25 | Nakkala (Kumbukkan Oya) | 2.45 | 🟢 Normal | 0.410 | 🔺 Rising |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 20:01:58 | Thanamalwila (Kirindi Oya) | 2.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-12 20:03:36 | Kuda Oya (Kirindi Oya) | 3.15 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-12 20:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 20:00:11 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 20:06:40 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-12 20:02:07 | Putupaula (Kalu Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-11-12 20:03:13 | Glencourse (Kelani Ganga) | 11.99 | 🟢 Normal | -0.010 |  |
| 2026-11-12 20:07:11 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.019 |  |
| 2026-11-12 20:03:38 | Siyambalanduwa (Heda Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-11-12 20:03:11 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-11-12 20:02:00 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | -0.020 |  |
| 2026-11-12 20:04:46 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-12 20:02:16 | Katharagama (Menik Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-12 20:03:58 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.041 |  |
| 2026-11-12 20:05:12 | Rathnapura (Kalu Ganga) | 4.90 | 🟢 Normal | -0.043 |  |
| 2026-11-12 20:03:27 | Peradeniya (Mahaweli Ganga) | 4.69 | 🟢 Normal | -0.046 |  |
| 2026-11-12 20:02:48 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.051 |  |
| 2026-11-12 20:02:27 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2026-11-12 20:07:22 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.061 |  |
| 2026-11-12 20:00:51 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | -0.085 |  |
| 2026-11-12 20:03:52 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.090 |  |
| 2026-11-12 20:03:27 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | -0.099 |  |
| 2026-11-12 20:02:23 | Pitabeddara (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.105 |  |
| 2026-11-12 20:02:17 | Wellawaya (Kirindi Oya) | 2.23 | 🟢 Normal | -0.108 |  |
| 2026-11-12 20:01:41 | Moragaswewa (Deduru Oya) | 2.32 | 🟢 Normal | -0.155 |  |
| 2026-11-12 20:04:34 | Thaldena (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)