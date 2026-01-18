# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_11:17:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,902 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 11:17:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-18 11:13:48 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:09:03 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-18 11:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.037 |  |
| 2026-01-18 11:08:24 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-18 11:07:15 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-01-18 11:06:57 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.011 |  |
| 2026-01-18 11:06:54 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-01-18 11:05:46 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-01-18 11:05:30 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-01-18 11:04:36 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:04:32 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.019 |  |
| 2026-01-18 11:04:28 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:04:20 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:04:07 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:04:04 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:03:56 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-18 11:03:40 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-01-18 11:03:38 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-01-18 11:03:00 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:45 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-01-18 11:02:39 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-18 11:02:26 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:24 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-18 11:02:23 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:13 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 11:02:10 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:08 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:03 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:01:32 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:01:20 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:01:05 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.016 |  |
| 2026-01-18 11:00:56 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:00:54 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-01-18 11:00:53 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.051 |  |
| 2026-01-18 11:00:52 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:00:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-01-18 11:00:25 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 10:22:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 11:03:40 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-01-18 11:00:54 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-01-18 11:00:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-01-18 11:02:39 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-18 11:17:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-18 11:02:24 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-18 11:03:56 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-18 11:09:03 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-18 11:08:24 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-18 11:02:13 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 11:00:52 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:00:25 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:23 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:01:32 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:04:28 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:04:20 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:26 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:04:07 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:10 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 10:03:49 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:03:00 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:08 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:04:04 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:01:20 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:13:48 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:00:56 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:02:03 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:04:36 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-18 11:07:15 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-01-18 11:02:45 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-01-18 11:06:57 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.011 |  |
| 2026-01-18 11:01:05 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.016 |  |
| 2026-01-18 11:04:32 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.019 |  |
| 2026-01-18 11:05:46 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-01-18 11:05:30 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-01-18 11:06:54 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-01-18 11:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.037 |  |
| 2026-01-18 11:00:53 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)