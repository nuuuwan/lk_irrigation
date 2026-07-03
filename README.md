# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_01:49:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,598 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 01:49:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:24:00 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-04 01:18:01 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-07-04 01:13:22 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-07-04 01:12:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-04 01:09:37 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-04 01:08:15 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:07:51 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 01:06:46 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:06:37 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:06:28 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-07-04 01:05:49 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-07-04 01:05:42 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:05:39 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 01:04:25 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 01:03:56 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.023 |  |
| 2026-07-04 01:03:42 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:03:15 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 01:05:49 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-07-04 01:18:01 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-07-04 01:09:37 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-04 01:12:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-04 01:01:49 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-03 22:01:32 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-04 01:02:51 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 01:07:51 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 01:24:00 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-04 01:01:57 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 01:04:25 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 01:05:39 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 01:00:26 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:01:15 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-03 22:02:10 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:03:15 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:01:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:05:42 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:06:46 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 00:00:27 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:06:37 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:49:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 00:02:42 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:02:21 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:08:15 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:47:16 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 00:03:28 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:03:42 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 01:01:11 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-04 01:06:28 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-07-03 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-07-04 00:05:10 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-07-04 01:02:52 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-04 01:13:22 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-07-04 00:03:46 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-07-04 01:03:56 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.023 |  |
| 2026-07-04 01:00:52 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.055 |  |
| 2026-07-04 01:03:00 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)