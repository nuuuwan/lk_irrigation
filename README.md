# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_22:33:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,158 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 22:33:27 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-12 22:15:48 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.019 |  |
| 2026-05-12 22:14:31 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.054 |  |
| 2026-05-12 22:12:16 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-12 22:09:41 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-12 22:09:23 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-12 22:09:05 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 22:08:32 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-12 22:07:21 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:07:12 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.063 |  |
| 2026-05-12 22:07:11 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-12 22:06:48 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-12 22:06:24 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.015 |  |
| 2026-05-12 22:06:20 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:05:57 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | -0.075 |  |
| 2026-05-12 22:04:48 | Nakkala (Kumbukkan Oya) | 3.25 | 🟢 Normal | -0.606 |  |
| 2026-05-12 22:04:44 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:04:38 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-12 22:04:34 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.255 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 22:01:54 | Siyambalanduwa (Heda Oya) | 2.70 | 🟢 Normal | 1.101 | 🔺 Rising |
| 2026-05-12 21:08:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-12 22:07:11 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-12 22:03:35 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-12 22:04:38 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-12 22:02:08 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-12 22:09:41 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-12 22:08:32 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-12 22:01:00 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 22:09:23 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-12 22:33:27 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 22:09:05 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 22:03:10 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:04:44 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:02:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:07:21 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:01:35 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:02:17 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-12 22:12:16 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-12 22:01:39 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-12 22:03:27 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-05-12 22:06:48 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-12 22:00:38 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-05-12 22:06:24 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.015 |  |
| 2026-05-12 22:15:48 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.019 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 22:01:37 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.021 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-12 22:02:16 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-05-12 22:14:31 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.054 |  |
| 2026-05-12 22:07:12 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.063 |  |
| 2026-05-12 22:05:57 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | -0.075 |  |
| 2026-05-12 21:05:06 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.085 |  |
| 2026-05-12 22:02:14 | Katharagama (Menik Ganga) | 1.68 | 🟢 Normal | -0.200 |  |
| 2026-05-12 22:01:59 | Thaldena (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.218 |  |
| 2026-05-12 22:04:34 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.255 |  |
| 2026-05-12 22:04:48 | Nakkala (Kumbukkan Oya) | 3.25 | 🟢 Normal | -0.606 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)