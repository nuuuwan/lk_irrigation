# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_20:12:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,901 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 20:12:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:09:48 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-19 20:08:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.058 |  |
| 2026-03-19 20:07:48 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-03-19 20:07:46 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:07:16 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.068 |  |
| 2026-03-19 20:06:57 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-03-19 20:06:29 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:05:56 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-19 20:05:53 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:05:52 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:05:50 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-19 20:05:22 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-03-19 20:05:20 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:05:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:04:55 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 20:04:49 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-19 20:04:41 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:04:35 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:04:15 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.021 |  |
| 2026-03-19 20:04:01 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2026-03-19 20:03:47 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-19 20:03:24 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-03-19 20:02:52 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 20:02:28 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:02:11 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:02:11 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-19 20:02:10 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:02:10 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.357 |  |
| 2026-03-19 20:02:10 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:01:31 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:01:15 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.062 |  |
| 2026-03-19 20:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:01:13 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 20:01:05 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.050 |  |
| 2026-03-19 20:00:12 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:59:50 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:36:56 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.357 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 20:05:50 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-19 20:04:49 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-19 20:09:48 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-19 20:02:11 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-19 20:05:56 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-19 20:02:52 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 20:01:13 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 20:04:55 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 20:04:35 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:00:12 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:05:20 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:06:29 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:02:11 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:01:31 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:02:10 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:05:53 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:02:10 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:02:28 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:05:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:05:52 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:07:46 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:04:41 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:12:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:07:48 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-03-19 20:03:47 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-19 20:03:24 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-03-19 20:06:57 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-03-19 20:04:15 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.021 |  |
| 2026-03-19 20:05:22 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-03-19 20:01:05 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.050 |  |
| 2026-03-19 20:04:01 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2026-03-19 20:08:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.058 |  |
| 2026-03-19 20:01:15 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.062 |  |
| 2026-03-19 20:07:16 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.068 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-19 20:02:10 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.357 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)