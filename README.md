# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_05:10:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,629 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 05:10:56 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-04-04 05:10:29 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-04 05:10:03 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:09:33 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.014 |  |
| 2026-04-04 05:07:53 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-04 05:07:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.120 |  |
| 2026-04-04 05:06:57 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:06:13 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-04 05:05:33 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.137 |  |
| 2026-04-04 05:04:52 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.120 |  |
| 2026-04-04 05:04:51 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 05:03:44 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-04-04 05:03:16 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 05:03:16 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.005 |  |
| 2026-04-04 05:02:48 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 05:02:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:02:18 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:02:10 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:01:56 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-04 05:01:41 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:01:24 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 05:01:21 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-04-04 05:01:10 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:00:51 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 05:00:12 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:00:10 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-04 04:54:03 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-04-04 04:34:22 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:33:24 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.008 |  |
| 2026-04-04 04:27:27 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.014 |  |
| 2026-04-04 04:24:24 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 05:10:56 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-04-04 04:09:53 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-04-04 05:03:44 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-04-04 05:07:53 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-04 05:00:10 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-04 05:10:29 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-04 03:04:40 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 05:04:51 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 05:00:51 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 05:01:24 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 05:03:16 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 04:17:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-04 05:02:48 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 04:10:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 05:00:12 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:01:56 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:06:57 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:01:41 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:02:18 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:10:03 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:02:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:01:10 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:02:10 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-04 05:03:16 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.005 |  |
| 2026-04-04 04:24:24 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.005 |  |
| 2026-04-04 04:33:24 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.008 |  |
| 2026-04-04 05:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-04 05:01:21 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-04-04 04:05:19 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-04 05:09:33 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.014 |  |
| 2026-04-04 00:04:26 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-04-04 05:06:13 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-04 05:04:52 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.120 |  |
| 2026-04-04 05:07:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.120 |  |
| 2026-04-04 05:05:33 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.137 |  |
| 2026-04-04 04:06:22 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)