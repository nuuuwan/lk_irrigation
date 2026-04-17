# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_16:22:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,656 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 16:22:39 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-17 16:10:22 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:09:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.018 |  |
| 2026-04-17 16:06:43 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:06:02 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.122 |  |
| 2026-04-17 16:06:00 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-17 16:05:40 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:05:23 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:05:18 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:05:13 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:04:53 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-04-17 16:04:25 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-04-17 16:04:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:03:34 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:03:33 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:27 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:25 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:25 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-04-17 16:03:24 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:03:02 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:00 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:51 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:46 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:46 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 16:02:39 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:02:21 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:15 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-17 16:01:59 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.032 |  |
| 2026-04-17 16:01:34 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:01:05 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.019 |  |
| 2026-04-17 16:01:01 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:00:57 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:00:43 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:00:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-04-17 16:00:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 16:22:39 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-17 16:02:15 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-17 16:06:00 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-17 16:02:46 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 16:00:43 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:02 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:51 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:25 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:00:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:27 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:09:21 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:00 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:01:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:46 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:05:13 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:05:40 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:06:08 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:21 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:33 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:00:57 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:39 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:04:25 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-04-17 16:05:18 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:05:23 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:01:01 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:04:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:01:34 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:10:22 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:03:34 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:03:24 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:06:43 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:09:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.018 |  |
| 2026-04-17 16:01:05 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.019 |  |
| 2026-04-17 16:03:25 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-04-17 16:00:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-04-17 16:01:59 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.032 |  |
| 2026-04-17 16:04:53 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-04-17 16:06:02 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)