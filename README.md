# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_19:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,552 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 19:03:06 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.020 |  |
| 2026-11-25 19:03:00 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-25 19:02:41 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-25 19:02:26 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-25 19:02:10 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-25 19:01:57 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-25 19:01:40 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-25 19:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 19:01:29 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.051 |  |
| 2026-11-25 19:01:23 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-25 19:01:09 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 19:01:09 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-11-25 19:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.085 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 17:06:45 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-25 18:01:31 | Peradeniya (Mahaweli Ganga) | 4.24 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-11-25 19:01:40 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-25 18:09:38 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-25 18:02:46 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-25 19:03:00 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-25 19:02:10 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 18:03:00 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-25 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.72 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-25 18:04:30 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 19:01:09 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 19:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 18:03:29 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-25 18:15:44 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-25 18:07:48 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-11-25 18:01:37 | Moraketiya (Walawe Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-25 18:05:30 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-25 19:01:57 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-25 19:02:26 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-25 19:01:23 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-25 18:02:13 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-11-25 18:09:17 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-11-25 19:02:41 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-25 19:03:06 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.020 |  |
| 2026-11-25 18:02:09 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 18:05:50 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-11-25 17:01:26 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-11-25 19:01:09 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-11-25 18:00:16 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.051 |  |
| 2026-11-25 19:01:29 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.051 |  |
| 2026-11-25 18:06:28 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.060 |  |
| 2026-11-25 18:06:30 | Hanwella (Kelani Ganga) | 2.65 | 🟢 Normal | -0.067 |  |
| 2026-11-25 18:04:00 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.080 |  |
| 2026-11-25 19:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.085 |  |
| 2026-11-25 18:06:21 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.112 |  |
| 2026-11-25 18:04:20 | Wellawaya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.351 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)