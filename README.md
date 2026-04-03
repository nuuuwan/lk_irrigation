# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_02:28:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,521 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 02:28:07 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:16:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-04-04 02:11:40 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:06:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.069 |  |
| 2026-04-04 02:05:48 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 02:05:12 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-04 02:04:30 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -1.714 |  |
| 2026-04-04 02:04:09 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -1.714 |  |
| 2026-04-04 02:04:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:04:07 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 02:03:15 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.022 |  |
| 2026-04-04 02:02:53 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-04 02:02:28 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-04 02:02:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:02:21 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 02:02:12 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:02:00 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-04-04 02:01:57 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.030 |  |
| 2026-04-04 02:01:33 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:01:25 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:01:23 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-04-04 02:01:19 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.070 |  |
| 2026-04-04 02:01:10 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.160 |  |
| 2026-04-04 02:00:58 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 02:00:45 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-04 02:00:16 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-04 01:44:37 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | 0.044 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 00:09:21 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-04-04 02:16:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-04-04 02:00:16 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-04 02:00:45 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-04 01:44:37 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-04 02:04:07 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 01:04:56 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-04 00:19:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 02:05:48 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 02:02:28 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-04 02:02:21 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 02:00:58 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 02:01:33 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:28:07 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:01:25 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 00:32:26 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:11:40 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:22:11 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:21:06 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:02:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:04:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 01:01:08 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:02:12 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-04 02:02:00 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-04-04 01:09:29 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2026-04-04 00:04:26 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-04-04 02:05:12 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-04 02:02:53 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-04 02:01:23 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-04-04 02:03:15 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.022 |  |
| 2026-04-04 02:01:57 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.030 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-04 02:06:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.069 |  |
| 2026-04-04 02:01:19 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.070 |  |
| 2026-04-03 21:11:08 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.076 |  |
| 2026-04-04 02:01:10 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.160 |  |
| 2026-04-04 02:04:30 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -1.714 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)