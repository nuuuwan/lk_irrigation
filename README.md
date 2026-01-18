# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_19:08:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,212 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 19:08:52 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:08:09 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:08:00 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-01-18 19:07:38 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:06:53 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:06:48 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-01-18 19:06:18 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:06:05 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:05:47 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:05:26 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-01-18 19:05:24 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-01-18 19:04:56 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.056 |  |
| 2026-01-18 19:04:51 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:04:36 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:04:32 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:03:23 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:03:03 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.010 |  |
| 2026-01-18 19:03:01 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-18 19:02:53 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.056 |  |
| 2026-01-18 19:02:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-01-18 19:02:25 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:02:21 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:01:54 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-01-18 19:01:47 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:01:32 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:01:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:01:19 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 19:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:00:36 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:19:56 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-01-18 18:16:20 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 19:01:54 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-01-18 19:06:48 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-01-18 18:09:17 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-18 18:04:12 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-18 19:01:19 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 19:01:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:02:25 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:05:47 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:06:18 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:06:53 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:00:10 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:05:15 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:00:36 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:02:21 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:04:36 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:01:47 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:03:36 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:04:32 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:03:23 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:06:05 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:08:09 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:08:52 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:04:51 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:01:56 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:03:17 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:01:32 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:07:38 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 19:05:26 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-01-18 18:06:29 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-01-18 19:05:24 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-01-18 19:03:03 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.010 |  |
| 2026-01-18 19:03:01 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-18 18:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-01-18 19:08:00 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-01-18 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.020 |  |
| 2026-01-18 19:04:56 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.056 |  |
| 2026-01-18 19:02:53 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.056 |  |
| 2026-01-18 19:02:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)