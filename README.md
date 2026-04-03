# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_18:09:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,243 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 18:09:52 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:06:45 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-04-03 18:05:49 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-03 18:05:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.120 |  |
| 2026-04-03 18:05:32 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-03 18:05:28 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:05:21 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.031 |  |
| 2026-04-03 18:05:09 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:05:00 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-04-03 18:04:58 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:04:46 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:04:23 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.144 |  |
| 2026-04-03 18:04:18 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.012 |  |
| 2026-04-03 18:03:46 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:22 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.038 |  |
| 2026-04-03 18:03:18 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:15 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 18:03:13 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:10 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:07 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:00 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-03 18:02:59 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.126 |  |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:41 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-03 18:02:35 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 18:05:00 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-04-03 18:02:10 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-03 18:01:55 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-03 18:05:49 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-03 18:03:15 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 18:00:29 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-03 18:02:41 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-03 18:01:45 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-03 18:02:16 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:05:28 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:01:30 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:00:23 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:07 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:46 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:05:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:09:52 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:19:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:01:39 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:10 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:13 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:04:58 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:03:18 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:02:35 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:05:09 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:05:32 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:01:29 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 18:04:18 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.012 |  |
| 2026-04-03 18:06:45 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-04-03 18:03:00 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-03 18:05:21 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.031 |  |
| 2026-04-03 18:03:22 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.038 |  |
| 2026-04-03 18:00:18 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.052 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-03 18:05:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.120 |  |
| 2026-04-03 18:02:59 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.126 |  |
| 2026-04-03 18:04:23 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)