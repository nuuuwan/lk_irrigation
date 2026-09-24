# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_06:31:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Pitabeddara — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 06:31:45 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:24:50 | Urawa (Nilwala Ganga) | 3.13 | 🟡 Alert | -0.008 |  |
| 2026-09-24 06:19:51 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | 0.325 | 🔺 Rising |
| 2026-09-24 06:15:40 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:10:35 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 06:09:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.72 | 🟠 Minor Flood | -0.061 |  |
| 2026-09-24 06:09:09 | Rathnapura (Kalu Ganga) | 4.96 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-09-24 06:08:52 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-24 06:08:36 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:08:14 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 06:07:55 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.001 |  |
| 2026-09-24 06:07:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.089 |  |
| 2026-09-24 06:07:12 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | 0.056 | 🔺 Rising |
| 2026-09-24 06:06:59 | Thawalama (Gin Ganga) | 4.98 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-09-24 06:05:58 | Pitabeddara (Nilwala Ganga) | 4.43 | 🟡 Alert | 0.315 | 🔺 Rising |
| 2026-09-24 06:05:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:05:20 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.031 |  |
| 2026-09-24 06:05:16 | Hanwella (Kelani Ganga) | 4.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 06:05:11 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-09-24 06:04:45 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.079 |  |
| 2026-09-24 06:04:17 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:03:53 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | 0.370 | 🔺 Rising |
| 2026-09-24 06:03:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:03:45 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:03:19 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -36.000 |  |
| 2026-09-24 06:03:19 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 06:03:18 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -36.000 |  |
| 2026-09-24 06:02:42 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-24 06:02:30 | Deraniyagala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-09-24 06:02:30 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:02:16 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:02:09 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-24 06:02:07 | Magura (Kalu Ganga) | 4.43 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-09-24 06:02:04 | Glencourse (Kelani Ganga) | 12.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 06:01:24 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-09-24 06:01:23 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.032 |  |
| 2026-09-24 06:01:13 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-09-24 06:00:54 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:00:53 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 06:19:51 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | 0.325 | 🔺 Rising |
| 2026-09-24 06:07:12 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | 0.056 | 🔺 Rising |
| 2026-09-24 06:09:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.72 | 🟠 Minor Flood | -0.061 |  |
| 2026-09-24 06:05:58 | Pitabeddara (Nilwala Ganga) | 4.43 | 🟡 Alert | 0.315 | 🔺 Rising |
| 2026-09-24 06:02:07 | Magura (Kalu Ganga) | 4.43 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-09-24 06:06:59 | Thawalama (Gin Ganga) | 4.98 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-09-24 06:05:11 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-09-24 06:24:50 | Urawa (Nilwala Ganga) | 3.13 | 🟡 Alert | -0.008 |  |
| 2026-09-24 06:03:53 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | 0.370 | 🔺 Rising |
| 2026-09-24 06:09:09 | Rathnapura (Kalu Ganga) | 4.96 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-09-24 06:02:30 | Deraniyagala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-09-24 06:08:52 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-24 06:02:09 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-24 06:10:35 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 06:03:19 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 06:02:04 | Glencourse (Kelani Ganga) | 12.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 06:05:16 | Hanwella (Kelani Ganga) | 4.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 06:08:14 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 06:07:55 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.001 |  |
| 2026-09-24 06:15:40 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:03:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:00:53 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:00:54 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:31:45 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:04:17 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:05:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:02:30 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:08:36 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:03:45 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:02:16 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 06:02:42 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-24 06:01:24 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-09-24 06:01:13 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-09-24 06:05:20 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.031 |  |
| 2026-09-24 06:01:23 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.032 |  |
| 2026-09-24 06:04:45 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.079 |  |
| 2026-09-24 06:07:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.089 |  |
| 2026-09-24 06:03:19 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)