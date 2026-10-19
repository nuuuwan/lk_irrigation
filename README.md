# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_11:07:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,112 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 11:07:22 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.021 |  |
| 2026-10-19 11:07:14 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-10-19 11:07:13 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-19 11:07:13 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 11:07:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:06:31 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:06:14 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.024 |  |
| 2026-10-19 11:06:10 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:05:54 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.050 |  |
| 2026-10-19 11:05:17 | Moragaswewa (Deduru Oya) | 1.73 | 🟢 Normal | -0.037 |  |
| 2026-10-19 11:05:05 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-10-19 11:04:37 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:04:23 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.069 |  |
| 2026-10-19 11:04:09 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.019 |  |
| 2026-10-19 11:03:46 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-10-19 11:03:32 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 11:03:06 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.022 |  |
| 2026-10-19 11:02:49 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-10-19 11:02:35 | Panadugama (Nilwala Ganga) | 5.36 | 🟡 Alert | -0.032 |  |
| 2026-10-19 11:02:34 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.101 |  |
| 2026-10-19 11:02:27 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-10-19 11:02:18 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-19 11:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:02:08 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-19 11:02:01 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.040 |  |
| 2026-10-19 11:01:51 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-10-19 11:01:27 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-10-19 11:01:21 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.011 |  |
| 2026-10-19 11:01:19 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-19 11:01:06 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.042 |  |
| 2026-10-19 11:00:56 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:00:46 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.500 |  |
| 2026-10-19 11:00:31 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 11:00:31 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:00:11 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-10-19 10:59:34 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.500 |  |
| 2026-10-19 10:32:46 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 11:00:31 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 11:02:35 | Panadugama (Nilwala Ganga) | 5.36 | 🟡 Alert | -0.032 |  |
| 2026-10-19 11:01:51 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-10-19 11:01:19 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-19 11:07:13 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 11:03:32 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 11:07:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:06:10 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:00:31 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:00:56 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:04:37 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-19 11:06:31 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:14:30 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-10-19 11:01:27 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-10-19 11:02:18 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-19 11:02:08 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:08:41 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-19 11:05:05 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-10-19 11:01:21 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.011 |  |
| 2026-10-19 11:02:27 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-10-19 11:04:09 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.019 |  |
| 2026-10-19 11:07:13 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-19 11:02:49 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-10-19 11:07:22 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.021 |  |
| 2026-10-19 11:03:06 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.022 |  |
| 2026-10-19 11:06:14 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.024 |  |
| 2026-10-19 11:07:14 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-10-19 10:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.029 |  |
| 2026-10-19 11:03:46 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-10-19 11:05:17 | Moragaswewa (Deduru Oya) | 1.73 | 🟢 Normal | -0.037 |  |
| 2026-10-19 11:02:01 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.040 |  |
| 2026-10-19 11:00:11 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-10-19 11:01:06 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.042 |  |
| 2026-10-19 11:05:54 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.050 |  |
| 2026-10-19 11:04:23 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.069 |  |
| 2026-10-19 11:02:34 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.101 |  |
| 2026-10-19 10:00:38 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.110 |  |
| 2026-10-19 11:00:46 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.500 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)