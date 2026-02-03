# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--03_19:12:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,439 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **54** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 19:12:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:29 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:27 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:24 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:22 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:20 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:18 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:16 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:14 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:12 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:09 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:06 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:03 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:12:03 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:12:00 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:11:58 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:11:54 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -108.000 |  |
| 2026-02-03 19:11:19 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:10:04 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:09:14 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:07:30 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:06:28 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-02-03 19:05:55 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:50 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:47 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-03 19:05:18 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.069 |  |
| 2026-02-03 19:05:15 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:14 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:13 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:12 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:11 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:09 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:07 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:06 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:04 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:03 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:02 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:00 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:04:59 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:04:57 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:04:07 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-03 19:03:37 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-03 19:03:26 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:03:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:03:10 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-02-03 19:03:06 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:02:50 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:02:48 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-03 19:02:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:02:23 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:02:21 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-03 19:02:20 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-03 19:00:58 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:00:21 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 19:02:48 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-03 05:18:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-03 18:11:41 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-03 19:03:37 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-03 05:03:58 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 19:03:26 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:03:06 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:00:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 18:14:18 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:50 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:12:03 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:07:30 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:02:23 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:02:50 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:00:58 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:03:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:13 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:10:04 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:05:55 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-03 19:09:14 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-03 19:06:28 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-02-03 19:05:47 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-03 19:04:07 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-03 19:02:21 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-03 06:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-03 19:02:20 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-03 18:02:54 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 09:01:34 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-03 18:23:53 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.036 |  |
| 2026-02-03 19:00:21 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.043 |  |
| 2026-02-03 19:03:10 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-02-03 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.068 |  |
| 2026-02-03 05:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 19:05:18 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.069 |  |
| 2026-02-03 19:12:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)