# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_19:12:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,014 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 19:12:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.068 |  |
| 2026-04-24 19:11:21 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 19:08:47 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:06:39 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.103 |  |
| 2026-04-24 19:06:32 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.029 |  |
| 2026-04-24 19:06:18 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.057 |  |
| 2026-04-24 19:06:15 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-04-24 19:05:43 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.019 |  |
| 2026-04-24 19:05:31 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-04-24 19:05:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-04-24 19:04:55 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:04:51 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:04:47 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-04-24 19:04:07 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.038 |  |
| 2026-04-24 19:03:59 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:03:52 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:03:41 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:03:17 | Katharagama (Menik Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-04-24 19:02:58 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-24 19:02:53 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:02:42 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.032 |  |
| 2026-04-24 19:02:42 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.035 |  |
| 2026-04-24 19:02:36 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 19:02:28 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.030 |  |
| 2026-04-24 19:02:25 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:02:20 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 19:02:17 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:01:47 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-24 19:01:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:01:22 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:01:09 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:00:55 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:00:36 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:00:10 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:40:15 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 19:02:58 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-24 19:01:47 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-24 19:02:36 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 19:02:20 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 19:11:21 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 19:00:10 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:00:36 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:01:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:03:03 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:02:17 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:40:15 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:01:22 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:03:59 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:03:41 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:04:55 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:08:47 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 19:02:25 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:04:51 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:03:52 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:01:09 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:02:53 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:00:55 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-04-24 19:05:43 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.019 |  |
| 2026-04-24 19:03:17 | Katharagama (Menik Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-04-24 19:06:15 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-24 19:05:31 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-04-24 19:05:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-04-24 19:06:32 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.029 |  |
| 2026-04-24 19:04:47 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-04-24 19:02:28 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.030 |  |
| 2026-04-24 19:02:42 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.032 |  |
| 2026-04-24 19:02:42 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.035 |  |
| 2026-04-24 19:04:07 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.038 |  |
| 2026-04-24 19:06:18 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.057 |  |
| 2026-04-24 19:12:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.068 |  |
| 2026-04-24 19:06:39 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)