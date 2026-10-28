# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_10:03:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,161 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 10:03:59 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.015 |  |
| 2026-10-28 10:03:59 | Rathnapura (Kalu Ganga) | 6.41 | 🟡 Alert | -0.114 |  |
| 2026-10-28 10:03:56 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.039 |  |
| 2026-10-28 10:03:48 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:03:18 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:03:10 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-10-28 10:03:07 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
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
| 2026-10-28 09:32:31 | Rathnapura (Kalu Ganga) | 6.47 | 🟡 Alert | -0.114 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 09:05:13 | Baddegama (Gin Ganga) | 4.24 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-28 09:01:11 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 09:06:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.77 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 09:04:12 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 09:02:50 | Ellagawa (Kalu Ganga) | 10.45 | 🟡 Alert | 0.000 |  |
| 2026-10-28 10:02:16 | Panadugama (Nilwala Ganga) | 5.87 | 🟡 Alert | -0.021 |  |
| 2026-10-28 09:07:26 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.043 |  |
| 2026-10-28 09:02:14 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | -0.073 |  |
| 2026-10-28 10:03:59 | Rathnapura (Kalu Ganga) | 6.41 | 🟡 Alert | -0.114 |  |
| 2026-10-28 10:01:08 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-10-28 10:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 09:02:05 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:09:23 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:48 | Galgamuwa (Mee Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:04:35 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:02:35 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:03:48 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:03:18 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:41 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:03:39 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:01:31 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 10:02:08 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:07:04 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:03:13 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:01:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:01:57 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-28 10:02:56 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | -0.011 |  |
| 2026-10-28 10:03:07 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-10-28 10:03:10 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-10-28 10:03:59 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.015 |  |
| 2026-10-28 09:06:17 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-10-28 09:02:55 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | -0.031 |  |
| 2026-10-28 10:03:56 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.039 |  |
| 2026-10-28 09:13:21 | Urawa (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.046 |  |
| 2026-10-28 09:06:20 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | -0.047 |  |
| 2026-10-28 09:06:15 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.049 |  |
| 2026-10-28 09:02:29 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-10-28 10:01:16 | Thanthirimale (Malwathu Oya) | 2.30 | 🟢 Normal | -0.051 |  |
| 2026-10-28 09:09:41 | Horowpothana (Yan Oya) | 3.20 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)