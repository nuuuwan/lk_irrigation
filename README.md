# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_07:19:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,062 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 07:19:53 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:16:33 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 07:14:44 | Pitabeddara (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.089 |  |
| 2026-10-28 07:13:09 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:13:06 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.025 |  |
| 2026-10-28 07:11:23 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.027 |  |
| 2026-10-28 07:09:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.80 | 🟠 Minor Flood | -0.018 |  |
| 2026-10-28 07:09:11 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:08:13 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | 0.000 |  |
| 2026-10-28 07:06:56 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-28 07:06:32 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.038 |  |
| 2026-10-28 07:05:54 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-28 07:05:43 | Putupaula (Kalu Ganga) | 3.60 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-28 07:04:58 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | -0.047 |  |
| 2026-10-28 07:04:53 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:04:42 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:04:38 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-10-28 07:04:35 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -4.259 |  |
| 2026-10-28 07:04:30 | Rathnapura (Kalu Ganga) | 6.64 | 🟡 Alert | -0.105 |  |
| 2026-10-28 07:04:09 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.074 |  |
| 2026-10-28 07:03:57 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:03:56 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-10-28 07:03:31 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:03:05 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:02:47 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | 0.000 |  |
| 2026-10-28 07:02:46 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.030 |  |
| 2026-10-28 07:02:41 | Thanthirimale (Malwathu Oya) | 2.43 | 🟢 Normal | -0.022 |  |
| 2026-10-28 07:02:41 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.061 |  |
| 2026-10-28 07:02:35 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:02:14 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:02:11 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-10-28 07:01:53 | Moragaswewa (Deduru Oya) | 3.17 | 🟢 Normal | -0.121 |  |
| 2026-10-28 07:01:48 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | -0.071 |  |
| 2026-10-28 07:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:01:43 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 07:01:34 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.130 |  |
| 2026-10-28 07:01:25 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:01:08 | Galgamuwa (Mee Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:00:59 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.186 |  |
| 2026-10-28 07:00:35 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:00:24 | Horowpothana (Yan Oya) | 3.34 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 07:01:43 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 07:16:33 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 07:09:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.80 | 🟠 Minor Flood | -0.018 |  |
| 2026-10-28 07:05:43 | Putupaula (Kalu Ganga) | 3.60 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-28 07:08:13 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | 0.000 |  |
| 2026-10-28 07:02:46 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.030 |  |
| 2026-10-28 07:01:48 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | -0.071 |  |
| 2026-10-28 07:04:30 | Rathnapura (Kalu Ganga) | 6.64 | 🟡 Alert | -0.105 |  |
| 2026-10-28 07:06:56 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-28 07:05:54 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-28 07:19:53 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:02:14 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:01:08 | Galgamuwa (Mee Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:03:57 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:04:53 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:01:25 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:09:11 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:13:09 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:04:38 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-10-28 07:04:42 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:03:31 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:00:35 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:02:35 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:02:11 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-10-28 07:02:41 | Thanthirimale (Malwathu Oya) | 2.43 | 🟢 Normal | -0.022 |  |
| 2026-10-28 07:13:06 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.025 |  |
| 2026-10-28 07:11:23 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.027 |  |
| 2026-10-28 07:03:56 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-10-28 07:00:24 | Horowpothana (Yan Oya) | 3.34 | 🟢 Normal | -0.035 |  |
| 2026-10-28 07:06:32 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.038 |  |
| 2026-10-28 07:04:58 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | -0.047 |  |
| 2026-10-28 07:02:41 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.061 |  |
| 2026-10-28 07:04:09 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.074 |  |
| 2026-10-28 07:14:44 | Pitabeddara (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.089 |  |
| 2026-10-28 07:01:53 | Moragaswewa (Deduru Oya) | 3.17 | 🟢 Normal | -0.121 |  |
| 2026-10-28 07:01:34 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.130 |  |
| 2026-10-28 07:00:59 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.186 |  |
| 2026-10-28 07:04:35 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -4.259 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)