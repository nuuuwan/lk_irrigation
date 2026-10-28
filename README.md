# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_00:34:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,706 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 00:34:25 | Ellagawa (Kalu Ganga) | 10.27 | 🟡 Alert | -0.013 |  |
| 2026-10-29 00:22:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.63 | 🟠 Minor Flood | -1.200 |  |
| 2026-10-29 00:22:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.64 | 🟠 Minor Flood | -1.200 |  |
| 2026-10-29 00:19:15 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.095 |  |
| 2026-10-29 00:17:52 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 00:17:26 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:10:26 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 00:09:02 | Rathnapura (Kalu Ganga) | 5.53 | 🟡 Alert | -0.076 |  |
| 2026-10-29 00:05:42 | Badalgama (Maha Oya) | 3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 00:05:24 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | -0.053 |  |
| 2026-10-29 00:05:21 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:05:05 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.041 |  |
| 2026-10-29 00:04:59 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 00:04:55 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-29 00:04:47 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.010 |  |
| 2026-10-29 00:04:28 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-29 00:04:14 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-29 00:03:56 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-10-29 00:03:38 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-29 00:03:25 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.014 |  |
| 2026-10-29 00:03:19 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.051 |  |
| 2026-10-29 00:03:10 | Giriulla (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-10-29 00:03:10 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | -7.927 |  |
| 2026-10-29 00:02:58 | Baddegama (Gin Ganga) | 4.22 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 00:02:44 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.031 |  |
| 2026-10-29 00:02:43 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | -0.044 |  |
| 2026-10-29 00:02:38 | Pitabeddara (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:02:34 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-29 00:02:31 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:01:49 | Moragaswewa (Deduru Oya) | 2.39 | 🟢 Normal | -0.059 |  |
| 2026-10-29 00:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:01:30 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-10-29 00:01:21 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -7.927 |  |
| 2026-10-29 00:00:59 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.070 |  |
| 2026-10-29 00:00:46 | Pitabeddara (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:00:24 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 00:10:26 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 00:02:58 | Baddegama (Gin Ganga) | 4.22 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 00:03:38 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-29 00:22:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.63 | 🟠 Minor Flood | -1.200 |  |
| 2026-10-29 00:17:52 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 00:34:25 | Ellagawa (Kalu Ganga) | 10.27 | 🟡 Alert | -0.013 |  |
| 2026-10-28 22:08:39 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.044 |  |
| 2026-10-29 00:09:02 | Rathnapura (Kalu Ganga) | 5.53 | 🟡 Alert | -0.076 |  |
| 2026-10-29 00:04:14 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-29 00:04:59 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 00:05:42 | Badalgama (Maha Oya) | 3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 00:00:24 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:17:26 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:02:38 | Pitabeddara (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:05:21 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-28 23:03:20 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:02:31 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-29 00:03:10 | Giriulla (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-10-29 00:04:55 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-29 00:02:34 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-29 00:04:47 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.010 |  |
| 2026-10-29 00:03:56 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-10-29 00:03:25 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.014 |  |
| 2026-10-29 00:04:28 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-29 00:01:30 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-10-29 00:02:44 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.031 |  |
| 2026-10-29 00:05:05 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.041 |  |
| 2026-10-29 00:02:43 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | -0.044 |  |
| 2026-10-28 23:04:28 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.045 |  |
| 2026-10-29 00:03:19 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.051 |  |
| 2026-10-29 00:05:24 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | -0.053 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-29 00:01:49 | Moragaswewa (Deduru Oya) | 2.39 | 🟢 Normal | -0.059 |  |
| 2026-10-29 00:00:59 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.070 |  |
| 2026-10-29 00:19:15 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.095 |  |
| 2026-10-29 00:03:10 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | -7.927 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)