# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_21:48:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,354 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 21:48:14 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-04-03 21:15:12 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 21:11:08 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.076 |  |
| 2026-04-03 21:09:18 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-03 21:08:54 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.018 |  |
| 2026-04-03 21:08:32 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:07:09 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 21:06:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.038 |  |
| 2026-04-03 21:06:44 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.009 |  |
| 2026-04-03 21:06:32 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.019 |  |
| 2026-04-03 21:05:57 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-03 21:05:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 21:04:21 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.049 |  |
| 2026-04-03 21:04:16 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-03 21:04:03 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.041 |  |
| 2026-04-03 21:03:56 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-03 21:03:54 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-04-03 21:03:52 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-03 21:03:42 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:03:41 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 21:02:49 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-04-03 21:05:57 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-03 21:02:07 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-03 21:03:30 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-03 21:03:52 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-03 21:09:18 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-03 21:05:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 21:01:18 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 21:02:15 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 21:07:09 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 21:15:12 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 21:00:53 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:00:44 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:03:10 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:08:32 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:00:28 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:03:42 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:02:20 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:02:31 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:03:32 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:02:23 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:03:12 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:06:44 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.009 |  |
| 2026-04-03 21:04:16 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-03 21:03:56 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-03 21:08:54 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.018 |  |
| 2026-04-03 21:03:54 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-04-03 21:06:32 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.019 |  |
| 2026-04-03 21:02:12 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-04-03 21:06:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.038 |  |
| 2026-04-03 21:04:03 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.041 |  |
| 2026-04-03 21:04:21 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.049 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-03 21:03:41 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.060 |  |
| 2026-04-03 21:48:14 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-04-03 21:11:08 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)