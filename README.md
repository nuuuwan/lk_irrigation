# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_01:22:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,494 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 01:22:11 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:21:06 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:09:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-04 01:09:29 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2026-04-04 01:08:27 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.045 |  |
| 2026-04-04 01:07:51 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:06:24 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-04-04 01:06:22 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-04 01:05:49 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-04 01:05:41 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 01:04:56 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-04 01:04:35 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 01:04:30 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.051 |  |
| 2026-04-04 01:04:01 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-04 01:03:32 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-04-04 01:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 2.835 | 🔺 Rising |
| 2026-04-04 01:03:08 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-04 01:02:42 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.030 |  |
| 2026-04-04 01:02:32 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-04 01:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:02:19 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-04 01:02:17 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-04 01:02:11 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:01:24 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-04 01:01:14 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-04-04 01:01:12 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.142 |  |
| 2026-04-04 01:01:08 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 2.835 | 🔺 Rising |
| 2026-04-04 01:01:00 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 01:00:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-04 00:56:31 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.123 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 01:02:19 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-04 01:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 2.835 | 🔺 Rising |
| 2026-04-04 00:09:21 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-04-04 01:06:24 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-04-04 01:01:24 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-04 01:02:32 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-04 01:04:56 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-04 01:06:22 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-04 00:19:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 01:05:41 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 01:09:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-04 01:01:00 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 01:04:35 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 01:07:51 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:00:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-04 00:32:26 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:22:11 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:21:06 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 00:06:02 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:01:08 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:02:11 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:05:49 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-04 01:01:14 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-04-04 01:03:08 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-04 01:04:01 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-04 01:09:29 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2026-04-04 00:04:26 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-04-04 01:03:32 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-04-04 01:02:42 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.030 |  |
| 2026-04-04 00:03:19 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.039 |  |
| 2026-04-04 01:08:27 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.045 |  |
| 2026-04-04 01:04:30 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.051 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-03 21:11:08 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.076 |  |
| 2026-04-04 00:36:50 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.114 |  |
| 2026-04-04 01:01:12 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)