# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_10:20:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,405 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 10:20:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:18:36 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:13:33 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-04-08 10:11:46 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.011 |  |
| 2026-04-08 10:09:49 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:08:26 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:07:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-04-08 10:07:32 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.028 |  |
| 2026-04-08 10:07:06 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:06:59 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.125 |  |
| 2026-04-08 10:06:04 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:05:41 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:05:05 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 10:04:37 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-04-08 10:04:35 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:04:11 | Kithulgala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.099 |  |
| 2026-04-08 10:03:54 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:03:51 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-08 10:03:51 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:03:40 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-08 10:03:18 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:03:07 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-08 10:03:01 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 10:03:00 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:02:46 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:02:39 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:02:27 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:02:20 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-08 10:02:08 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-08 10:01:47 | Thawalama (Gin Ganga) | 0.85 | 🟢 Normal | -0.042 |  |
| 2026-04-08 10:01:42 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-08 10:01:39 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:01:26 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:00:58 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:00:57 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-04-08 10:00:55 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-08 10:00:45 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:00:15 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-08 10:00:10 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 10:00:55 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-08 10:02:08 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-08 10:00:15 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-08 10:05:05 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 10:03:51 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-08 10:01:42 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-08 10:03:01 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 10:02:27 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:00:10 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:01:39 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:03:00 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:05:41 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:09:49 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:04:35 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:06:04 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:03:51 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:03:54 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:07:06 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:20:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:02:46 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:03:18 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:02:39 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:00:58 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:18:36 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:08:26 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:01:26 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-08 10:13:33 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-04-08 10:03:40 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-08 10:03:07 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-08 10:11:46 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.011 |  |
| 2026-04-08 10:04:37 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-04-08 10:02:20 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-08 10:07:32 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.028 |  |
| 2026-04-08 10:07:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-04-08 10:01:47 | Thawalama (Gin Ganga) | 0.85 | 🟢 Normal | -0.042 |  |
| 2026-04-08 10:00:57 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-04-08 10:04:11 | Kithulgala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.099 |  |
| 2026-04-08 10:06:59 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)