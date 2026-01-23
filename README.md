# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--23_06:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **53,204 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 06:11:57 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:11:11 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:11:00 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:10:09 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:10:04 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.018 |  |
| 2026-01-23 06:09:22 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:08:43 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.005 |  |
| 2026-01-23 06:07:22 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:06:50 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 06:06:31 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:06:24 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:06:18 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-23 06:05:40 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:05:22 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 06:05:13 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:05:00 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 06:04:56 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:04:55 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:04:38 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-01-23 06:03:38 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:03:19 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-01-23 06:02:50 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:30 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:29 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:28 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:27 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:26 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:23 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:13 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-23 06:01:56 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 06:01:48 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:01:45 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:01:29 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.114 |  |
| 2026-01-23 06:01:28 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-23 06:01:28 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-23 06:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.043 |  |
| 2026-01-23 06:01:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-01-23 06:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-23 06:00:12 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.224 |  |
| 2026-01-23 05:57:35 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 06:01:28 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-23 05:07:22 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-23 06:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-23 06:01:28 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-23 06:06:18 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-23 06:01:56 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 06:05:22 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 06:05:00 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 06:06:50 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 06:01:45 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 05:01:59 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:11:00 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:50 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:07:08 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:23 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:06:31 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:03:38 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:01:48 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:04:55 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:11:11 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:05:13 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:06:24 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:02:30 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:11:57 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:09:22 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:05:40 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:10:09 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:34 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:07:22 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:04:56 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:08:43 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.005 |  |
| 2026-01-23 06:02:13 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-23 06:10:04 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.018 |  |
| 2026-01-23 06:04:38 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-01-23 06:03:19 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-01-23 06:01:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-01-23 06:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.043 |  |
| 2026-01-23 06:01:29 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.114 |  |
| 2026-01-23 06:00:12 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.224 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)