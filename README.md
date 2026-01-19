# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--19_05:26:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,563 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 05:26:21 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-01-19 05:25:49 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-01-19 05:23:57 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.008 |  |
| 2026-01-19 05:15:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-01-19 05:14:34 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-19 05:13:44 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:10:39 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:09:35 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-19 05:07:08 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:06:34 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 05:05:27 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:05:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:04:59 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.009 |  |
| 2026-01-19 05:04:12 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:03:42 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.012 |  |
| 2026-01-19 05:03:33 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:03:10 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-19 05:02:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:02:47 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-19 05:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-01-19 05:02:42 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:02:41 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:02:40 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.250 |  |
| 2026-01-19 05:02:12 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-19 05:02:09 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:01:47 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:01:34 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:01:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.094 |  |
| 2026-01-19 05:01:24 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-19 05:01:18 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:01:08 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-19 04:56:37 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 05:26:21 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-01-19 03:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-19 05:14:34 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-19 05:02:12 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-19 05:02:47 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-19 04:32:24 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-19 04:01:51 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 05:06:34 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 05:09:35 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-19 05:05:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:04:12 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:01:47 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:02:41 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:02:42 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:05:15 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:05:27 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:10:39 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:13:44 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-19 04:56:37 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:02:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:02:09 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 02:32:29 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:07:14 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:03:33 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:01:56 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:01:18 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:01:34 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:07:08 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-19 05:23:57 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.008 |  |
| 2026-01-19 05:04:59 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.009 |  |
| 2026-01-19 05:01:24 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-19 05:03:10 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-19 05:03:42 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.012 |  |
| 2026-01-18 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.020 |  |
| 2026-01-19 05:01:08 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-19 05:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-01-19 05:15:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-01-19 05:01:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.094 |  |
| 2026-01-19 05:02:40 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.250 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)