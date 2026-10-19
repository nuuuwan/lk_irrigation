# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_20:07:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,464 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 20:07:56 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-19 20:07:49 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-10-19 20:07:34 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | -0.025 |  |
| 2026-10-19 20:06:48 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-19 20:06:16 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | -0.029 |  |
| 2026-10-19 20:06:06 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 20:05:57 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-19 20:05:56 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 20:05:30 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 20:05:30 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-10-19 20:05:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-19 20:04:44 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | 1.137 | 🔺 Rising |
| 2026-10-19 20:04:19 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-10-19 20:04:10 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-10-19 20:03:55 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-10-19 20:03:24 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.051 |  |
| 2026-10-19 20:03:01 | Kithulgala (Kelani Ganga) | 2.79 | 🟢 Normal | 0.827 | 🔺 Rising |
| 2026-10-19 20:03:00 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.012 |  |
| 2026-10-19 20:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-10-19 20:02:54 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-10-19 20:02:41 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 20:02:36 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-10-19 20:02:25 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | -0.020 |  |
| 2026-10-19 20:02:22 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.011 |  |
| 2026-10-19 20:02:18 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-19 20:02:12 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-19 20:01:51 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 20:01:39 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.033 |  |
| 2026-10-19 20:01:37 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 20:01:14 | Ellagawa (Kalu Ganga) | 6.59 | 🟢 Normal | -0.071 |  |
| 2026-10-19 20:00:22 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-19 20:00:13 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:29:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 20:07:34 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | -0.025 |  |
| 2026-10-19 19:03:29 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.028 |  |
| 2026-10-19 20:04:44 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | 1.137 | 🔺 Rising |
| 2026-10-19 20:03:01 | Kithulgala (Kelani Ganga) | 2.79 | 🟢 Normal | 0.827 | 🔺 Rising |
| 2026-10-19 20:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-10-19 20:04:19 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-10-19 20:02:18 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-19 20:02:12 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-19 20:06:48 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-19 20:02:41 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 20:05:30 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 20:06:06 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 20:00:13 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 20:01:37 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-19 20:01:51 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 20:05:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-19 20:05:56 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:02:03 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 20:05:30 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-10-19 20:07:56 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-19 20:00:22 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-19 20:05:57 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-19 20:02:22 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.011 |  |
| 2026-10-19 20:03:00 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.012 |  |
| 2026-10-19 19:07:13 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-10-19 20:02:54 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-10-19 20:04:10 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-10-19 20:02:25 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | -0.020 |  |
| 2026-10-19 19:29:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.021 |  |
| 2026-10-19 20:06:16 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | -0.029 |  |
| 2026-10-19 20:07:49 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-10-19 20:03:55 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-10-19 20:01:39 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.033 |  |
| 2026-10-19 20:02:36 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-10-19 20:03:24 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.051 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-19 20:01:14 | Ellagawa (Kalu Ganga) | 6.59 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)