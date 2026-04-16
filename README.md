# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_00:22:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,059 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 00:22:45 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.017 |  |
| 2026-04-17 00:19:05 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:08:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.074 |  |
| 2026-04-17 00:08:10 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-17 00:07:30 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:06:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:06:03 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-17 00:05:15 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-17 00:05:12 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.041 |  |
| 2026-04-17 00:05:01 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-17 00:04:45 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:04:06 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 00:03:39 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-17 00:03:39 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 00:03:24 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 00:03:21 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-17 00:03:16 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-04-17 00:03:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:56 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-04-17 00:02:41 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:38 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:32 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:27 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:19 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-04-17 00:01:51 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:01:48 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:01:47 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-04-17 00:01:42 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.030 |  |
| 2026-04-17 00:01:39 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 00:01:18 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-17 00:01:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-17 00:00:20 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 00:02:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-04-17 00:06:03 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-17 00:01:18 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-17 00:03:39 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 00:08:10 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-17 00:01:39 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 00:03:24 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 00:04:06 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 00:03:21 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-17 00:05:01 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-17 00:06:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:27 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:01:48 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:07:30 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-16 23:01:00 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:41 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:32 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:04:45 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:01:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:00:20 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:03:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:19:05 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:56 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:38 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:01:51 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-16 22:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:05:15 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-17 00:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-17 00:03:16 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-04-17 00:03:39 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-17 00:22:45 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.017 |  |
| 2026-04-17 00:01:47 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-04-17 00:01:42 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.030 |  |
| 2026-04-17 00:02:19 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-04-17 00:05:12 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.041 |  |
| 2026-04-17 00:08:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.074 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)