# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_08:37:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,463 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 08:37:13 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:22:27 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:19:30 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:18:28 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:26 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:25 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:24 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:23 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:22 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:20 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:19 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:18 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:16 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:18:15 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:12:26 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-03-07 08:10:49 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:09:43 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-07 08:09:18 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:08:58 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:08:23 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:08:14 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.104 |  |
| 2026-03-07 08:07:24 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:06:56 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:06:48 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:04:42 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-07 08:04:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-03-07 08:04:12 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:04:00 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.020 |  |
| 2026-03-07 08:03:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.005 |  |
| 2026-03-07 08:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.059 |  |
| 2026-03-07 08:03:11 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 08:03:09 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:03:08 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-03-07 08:03:00 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 08:02:59 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:02:58 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-07 08:02:55 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:02:10 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:01:55 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:01:51 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 08:18:28 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-07 08:00:50 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-07 08:04:42 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-07 08:03:00 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 08:09:43 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-07 08:01:27 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-07 08:00:39 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-07 08:03:11 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 08:08:58 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:02:59 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:00:37 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:01:51 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:02:10 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:08:23 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:09:18 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:02:55 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:06:48 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:19:30 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:00:22 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:03:09 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:07:24 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:06:56 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:01:55 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:04:12 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:37:13 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:22:27 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-07 08:03:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.005 |  |
| 2026-03-07 08:02:58 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-07 08:03:08 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-03-07 08:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-07 08:12:26 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-03-07 08:01:12 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | -0.012 |  |
| 2026-03-07 08:01:26 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.014 |  |
| 2026-03-07 08:01:10 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-03-07 08:01:11 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.020 |  |
| 2026-03-07 08:04:00 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.020 |  |
| 2026-03-07 08:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.059 |  |
| 2026-03-07 08:04:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-03-07 08:08:14 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)