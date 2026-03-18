# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_19:47:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,955 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 19:47:15 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.035 |  |
| 2026-03-18 19:30:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-18 19:14:07 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:11:38 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:11:36 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-03-18 19:09:18 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-18 19:07:28 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:06:56 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-03-18 19:06:50 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-03-18 19:06:16 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-18 19:05:41 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-18 19:04:52 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-18 19:04:50 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:04:38 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:04:05 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.024 |  |
| 2026-03-18 19:04:01 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:03:54 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:03:50 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-18 19:03:29 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:03:19 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:03:08 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:03:05 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-03-18 19:02:50 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:02:39 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-18 19:02:39 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:02:32 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:02:28 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 19:02:28 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-03-18 19:02:15 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.062 |  |
| 2026-03-18 19:02:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:01:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.120 |  |
| 2026-03-18 19:01:36 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-18 19:01:34 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 19:06:56 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-03-18 19:11:36 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-03-18 19:04:52 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-18 19:00:52 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-18 19:06:16 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-18 19:01:36 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-18 19:02:28 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 19:30:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-18 19:01:22 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 19:05:41 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-18 19:09:18 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-18 19:11:38 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:03:29 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:16 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:03:08 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:04:50 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:01:34 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:03:19 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:04:01 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:02:50 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:00:29 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:02:39 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:07:28 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:03:54 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:04:38 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:14:07 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:01:09 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-18 19:06:50 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-03-18 19:02:39 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-18 19:03:50 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-18 19:02:28 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-03-18 19:03:05 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-03-18 19:04:05 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.024 |  |
| 2026-03-18 19:47:15 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.035 |  |
| 2026-03-18 19:02:15 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.062 |  |
| 2026-03-18 18:02:41 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.088 |  |
| 2026-03-18 19:01:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)