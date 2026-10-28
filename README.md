# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_10:16:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,182 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Putupaula — Alert; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 10:16:41 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 10:11:45 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.070 |  |
| 2026-10-28 10:11:19 | Horowpothana (Yan Oya) | 3.09 | 🟢 Normal | -0.107 |  |
| 2026-10-28 10:11:01 | Urawa (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:10:38 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.018 |  |
| 2026-10-28 10:10:37 | Magura (Kalu Ganga) | 4.24 | 🟡 Alert | -0.028 |  |
| 2026-10-28 10:09:52 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:08:48 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-28 10:08:41 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:08:14 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:07:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 10:06:25 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-10-28 10:06:04 | Moragaswewa (Deduru Oya) | 3.04 | 🟢 Normal | -0.019 |  |
| 2026-10-28 10:05:51 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2026-10-28 10:05:44 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -0.038 |  |
| 2026-10-28 10:05:42 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:05:10 | Ellagawa (Kalu Ganga) | 10.44 | 🟡 Alert | -0.010 |  |
| 2026-10-28 10:04:47 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | -0.077 |  |
| 2026-10-28 10:04:30 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.031 |  |
| 2026-10-28 10:04:21 | Putupaula (Kalu Ganga) | 3.63 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 10:04:16 | Hanwella (Kelani Ganga) | 4.49 | 🟢 Normal | -0.052 |  |
| 2026-10-28 10:03:59 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.015 |  |
| 2026-10-28 10:03:59 | Rathnapura (Kalu Ganga) | 6.41 | 🟡 Alert | -0.114 |  |
| 2026-10-28 10:03:56 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.039 |  |
| 2026-10-28 10:03:48 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:03:18 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:03:10 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-10-28 10:03:07 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:02:56 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | -0.011 |  |
| 2026-10-28 10:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 10:02:35 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:02:16 | Panadugama (Nilwala Ganga) | 5.87 | 🟡 Alert | -0.021 |  |
| 2026-10-28 10:02:08 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:57 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:01:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:01:48 | Galgamuwa (Mee Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:41 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:31 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:16 | Thanthirimale (Malwathu Oya) | 2.30 | 🟢 Normal | -0.051 |  |
| 2026-10-28 10:01:08 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.198 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 10:16:41 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 10:07:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 10:08:48 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-28 10:04:21 | Putupaula (Kalu Ganga) | 3.63 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 10:05:10 | Ellagawa (Kalu Ganga) | 10.44 | 🟡 Alert | -0.010 |  |
| 2026-10-28 10:02:16 | Panadugama (Nilwala Ganga) | 5.87 | 🟡 Alert | -0.021 |  |
| 2026-10-28 10:10:37 | Magura (Kalu Ganga) | 4.24 | 🟡 Alert | -0.028 |  |
| 2026-10-28 10:04:47 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | -0.077 |  |
| 2026-10-28 10:03:59 | Rathnapura (Kalu Ganga) | 6.41 | 🟡 Alert | -0.114 |  |
| 2026-10-28 10:01:08 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-10-28 10:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 10:08:41 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:48 | Galgamuwa (Mee Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:09:52 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:02:35 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:03:48 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:03:18 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:41 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:11:01 | Urawa (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:31 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:02:08 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:06:25 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-10-28 10:08:14 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:01:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:05:42 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:01:57 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:02:56 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | -0.011 |  |
| 2026-10-28 10:03:10 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-10-28 10:03:59 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.015 |  |
| 2026-10-28 10:10:38 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.018 |  |
| 2026-10-28 10:06:04 | Moragaswewa (Deduru Oya) | 3.04 | 🟢 Normal | -0.019 |  |
| 2026-10-28 10:05:51 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2026-10-28 10:04:30 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.031 |  |
| 2026-10-28 10:05:44 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -0.038 |  |
| 2026-10-28 10:03:56 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.039 |  |
| 2026-10-28 10:01:16 | Thanthirimale (Malwathu Oya) | 2.30 | 🟢 Normal | -0.051 |  |
| 2026-10-28 10:04:16 | Hanwella (Kelani Ganga) | 4.49 | 🟢 Normal | -0.052 |  |
| 2026-10-28 10:11:45 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.070 |  |
| 2026-10-28 10:11:19 | Horowpothana (Yan Oya) | 3.09 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)