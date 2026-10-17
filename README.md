# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_21:22:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,697 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Norwood — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **50** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 21:22:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:22:00 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:21:58 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-17 21:20:59 | Thaldena (Mahaweli Ganga) | 1.21 | 🟢 Normal | 270.000 | 🔺 Rising |
| 2026-10-17 21:20:57 | Thaldena (Mahaweli Ganga) | 1.06 | 🟢 Normal | 270.000 | 🔺 Rising |
| 2026-10-17 21:15:23 | Urawa (Nilwala Ganga) | 1.71 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-17 21:15:16 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-10-17 21:13:56 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -288.000 |  |
| 2026-10-17 21:13:55 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -288.000 |  |
| 2026-10-17 21:13:53 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -288.000 |  |
| 2026-10-17 21:13:52 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | -288.000 |  |
| 2026-10-17 21:13:27 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-10-17 21:12:00 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | -0.027 |  |
| 2026-10-17 21:08:50 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:08:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:08:17 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-17 21:07:22 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | 0.101 | 🔺 Rising |
| 2026-10-17 21:06:42 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:06:39 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 21:06:34 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-10-17 21:06:25 | Padiyathalawa (Maduru Oya) | 3.40 | 🟢 Normal | -1.161 |  |
| 2026-10-17 21:06:23 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-10-17 21:06:08 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -144.000 |  |
| 2026-10-17 21:06:06 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -144.000 |  |
| 2026-10-17 21:06:05 | Ellagawa (Kalu Ganga) | 7.24 | 🟢 Normal | -144.000 |  |
| 2026-10-17 21:06:03 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -144.000 |  |
| 2026-10-17 21:06:01 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -144.000 |  |
| 2026-10-17 21:05:59 | Ellagawa (Kalu Ganga) | 7.37 | 🟢 Normal | -144.000 |  |
| 2026-10-17 21:05:57 | Ellagawa (Kalu Ganga) | 7.46 | 🟢 Normal | -144.000 |  |
| 2026-10-17 21:05:55 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-10-17 21:05:35 | Holombuwa (Kelani Ganga) | 3.15 | 🟡 Alert | -0.150 |  |
| 2026-10-17 21:05:32 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.138 |  |
| 2026-10-17 21:05:27 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | 1.192 | 🔺 Rising |
| 2026-10-17 21:05:19 | Thaldena (Mahaweli Ganga) | 1.21 | 🟢 Normal | 270.000 | 🔺 Rising |
| 2026-10-17 21:04:49 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-17 21:04:35 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:04:31 | Rathnapura (Kalu Ganga) | 6.30 | 🟡 Alert | 0.151 | 🔺 Rising |
| 2026-10-17 21:04:09 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.084 |  |
| 2026-10-17 21:03:25 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.355 |  |
| 2026-10-17 21:03:15 | Pitabeddara (Nilwala Ganga) | 3.40 | 🟢 Normal | 1.011 | 🔺 Rising |
| 2026-10-17 21:03:10 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-10-17 21:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.50 | 🟡 Alert | -0.020 |  |
| 2026-10-17 21:02:35 | Norwood (Kelani Ganga) | 1.68 | 🟡 Alert | -0.012 |  |
| 2026-10-17 21:02:35 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:02:30 | Nawalapitiya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.224 |  |
| 2026-10-17 21:02:29 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-10-17 21:02:21 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:02:16 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-17 21:01:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 21:07:22 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | 0.101 | 🔺 Rising |
| 2026-10-17 21:15:16 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-10-17 21:04:31 | Rathnapura (Kalu Ganga) | 6.30 | 🟡 Alert | 0.151 | 🔺 Rising |
| 2026-10-17 21:02:35 | Norwood (Kelani Ganga) | 1.68 | 🟡 Alert | -0.012 |  |
| 2026-10-17 21:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.50 | 🟡 Alert | -0.020 |  |
| 2026-10-17 21:05:35 | Holombuwa (Kelani Ganga) | 3.15 | 🟡 Alert | -0.150 |  |
| 2026-10-17 21:20:59 | Thaldena (Mahaweli Ganga) | 1.21 | 🟢 Normal | 270.000 | 🔺 Rising |
| 2026-10-17 21:05:27 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | 1.192 | 🔺 Rising |
| 2026-10-17 21:03:15 | Pitabeddara (Nilwala Ganga) | 3.40 | 🟢 Normal | 1.011 | 🔺 Rising |
| 2026-10-17 21:03:10 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-10-17 21:08:17 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-17 21:15:23 | Urawa (Nilwala Ganga) | 1.71 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-17 21:04:49 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-17 21:02:16 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-17 21:06:39 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:04:35 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:22:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:08:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:08:50 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:02:21 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:02:35 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:06:42 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:01:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:13:27 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-10-17 21:06:34 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-17 21:05:55 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-10-17 21:06:23 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-10-17 21:12:00 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | -0.027 |  |
| 2026-10-17 21:02:29 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-17 21:04:09 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.084 |  |
| 2026-10-17 21:05:32 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.138 |  |
| 2026-10-17 21:02:30 | Nawalapitiya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.224 |  |
| 2026-10-17 21:03:25 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.355 |  |
| 2026-10-17 21:06:25 | Padiyathalawa (Maduru Oya) | 3.40 | 🟢 Normal | -1.161 |  |
| 2026-10-17 21:06:08 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -144.000 |  |
| 2026-10-17 21:13:56 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -288.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)