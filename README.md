# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_14:05:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,368 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 14:05:19 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 14:04:39 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-28 14:04:36 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:04:20 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-28 14:03:44 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-28 14:03:41 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.021 |  |
| 2026-04-28 14:03:14 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.051 |  |
| 2026-04-28 14:02:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-04-28 14:02:57 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:51 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:43 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:37 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:17 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-28 14:02:14 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:08 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 14:02:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 14:01:30 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-28 14:01:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:01:18 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-04-28 14:01:14 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-28 14:01:09 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:21:07 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:20:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:19:53 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.033 |  |
| 2026-04-28 13:15:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 13:00:06 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-28 14:05:19 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 14:02:08 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 14:01:30 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-28 14:02:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 13:03:03 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:37 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:01:09 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:01:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:10:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:21:07 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:20:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:05:15 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:57 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:43 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:51 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:59:48 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:07:24 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:04:36 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:02:14 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:06:15 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-04-28 14:03:44 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:03:21 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-28 14:04:20 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-28 14:02:17 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:01:31 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-28 14:01:14 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-28 14:01:18 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:07:45 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-04-28 14:04:39 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-28 14:03:41 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.021 |  |
| 2026-04-28 13:06:34 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.025 |  |
| 2026-04-28 13:19:53 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.033 |  |
| 2026-04-28 14:03:14 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.051 |  |
| 2026-04-28 13:15:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.053 |  |
| 2026-04-28 13:02:19 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.054 |  |
| 2026-04-28 14:02:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-04-28 13:03:58 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)