# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_03:33:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,119 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 03:33:36 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-09-26 03:31:42 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:21:09 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.008 |  |
| 2026-09-26 03:20:30 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:20:13 | Kithulgala (Kelani Ganga) | 2.72 | 🟢 Normal | -0.047 |  |
| 2026-09-26 03:19:15 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:18:10 | Baddegama (Gin Ganga) | 4.79 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-26 03:14:22 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:12:30 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:11:51 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:11:02 | Hanwella (Kelani Ganga) | 5.88 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:10:09 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.039 |  |
| 2026-09-26 03:09:16 | Ellagawa (Kalu Ganga) | 8.79 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-09-26 03:09:07 | Rathnapura (Kalu Ganga) | 5.48 | 🟡 Alert | -108.000 |  |
| 2026-09-26 03:09:05 | Rathnapura (Kalu Ganga) | 5.54 | 🟡 Alert | -108.000 |  |
| 2026-09-26 03:07:49 | Thawalama (Gin Ganga) | 3.24 | 🟢 Normal | -0.071 |  |
| 2026-09-26 03:07:30 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.004 |  |
| 2026-09-26 03:05:48 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:05:30 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-09-26 03:05:21 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:05:01 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | -1.469 |  |
| 2026-09-26 03:04:56 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:04:29 | Glencourse (Kelani Ganga) | 13.83 | 🟢 Normal | -0.067 |  |
| 2026-09-26 03:04:12 | Panadugama (Nilwala Ganga) | 6.19 | 🟠 Minor Flood | -1.469 |  |
| 2026-09-26 03:04:01 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:03:51 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:03:48 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:03:48 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | -0.013 |  |
| 2026-09-26 03:03:35 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:03:34 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-09-26 03:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | 0.006 | 🔺 Rising |
| 2026-09-26 03:02:58 | Deraniyagala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:02:15 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:01:44 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-26 03:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:01:18 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 03:01:10 | Pitabeddara (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:01:06 | Peradeniya (Mahaweli Ganga) | 4.16 | 🟢 Normal | -0.220 |  |
| 2026-09-26 03:00:45 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:00:23 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 03:18:10 | Baddegama (Gin Ganga) | 4.79 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-26 03:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | 0.006 | 🔺 Rising |
| 2026-09-26 03:07:30 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.004 |  |
| 2026-09-26 03:05:01 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | -1.469 |  |
| 2026-09-26 03:03:48 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | -0.013 |  |
| 2026-09-26 03:09:07 | Rathnapura (Kalu Ganga) | 5.48 | 🟡 Alert | -108.000 |  |
| 2026-09-26 03:33:36 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-09-26 03:01:44 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-26 03:01:18 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 03:12:30 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:20:30 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:05:21 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:03:35 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:01:10 | Pitabeddara (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:05:48 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:11:02 | Hanwella (Kelani Ganga) | 5.88 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:02:58 | Deraniyagala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:19:15 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:03:51 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:03:32 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:14:22 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:04:01 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:31:42 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:04:56 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:02:15 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:21:09 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.008 |  |
| 2026-09-26 03:05:30 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:02:21 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-26 03:03:34 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-09-26 03:10:09 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.039 |  |
| 2026-09-26 03:00:23 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.043 |  |
| 2026-09-26 03:20:13 | Kithulgala (Kelani Ganga) | 2.72 | 🟢 Normal | -0.047 |  |
| 2026-09-26 03:04:29 | Glencourse (Kelani Ganga) | 13.83 | 🟢 Normal | -0.067 |  |
| 2026-09-26 03:07:49 | Thawalama (Gin Ganga) | 3.24 | 🟢 Normal | -0.071 |  |
| 2026-09-26 03:01:06 | Peradeniya (Mahaweli Ganga) | 4.16 | 🟢 Normal | -0.220 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)