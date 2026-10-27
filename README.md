# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_06:23:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,114 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 06:23:37 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-27 06:16:46 | Panadugama (Nilwala Ganga) | 6.52 | 🟠 Minor Flood | -0.024 |  |
| 2026-10-27 06:12:37 | Holombuwa (Kelani Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:12:11 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.035 |  |
| 2026-10-27 06:09:54 | Moragaswewa (Deduru Oya) | 5.28 | 🟡 Alert | 0.000 |  |
| 2026-10-27 06:09:14 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.099 |  |
| 2026-10-27 06:08:23 | Holombuwa (Kelani Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:07:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | 0.291 | 🔺 Rising |
| 2026-10-27 06:05:57 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.179 |  |
| 2026-10-27 06:05:57 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | -0.148 |  |
| 2026-10-27 06:05:48 | Thalgahagoda (Nilwala Ganga) | 1.59 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-27 06:05:41 | Deraniyagala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-27 06:05:31 | Ellagawa (Kalu Ganga) | 9.81 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-27 06:04:59 | Rathnapura (Kalu Ganga) | 8.66 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-27 06:04:42 | Glencourse (Kelani Ganga) | 14.23 | 🟢 Normal | -0.214 |  |
| 2026-10-27 06:04:28 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | -0.111 |  |
| 2026-10-27 06:04:24 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.021 |  |
| 2026-10-27 06:04:14 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:04:09 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:04:02 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:03:54 | Norwood (Kelani Ganga) | 1.60 | 🟡 Alert | -0.040 |  |
| 2026-10-27 06:03:53 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.051 |  |
| 2026-10-27 06:03:47 | Nawalapitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.030 |  |
| 2026-10-27 06:03:31 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.022 |  |
| 2026-10-27 06:03:26 | Baddegama (Gin Ganga) | 3.84 | 🟡 Alert | 0.045 | 🔺 Rising |
| 2026-10-27 06:03:15 | Giriulla (Maha Oya) | 4.42 | 🟢 Normal | -0.213 |  |
| 2026-10-27 06:03:11 | Badalgama (Maha Oya) | 5.76 | 🟡 Alert | -0.010 |  |
| 2026-10-27 06:03:02 | Pitabeddara (Nilwala Ganga) | 3.51 | 🟢 Normal | -0.120 |  |
| 2026-10-27 06:02:54 | Dunamale (Aththanagalu Oya) | 4.76 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 06:02:51 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:02:44 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-27 06:02:10 | Thawalama (Gin Ganga) | 5.04 | 🟡 Alert | -0.060 |  |
| 2026-10-27 06:02:09 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-10-27 06:01:43 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-10-27 06:01:31 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-27 06:01:27 | Putupaula (Kalu Ganga) | 3.23 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-10-27 06:01:14 | Hanwella (Kelani Ganga) | 6.69 | 🟢 Normal | -0.020 |  |
| 2026-10-27 06:00:14 | Magura (Kalu Ganga) | 5.30 | 🟡 Alert | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 06:07:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | 0.291 | 🔺 Rising |
| 2026-10-27 06:02:54 | Dunamale (Aththanagalu Oya) | 4.76 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 06:04:59 | Rathnapura (Kalu Ganga) | 8.66 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-27 06:16:46 | Panadugama (Nilwala Ganga) | 6.52 | 🟠 Minor Flood | -0.024 |  |
| 2026-10-27 06:03:26 | Baddegama (Gin Ganga) | 3.84 | 🟡 Alert | 0.045 | 🔺 Rising |
| 2026-10-27 06:01:27 | Putupaula (Kalu Ganga) | 3.23 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-10-27 06:00:14 | Magura (Kalu Ganga) | 5.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 06:05:48 | Thalgahagoda (Nilwala Ganga) | 1.59 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-27 06:09:54 | Moragaswewa (Deduru Oya) | 5.28 | 🟡 Alert | 0.000 |  |
| 2026-10-27 06:03:11 | Badalgama (Maha Oya) | 5.76 | 🟡 Alert | -0.010 |  |
| 2026-10-27 06:03:54 | Norwood (Kelani Ganga) | 1.60 | 🟡 Alert | -0.040 |  |
| 2026-10-27 06:02:10 | Thawalama (Gin Ganga) | 5.04 | 🟡 Alert | -0.060 |  |
| 2026-10-27 06:01:43 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-27 06:02:44 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-27 06:05:41 | Deraniyagala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-27 06:05:31 | Ellagawa (Kalu Ganga) | 9.81 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-27 06:23:37 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-27 06:04:02 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:04:14 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:04:09 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:02:51 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:12:37 | Holombuwa (Kelani Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-27 06:01:31 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-27 06:02:09 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-10-27 06:01:14 | Hanwella (Kelani Ganga) | 6.69 | 🟢 Normal | -0.020 |  |
| 2026-10-27 06:04:24 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.021 |  |
| 2026-10-27 06:03:31 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.022 |  |
| 2026-10-27 06:03:47 | Nawalapitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.030 |  |
| 2026-10-27 06:12:11 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.035 |  |
| 2026-10-27 06:03:53 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.051 |  |
| 2026-10-27 06:09:14 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.099 |  |
| 2026-10-27 06:04:28 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | -0.111 |  |
| 2026-10-27 06:03:02 | Pitabeddara (Nilwala Ganga) | 3.51 | 🟢 Normal | -0.120 |  |
| 2026-10-27 06:05:57 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | -0.148 |  |
| 2026-10-27 06:05:57 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.179 |  |
| 2026-10-27 06:03:15 | Giriulla (Maha Oya) | 4.42 | 🟢 Normal | -0.213 |  |
| 2026-10-27 06:04:42 | Glencourse (Kelani Ganga) | 14.23 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)