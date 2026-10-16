# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_21:05:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,795 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 21:05:57 | Pitabeddara (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:05:44 | Panadugama (Nilwala Ganga) | 6.39 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 21:05:38 | Moragaswewa (Deduru Oya) | 2.13 | 🟢 Normal | -0.041 |  |
| 2026-10-16 21:04:41 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:04:38 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.060 |  |
| 2026-10-16 21:04:33 | Urawa (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-16 21:04:02 | Rathnapura (Kalu Ganga) | 3.97 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-10-16 21:03:58 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:03:54 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-16 21:03:27 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-16 21:03:27 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-16 21:03:24 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:03:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-16 21:03:17 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | -0.040 |  |
| 2026-10-16 21:03:01 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-16 21:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.000 |  |
| 2026-10-16 21:02:50 | Thaldena (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.267 |  |
| 2026-10-16 21:02:40 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:02:38 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 21:02:24 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 21:02:19 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:02:08 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 21:01:55 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:01:37 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.217 |  |
| 2026-10-16 21:00:50 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 21:00:39 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.089 |  |
| 2026-10-16 21:00:38 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:00:21 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.022 |  |
| 2026-10-16 20:59:02 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:59:01 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 21:05:44 | Panadugama (Nilwala Ganga) | 6.39 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 20:07:23 | Thalgahagoda (Nilwala Ganga) | 1.96 | 🟠 Minor Flood | -0.037 |  |
| 2026-10-16 21:03:27 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-16 21:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.000 |  |
| 2026-10-16 20:05:40 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.496 | 🔺 Rising |
| 2026-10-16 21:04:02 | Rathnapura (Kalu Ganga) | 3.97 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-10-16 21:03:54 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-16 21:03:01 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-16 20:01:27 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-16 21:04:33 | Urawa (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-16 20:05:01 | Thawalama (Gin Ganga) | 3.60 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-16 20:10:00 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-16 21:00:50 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 21:02:08 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 21:02:38 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 20:06:49 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 21:02:24 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 21:04:41 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:59:02 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:01:55 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:05:57 | Pitabeddara (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:03:24 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:02:40 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:02:19 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:03:58 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:03:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-16 21:03:27 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-16 21:00:21 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.022 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-16 21:03:17 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | -0.040 |  |
| 2026-10-16 20:02:34 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-10-16 21:05:38 | Moragaswewa (Deduru Oya) | 2.13 | 🟢 Normal | -0.041 |  |
| 2026-10-16 21:04:38 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.060 |  |
| 2026-10-16 20:00:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.062 |  |
| 2026-10-16 21:00:39 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.089 |  |
| 2026-10-16 21:01:37 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.217 |  |
| 2026-10-16 21:02:50 | Thaldena (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)