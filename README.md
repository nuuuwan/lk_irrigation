# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_13:15:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,194 measurements** from **39** stations.
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
| 2026-10-19 13:15:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | -0.017 |  |
| 2026-10-19 13:08:22 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.015 |  |
| 2026-10-19 13:08:20 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.019 |  |
| 2026-10-19 13:08:12 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 13:08:06 | Panadugama (Nilwala Ganga) | 5.27 | 🟡 Alert | -0.047 |  |
| 2026-10-19 13:07:13 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-10-19 13:06:15 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-19 13:06:05 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-10-19 13:05:58 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:05:47 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:05:39 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-10-19 13:05:11 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-19 13:04:56 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.038 |  |
| 2026-10-19 13:04:53 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.029 |  |
| 2026-10-19 13:04:37 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:04:15 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 13:03:39 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:03:27 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.079 |  |
| 2026-10-19 13:03:25 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-19 13:02:57 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | -0.060 |  |
| 2026-10-19 13:02:51 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.042 |  |
| 2026-10-19 13:02:50 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-10-19 13:02:44 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.084 |  |
| 2026-10-19 13:02:39 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:02:39 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-19 13:02:28 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:02:11 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:01:44 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.021 |  |
| 2026-10-19 13:01:41 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:01:32 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-19 13:01:16 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-10-19 13:01:01 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-10-19 13:01:01 | Moragaswewa (Deduru Oya) | 1.61 | 🟢 Normal | -0.052 |  |
| 2026-10-19 13:00:46 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:00:39 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:59:06 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 13:08:12 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 13:08:06 | Panadugama (Nilwala Ganga) | 5.27 | 🟡 Alert | -0.047 |  |
| 2026-10-19 13:03:25 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-19 13:04:15 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 13:02:11 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:00:39 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:05:58 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:02:28 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:59:06 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:00:46 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:03:39 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:05:47 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:04:37 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:02:39 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:01:41 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:08:53 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-10-19 13:07:13 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-10-19 13:05:11 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-19 13:06:15 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-19 13:01:32 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-19 13:06:05 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-10-19 13:08:22 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.015 |  |
| 2026-10-19 13:15:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | -0.017 |  |
| 2026-10-19 13:08:20 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.019 |  |
| 2026-10-19 13:02:50 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-10-19 13:01:44 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.021 |  |
| 2026-10-19 13:05:39 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-10-19 13:04:53 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.029 |  |
| 2026-10-19 13:01:16 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-10-19 13:01:01 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-10-19 13:04:56 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.038 |  |
| 2026-10-19 13:02:51 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.042 |  |
| 2026-10-19 13:02:39 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-19 13:01:01 | Moragaswewa (Deduru Oya) | 1.61 | 🟢 Normal | -0.052 |  |
| 2026-10-19 13:02:57 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | -0.060 |  |
| 2026-10-19 13:03:27 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.079 |  |
| 2026-10-19 13:02:44 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.084 |  |
| 2026-10-19 12:09:40 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)