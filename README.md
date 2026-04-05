# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_01:14:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,293 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 01:14:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:14:25 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:09:49 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:06:36 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-06 01:06:16 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-04-06 01:06:16 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 01:04:42 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:04:14 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:03:49 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.170 |  |
| 2026-04-06 01:03:36 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.025 |  |
| 2026-04-06 01:03:30 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:03:26 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:02:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:02:49 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:02:12 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:02:03 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:42 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:34 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:33 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-04-06 01:01:22 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:18 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:16 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:14 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 01:01:11 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-04-06 01:00:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:00:55 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:00:35 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:00:32 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 01:00:09 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 00:08:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-06 01:06:36 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-06 01:00:32 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 01:01:14 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 01:06:16 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 01:00:09 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:00:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:02:49 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:09:49 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-06 00:03:13 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:16 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:22 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:18 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 00:01:54 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:42 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:02:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:04:42 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:34 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:14:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:02:03 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:03:26 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:02:12 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:03:30 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-06 00:02:16 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:04:14 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:00:55 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:00:35 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:01:33 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-04-06 01:06:16 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-04-05 23:05:50 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-04-06 01:01:11 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-04-06 01:03:36 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.025 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-06 00:03:14 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | -0.051 |  |
| 2026-04-06 00:05:48 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.056 |  |
| 2026-04-05 21:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.081 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-06 01:03:49 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)