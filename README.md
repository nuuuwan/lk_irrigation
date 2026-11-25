# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_04:02:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,849 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 04:02:45 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.381 | 🔺 Rising |
| 2026-11-26 04:02:37 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.161 |  |
| 2026-11-26 04:02:32 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.011 |  |
| 2026-11-26 04:02:24 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-26 04:02:23 | Peradeniya (Mahaweli Ganga) | 3.54 | 🟢 Normal | -0.177 |  |
| 2026-11-26 04:02:21 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-26 04:02:09 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.070 |  |
| 2026-11-26 04:02:09 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-11-26 04:02:01 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.035 |  |
| 2026-11-26 04:02:00 | Moragaswewa (Deduru Oya) | 2.84 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-11-26 04:01:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-26 04:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.054 |  |
| 2026-11-26 03:45:04 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.070 |  |
| 2026-11-26 03:43:12 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 04:02:21 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-25 20:05:34 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-11-26 04:02:45 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.381 | 🔺 Rising |
| 2026-11-26 04:02:00 | Moragaswewa (Deduru Oya) | 2.84 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-11-25 18:02:46 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-26 03:04:37 | Badalgama (Maha Oya) | 3.91 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-26 03:07:25 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-26 04:02:24 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-26 03:04:48 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-26 02:02:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-26 04:01:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-26 03:01:50 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-26 03:03:14 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-26 03:03:00 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-26 02:00:15 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-26 03:43:12 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.007 |  |
| 2026-11-26 04:02:32 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.011 |  |
| 2026-11-26 03:06:11 | Putupaula (Kalu Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-11-26 03:02:28 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-26 03:01:08 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-11-26 04:02:09 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-26 03:00:04 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-11-26 04:02:01 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.035 |  |
| 2026-11-26 03:09:54 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.040 |  |
| 2026-11-26 03:01:58 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.050 |  |
| 2026-11-26 04:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.054 |  |
| 2026-11-26 04:02:09 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.070 |  |
| 2026-11-26 03:11:29 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.073 |  |
| 2026-11-26 03:02:33 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.081 |  |
| 2026-11-26 03:02:39 | Glencourse (Kelani Ganga) | 12.13 | 🟢 Normal | -0.108 |  |
| 2026-11-26 03:11:01 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.146 |  |
| 2026-11-26 04:02:37 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.161 |  |
| 2026-11-26 04:02:23 | Peradeniya (Mahaweli Ganga) | 3.54 | 🟢 Normal | -0.177 |  |
| 2026-11-26 03:05:07 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.712 |  |
| 2026-11-26 03:00:38 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.973 |  |
| 2026-11-26 03:08:47 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)