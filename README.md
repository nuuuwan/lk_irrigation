# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_06:22:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 06:22:55 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:18:57 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-30 06:12:02 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:11:29 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.017 |  |
| 2026-03-30 06:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.481 |  |
| 2026-03-30 06:07:40 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-30 06:07:28 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:07:28 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-03-30 06:07:19 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | -0.011 |  |
| 2026-03-30 06:06:47 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-03-30 06:06:07 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-30 06:05:45 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 06:05:17 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-03-30 06:04:39 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-03-30 06:04:18 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:04:15 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:04:05 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 06:04:02 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2026-03-30 06:03:54 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:03:53 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-30 06:03:46 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:03:44 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 06:03:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:03:10 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-30 06:02:53 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:02:53 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.026 |  |
| 2026-03-30 06:02:53 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:02:25 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.013 |  |
| 2026-03-30 06:02:21 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:02:17 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:02:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-30 06:02:05 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:01:59 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:01:53 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:01:50 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.083 |  |
| 2026-03-30 06:01:49 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:01:38 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:01:30 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:00:20 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-30 05:52:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.481 |  |
| 2026-03-30 05:46:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 05:38:42 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 05:38:16 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 05:37:03 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 06:07:40 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-30 06:00:20 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-30 06:18:57 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-30 06:03:53 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-30 06:05:45 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 06:03:10 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-30 06:02:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-30 06:03:44 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 06:04:05 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 06:01:38 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:22:55 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:02:05 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:02:53 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:07:28 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:03:02 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:02:53 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:02:17 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:01:53 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:01:59 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:03:54 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:03:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:02:21 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:12:02 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:04:18 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:01:49 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:04:15 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:06:47 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-03-30 06:06:07 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-30 06:07:19 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | -0.011 |  |
| 2026-03-30 06:02:25 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.013 |  |
| 2026-03-30 06:11:29 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.017 |  |
| 2026-03-30 06:07:28 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-03-30 06:05:17 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-03-30 06:02:53 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.026 |  |
| 2026-03-30 06:04:39 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-03-30 06:04:02 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2026-03-30 06:01:50 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.083 |  |
| 2026-03-30 06:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.481 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)