# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_00:08:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,011 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 00:08:11 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.049 |  |
| 2026-09-26 00:07:52 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 00:07:49 | Kithulgala (Kelani Ganga) | 2.90 | 🟢 Normal | -0.102 |  |
| 2026-09-26 00:06:01 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-26 00:05:57 | Nawalapitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-09-26 00:05:33 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-26 00:05:27 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:05:21 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-09-26 00:05:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:05:09 | Rathnapura (Kalu Ganga) | 5.73 | 🟡 Alert | -0.048 |  |
| 2026-09-26 00:05:05 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 00:05:04 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 00:04:40 | Thawalama (Gin Ganga) | 3.40 | 🟢 Normal | -0.054 |  |
| 2026-09-26 00:04:26 | Deraniyagala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.175 |  |
| 2026-09-26 00:04:19 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:03:52 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:03:30 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-09-26 00:03:21 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.034 |  |
| 2026-09-26 00:03:17 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:03:05 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:03:04 | Panadugama (Nilwala Ganga) | 6.23 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-26 00:03:01 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-09-26 00:02:49 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:02:37 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:02:28 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-26 00:02:23 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 00:01:51 | Glencourse (Kelani Ganga) | 13.90 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-26 00:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:01:41 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:01:23 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:00:50 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 23:43:31 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:31:32 | Pitabeddara (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.049 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 23:09:00 | Baddegama (Gin Ganga) | 4.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 00:00:50 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 00:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 00:03:04 | Panadugama (Nilwala Ganga) | 6.23 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-26 00:03:21 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.034 |  |
| 2026-09-26 00:05:09 | Rathnapura (Kalu Ganga) | 5.73 | 🟡 Alert | -0.048 |  |
| 2026-09-26 00:01:51 | Glencourse (Kelani Ganga) | 13.90 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-26 00:02:28 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-26 00:05:04 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 00:07:52 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 23:05:10 | Hanwella (Kelani Ganga) | 5.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 00:05:05 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 00:01:23 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:03:05 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:03:17 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:04:19 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:01:55 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:05:27 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:05:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:02:49 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:02:37 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:01:41 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:03:52 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:06:01 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-26 00:05:33 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-26 00:05:21 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-09-26 00:03:30 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-26 00:03:01 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-09-25 23:06:06 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-09-26 00:05:57 | Nawalapitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-09-25 23:03:17 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.048 |  |
| 2026-09-26 00:08:11 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.049 |  |
| 2026-09-26 00:04:40 | Thawalama (Gin Ganga) | 3.40 | 🟢 Normal | -0.054 |  |
| 2026-09-26 00:07:49 | Kithulgala (Kelani Ganga) | 2.90 | 🟢 Normal | -0.102 |  |
| 2026-09-26 00:04:26 | Deraniyagala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)