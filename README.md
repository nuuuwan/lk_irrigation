# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_20:17:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,565 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 20:17:05 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.071 |  |
| 2026-10-28 20:10:32 | Rathnapura (Kalu Ganga) | 5.79 | 🟡 Alert | -0.064 |  |
| 2026-10-28 20:09:52 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-28 20:08:34 | Moragaswewa (Deduru Oya) | 2.78 | 🟢 Normal | -0.100 |  |
| 2026-10-28 20:07:52 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 20:07:28 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.122 |  |
| 2026-10-28 20:07:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-10-28 20:05:49 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:05:47 | Putupaula (Kalu Ganga) | 3.72 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 20:05:05 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 20:04:49 | Giriulla (Maha Oya) | 2.09 | 🟢 Normal | -0.063 |  |
| 2026-10-28 20:04:42 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-28 20:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.66 | 🟠 Minor Flood | -0.012 |  |
| 2026-10-28 20:03:48 | Hanwella (Kelani Ganga) | 4.21 | 🟢 Normal | -0.030 |  |
| 2026-10-28 20:03:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:03:43 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:03:33 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.039 |  |
| 2026-10-28 20:03:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:03:28 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:03:25 | Thawalama (Gin Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:03:24 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:03:01 | Ellagawa (Kalu Ganga) | 10.38 | 🟡 Alert | -0.020 |  |
| 2026-10-28 20:02:31 | Dunamale (Aththanagalu Oya) | 3.11 | 🟢 Normal | -0.070 |  |
| 2026-10-28 20:02:30 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-10-28 20:02:13 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-28 20:02:06 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:02:06 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.022 |  |
| 2026-10-28 20:01:42 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:01:27 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:01:26 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:01:15 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:01:10 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:01:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:00:41 | Pitabeddara (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.071 |  |
| 2026-10-28 20:00:22 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-10-28 20:00:20 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 20:00:22 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-10-28 20:04:42 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-28 20:05:05 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 20:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.66 | 🟠 Minor Flood | -0.012 |  |
| 2026-10-28 20:00:20 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-28 20:05:47 | Putupaula (Kalu Ganga) | 3.72 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 20:03:01 | Ellagawa (Kalu Ganga) | 10.38 | 🟡 Alert | -0.020 |  |
| 2026-10-28 20:10:32 | Rathnapura (Kalu Ganga) | 5.79 | 🟡 Alert | -0.064 |  |
| 2026-10-28 20:09:52 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 20:02:13 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-28 20:07:52 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 20:01:27 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:01:15 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:03:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:05:49 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:01:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:01:10 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:03:28 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:01:42 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 20:03:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:02:06 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:03:25 | Thawalama (Gin Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:03:24 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:03:43 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-28 20:02:06 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.022 |  |
| 2026-10-28 20:02:30 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-10-28 20:03:48 | Hanwella (Kelani Ganga) | 4.21 | 🟢 Normal | -0.030 |  |
| 2026-10-28 20:03:33 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.039 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-28 20:04:49 | Giriulla (Maha Oya) | 2.09 | 🟢 Normal | -0.063 |  |
| 2026-10-28 20:02:31 | Dunamale (Aththanagalu Oya) | 3.11 | 🟢 Normal | -0.070 |  |
| 2026-10-28 20:00:41 | Pitabeddara (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.071 |  |
| 2026-10-28 20:17:05 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.071 |  |
| 2026-10-28 20:07:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-10-28 20:08:34 | Moragaswewa (Deduru Oya) | 2.78 | 🟢 Normal | -0.100 |  |
| 2026-10-28 20:07:28 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)