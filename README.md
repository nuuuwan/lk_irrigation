# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_17:14:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 17:14:20 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:12:02 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.018 |  |
| 2026-04-07 17:09:32 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-07 17:08:25 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:07:18 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.009 |  |
| 2026-04-07 17:07:05 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:07:00 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:06:59 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-07 17:06:20 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-07 17:05:51 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-07 17:05:45 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:05:35 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-04-07 17:05:09 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-04-07 17:04:36 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:03:42 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:03:32 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:03:13 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:03:12 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-07 17:03:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:03:05 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-07 17:03:04 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:03:02 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-07 17:02:57 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-04-07 17:02:40 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-07 17:02:39 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:02:30 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 17:01:58 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 17:01:54 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.080 |  |
| 2026-04-07 17:01:49 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:48 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:46 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:01:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-07 17:01:34 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:00:53 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-07 17:00:53 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:00:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-07 16:58:40 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 17:02:40 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-07 17:03:12 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-07 17:00:53 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-07 17:03:02 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-07 17:01:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-07 17:01:58 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 17:02:30 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 16:07:36 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 17:07:05 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:07:00 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:02:39 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:03:13 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 17:06:20 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-07 17:00:53 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:03:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:03:42 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:49 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:34 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:14:20 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:01:48 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:04:36 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:08:25 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-07 17:09:32 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-07 17:05:35 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-04-07 17:07:18 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.009 |  |
| 2026-04-07 17:05:45 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:00:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:03:04 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:01:46 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-07 17:12:02 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.018 |  |
| 2026-04-07 17:06:59 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-07 17:05:51 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-07 17:02:57 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-04-07 17:03:05 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-07 17:05:09 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-04-07 17:01:54 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)