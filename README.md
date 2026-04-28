# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_17:15:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,499 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 17:15:48 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:39 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:14 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:07 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:08:32 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -12.000 |  |
| 2026-04-28 17:08:29 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -12.000 |  |
| 2026-04-28 17:08:06 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.057 |  |
| 2026-04-28 17:07:56 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | -0.039 |  |
| 2026-04-28 17:07:20 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.065 |  |
| 2026-04-28 17:06:58 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-04-28 17:06:45 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.101 |  |
| 2026-04-28 17:06:20 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:05:59 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-04-28 17:05:45 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.038 |  |
| 2026-04-28 17:05:41 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-04-28 17:05:08 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:04:55 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-28 17:04:39 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-04-28 17:04:22 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-28 17:04:21 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2026-04-28 17:04:13 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:04:02 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:03:47 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-28 17:03:34 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-04-28 17:03:33 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:03:18 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-04-28 17:03:12 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.063 |  |
| 2026-04-28 17:02:58 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:02:53 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 17:02:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-04-28 17:02:09 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.041 |  |
| 2026-04-28 17:02:08 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.072 |  |
| 2026-04-28 17:02:06 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 17:01:16 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:01:11 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 17:01:06 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-04-28 17:00:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 17:06:58 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-04-28 17:02:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-04-28 17:01:11 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 17:02:06 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 17:04:22 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 17:01:16 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:00:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:06:20 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:15:48 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:07 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:02:58 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:04:13 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:05:08 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:04:02 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:39 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:03:33 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:14 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:09:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:04:55 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-28 17:02:53 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-28 17:05:59 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-04-28 17:03:47 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-28 17:01:06 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-04-28 17:04:39 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-04-28 17:03:34 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-04-28 17:03:18 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-04-28 17:05:45 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.038 |  |
| 2026-04-28 17:07:56 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | -0.039 |  |
| 2026-04-28 17:04:21 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2026-04-28 17:02:09 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.041 |  |
| 2026-04-28 17:08:06 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.057 |  |
| 2026-04-28 17:05:41 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-04-28 17:03:12 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.063 |  |
| 2026-04-28 17:07:20 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.065 |  |
| 2026-04-28 17:02:08 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.072 |  |
| 2026-04-28 17:06:45 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.101 |  |
| 2026-04-28 17:08:32 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -12.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)