# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_23:35:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,670 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 23:35:20 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.013 |  |
| 2026-10-28 23:21:42 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:10:41 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-28 23:09:07 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | 0.000 |  |
| 2026-10-28 23:08:20 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:08:19 | Thawalama (Gin Ganga) | 3.17 | 🟢 Normal | -0.045 |  |
| 2026-10-28 23:07:53 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 23:07:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-28 23:07:44 | Hanwella (Kelani Ganga) | 4.17 | 🟢 Normal | -0.019 |  |
| 2026-10-28 23:06:51 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.039 |  |
| 2026-10-28 23:06:35 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.038 |  |
| 2026-10-28 23:06:29 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-10-28 23:06:02 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 23:05:52 | Rathnapura (Kalu Ganga) | 5.61 | 🟡 Alert | -0.061 |  |
| 2026-10-28 23:05:46 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 23:05:18 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:05:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-10-28 23:04:28 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.045 |  |
| 2026-10-28 23:04:24 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.123 |  |
| 2026-10-28 23:04:14 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-10-28 23:04:09 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:04:08 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-10-28 23:03:35 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:03:30 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:03:26 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:03:21 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.139 |  |
| 2026-10-28 23:03:20 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:03:18 | Panadugama (Nilwala Ganga) | 6.14 | 🟠 Minor Flood | -0.024 |  |
| 2026-10-28 23:02:59 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:01:58 | Ellagawa (Kalu Ganga) | 10.29 | 🟡 Alert | -0.020 |  |
| 2026-10-28 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:01:07 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | -0.122 |  |
| 2026-10-28 23:00:21 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:00:09 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 23:06:02 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 22:12:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.64 | 🟠 Minor Flood | -0.008 |  |
| 2026-10-28 23:10:41 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-28 23:03:18 | Panadugama (Nilwala Ganga) | 6.14 | 🟠 Minor Flood | -0.024 |  |
| 2026-10-28 23:09:07 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | 0.000 |  |
| 2026-10-28 23:01:58 | Ellagawa (Kalu Ganga) | 10.29 | 🟡 Alert | -0.020 |  |
| 2026-10-28 22:08:39 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.044 |  |
| 2026-10-28 23:05:52 | Rathnapura (Kalu Ganga) | 5.61 | 🟡 Alert | -0.061 |  |
| 2026-10-28 23:07:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 23:07:53 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 23:05:46 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 23:00:21 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:00:09 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:03:26 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:03:30 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:21:42 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:03:35 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:05:18 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:04:09 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:03:20 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:02:59 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:08:20 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:35:20 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.013 |  |
| 2026-10-28 23:07:44 | Hanwella (Kelani Ganga) | 4.17 | 🟢 Normal | -0.019 |  |
| 2026-10-28 23:04:08 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-10-28 23:04:14 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-10-28 23:05:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-10-28 23:06:29 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-10-28 23:06:35 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.038 |  |
| 2026-10-28 23:06:51 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.039 |  |
| 2026-10-28 23:08:19 | Thawalama (Gin Ganga) | 3.17 | 🟢 Normal | -0.045 |  |
| 2026-10-28 23:04:28 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.045 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-28 23:01:07 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | -0.122 |  |
| 2026-10-28 23:04:24 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.123 |  |
| 2026-10-28 23:03:21 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)