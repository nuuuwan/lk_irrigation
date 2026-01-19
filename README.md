# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--19_17:19:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,039 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 17:19:39 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |
| 2026-01-19 17:14:25 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-01-19 17:12:56 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:11:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-19 17:09:44 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:08:23 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-19 17:06:37 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:05:58 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:05:34 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.082 |  |
| 2026-01-19 17:05:25 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:05:11 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:05:03 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:04:40 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:04:18 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:03:45 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 17:03:42 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.010 |  |
| 2026-01-19 17:03:40 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-19 17:03:34 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -1.741 |  |
| 2026-01-19 17:03:29 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:03:24 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:03:15 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:02:33 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-19 17:02:32 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-01-19 17:02:29 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.080 |  |
| 2026-01-19 17:02:28 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:02:27 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:02:15 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-01-19 17:02:09 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.073 |  |
| 2026-01-19 17:02:07 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:02:03 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.031 |  |
| 2026-01-19 17:01:57 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:01:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-19 17:01:21 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.066 |  |
| 2026-01-19 17:01:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:00:28 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:00:17 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.090 |  |
| 2026-01-19 17:00:07 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 17:11:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-19 16:01:41 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-19 17:03:40 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-19 17:08:23 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-19 17:03:45 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 17:03:24 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:02:07 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:00:28 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:05:58 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-19 16:12:49 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:02:28 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:00:07 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:09:44 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:04:18 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:05:03 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:05:25 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:05:11 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:03:29 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:04:40 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:02:15 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:02:27 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:12:56 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:06:37 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:01:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:01:57 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 17:19:39 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |
| 2026-01-19 17:14:25 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-01-19 17:03:42 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.010 |  |
| 2026-01-19 17:02:33 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-19 17:01:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-19 17:02:32 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-01-19 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-01-19 17:02:03 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.031 |  |
| 2026-01-19 17:01:21 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.066 |  |
| 2026-01-19 17:02:09 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.073 |  |
| 2026-01-19 17:02:29 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.080 |  |
| 2026-01-19 17:05:34 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.082 |  |
| 2026-01-19 17:00:17 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.090 |  |
| 2026-01-19 17:03:34 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -1.741 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)