# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_17:08:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,349 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 17:08:23 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:08:19 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:07:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.61 | 🟢 Normal | -0.038 |  |
| 2026-10-19 17:06:16 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-19 17:05:42 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-10-19 17:05:26 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-10-19 17:05:17 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-19 17:04:54 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-19 17:04:51 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-19 17:04:47 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.021 |  |
| 2026-10-19 17:04:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.012 |  |
| 2026-10-19 17:04:44 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.051 |  |
| 2026-10-19 17:04:43 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.038 |  |
| 2026-10-19 17:04:20 | Ellagawa (Kalu Ganga) | 6.81 | 🟢 Normal | -0.087 |  |
| 2026-10-19 17:03:57 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | -0.071 |  |
| 2026-10-19 17:03:40 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:03:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:03:17 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:02:45 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 17:02:42 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.050 |  |
| 2026-10-19 17:02:38 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:02:35 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.015 |  |
| 2026-10-19 17:02:33 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-19 17:02:21 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-19 17:02:16 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:01:58 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.059 |  |
| 2026-10-19 17:01:49 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-19 17:01:28 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.015 |  |
| 2026-10-19 17:01:24 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.070 |  |
| 2026-10-19 17:01:22 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:00:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 16:03:22 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-19 16:05:12 | Panadugama (Nilwala Ganga) | 5.18 | 🟡 Alert | -0.029 |  |
| 2026-10-19 17:05:17 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-19 17:04:51 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-19 17:06:16 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-19 17:02:45 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 16:05:44 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-19 17:00:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:10:36 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:01:22 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:03:26 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:03:40 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:08:23 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:08:19 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:02:16 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:03:17 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:03:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:13:36 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-19 17:01:49 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-19 17:02:21 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-19 17:02:33 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-19 17:04:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.012 |  |
| 2026-10-19 17:01:28 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.015 |  |
| 2026-10-19 17:02:35 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.015 |  |
| 2026-10-19 17:04:54 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-19 17:05:42 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-10-19 17:05:26 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-10-19 17:04:47 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.021 |  |
| 2026-10-19 16:09:50 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.030 |  |
| 2026-10-19 17:04:43 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.038 |  |
| 2026-10-19 17:07:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.61 | 🟢 Normal | -0.038 |  |
| 2026-10-19 17:02:42 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.050 |  |
| 2026-10-19 17:04:44 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.051 |  |
| 2026-10-19 17:01:58 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.059 |  |
| 2026-10-19 17:01:24 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.070 |  |
| 2026-10-19 17:03:57 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | -0.071 |  |
| 2026-10-19 16:09:31 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.074 |  |
| 2026-10-19 17:04:20 | Ellagawa (Kalu Ganga) | 6.81 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)