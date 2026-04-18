# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_04:24:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,958 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 04:24:52 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:13:21 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-19 04:12:38 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.203 |  |
| 2026-04-19 04:08:38 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-04-19 04:06:13 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:05:47 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:05:47 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-19 04:05:41 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:05:16 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.033 |  |
| 2026-04-19 04:05:00 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-19 04:04:52 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:04:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:03:33 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.059 |  |
| 2026-04-19 04:02:59 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-19 04:02:23 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-19 04:02:09 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.128 |  |
| 2026-04-19 04:01:59 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:01:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.100 |  |
| 2026-04-19 04:01:55 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-04-19 04:01:50 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:01:34 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.042 |  |
| 2026-04-19 04:01:29 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:01:28 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:01:25 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-19 04:00:54 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-19 04:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-19 04:00:46 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:00:19 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:35:32 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 04:13:21 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-19 03:07:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-19 04:00:54 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-19 03:03:58 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-19 04:02:59 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-19 03:01:11 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 04:00:46 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:01:28 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:01:50 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:02:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:12:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:05:47 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:04:52 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:03:31 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:03:43 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:24:52 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:01:59 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:04:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:01:29 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 04:06:13 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:07:06 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-04-19 03:05:35 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.005 |  |
| 2026-04-19 04:08:38 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-04-19 04:05:00 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-19 04:01:25 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-19 04:02:23 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-19 04:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-19 04:05:47 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-19 04:01:55 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-04-19 03:35:32 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2026-04-19 04:05:16 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.033 |  |
| 2026-04-19 04:01:34 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.042 |  |
| 2026-04-19 04:03:33 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.059 |  |
| 2026-04-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.068 |  |
| 2026-04-19 04:01:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.100 |  |
| 2026-04-19 04:02:09 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.128 |  |
| 2026-04-19 04:12:38 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)