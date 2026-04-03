# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_17:22:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,205 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 17:22:35 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-03 17:22:25 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-04-03 17:19:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:15:03 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.005 |  |
| 2026-04-03 17:14:57 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.037 |  |
| 2026-04-03 17:10:47 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-03 17:10:09 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:09:04 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:07:30 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-03 17:06:54 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-03 17:06:52 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-03 17:06:51 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-03 17:06:29 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:06:14 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-04-03 17:05:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:05:42 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-04-03 17:05:18 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 17:04:33 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:04:27 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:04:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-04-03 17:03:52 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 120.000 | 🔺 Rising |
| 2026-04-03 17:03:49 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 120.000 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 17:03:52 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 120.000 | 🔺 Rising |
| 2026-04-03 17:00:51 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 1.565 | 🔺 Rising |
| 2026-04-03 17:01:18 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.504 | 🔺 Rising |
| 2026-04-03 17:06:14 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-04-03 17:06:54 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-03 17:06:52 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-03 17:02:55 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-03 17:00:59 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-03 17:22:35 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-03 17:07:30 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-03 17:10:47 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-03 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-03 17:06:51 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-03 17:02:42 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 17:02:30 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 17:05:18 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 17:02:29 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 17:15:03 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.005 |  |
| 2026-04-03 17:09:04 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:02:21 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:06:29 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:05:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:19:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:01:52 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:03:10 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:04:27 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:04:33 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:10:09 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:03:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:03:27 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:02:26 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:22:25 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-04-03 17:03:44 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-03 17:04:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-04-03 17:05:42 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-04-03 17:03:01 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-04-03 17:14:57 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.037 |  |
| 2026-04-03 17:00:15 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)