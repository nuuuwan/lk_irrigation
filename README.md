# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_10:31:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,147 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 10:31:13 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:12:04 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.036 |  |
| 2026-09-18 10:11:04 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:09:54 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:08:55 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2026-09-18 10:08:51 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.050 |  |
| 2026-09-18 10:07:58 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.055 |  |
| 2026-09-18 10:07:27 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-18 10:07:02 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-09-18 10:06:46 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-09-18 10:06:40 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:06:12 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:05:46 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | -0.051 |  |
| 2026-09-18 10:05:45 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.028 |  |
| 2026-09-18 10:05:37 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:04:35 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.010 |  |
| 2026-09-18 10:04:20 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:04:07 | Magura (Kalu Ganga) | 4.19 | 🟡 Alert | -0.069 |  |
| 2026-09-18 10:03:53 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-18 10:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 10:03:39 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-18 10:03:28 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-09-18 10:03:17 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 10:03:09 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:02:35 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:02:23 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:02:12 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:02:06 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-18 10:01:58 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-18 10:01:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:01:52 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.020 |  |
| 2026-09-18 10:01:52 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-18 10:01:17 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:00:54 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:00:52 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-18 10:00:40 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:00:37 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:00:19 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 10:04:07 | Magura (Kalu Ganga) | 4.19 | 🟡 Alert | -0.069 |  |
| 2026-09-18 10:07:27 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-18 10:01:58 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-18 10:03:39 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-18 10:01:52 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-18 10:03:17 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 10:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 10:00:40 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:03:09 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:01:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:04:20 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:00:19 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:02:12 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:00:37 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:00:54 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:01:17 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:05:37 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:02:23 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:06:40 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:09:54 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:31:13 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:06:12 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:11:04 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:02:35 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 10:04:35 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.010 |  |
| 2026-09-18 10:03:53 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-18 10:02:06 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-18 10:00:52 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-18 10:08:55 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2026-09-18 10:06:46 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-09-18 10:07:02 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-09-18 10:01:52 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.020 |  |
| 2026-09-18 10:03:28 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-09-18 10:05:45 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.028 |  |
| 2026-09-18 10:12:04 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.036 |  |
| 2026-09-18 10:08:51 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.050 |  |
| 2026-09-18 10:05:46 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | -0.051 |  |
| 2026-09-18 10:07:58 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.055 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)