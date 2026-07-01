# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_12:13:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,331 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 12:13:42 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:13:01 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:12:18 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-01 12:11:50 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-07-01 12:11:37 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-07-01 12:11:23 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-07-01 12:10:43 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-07-01 12:10:10 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:09:47 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-07-01 12:07:48 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:07:36 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:07:26 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.29 | 🟢 Normal | -0.053 |  |
| 2026-07-01 12:06:14 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:06:04 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.026 |  |
| 2026-07-01 12:05:44 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:04:27 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-07-01 12:04:10 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:04:04 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:04:03 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:03:54 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-07-01 12:03:21 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.031 |  |
| 2026-07-01 12:03:04 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.068 |  |
| 2026-07-01 12:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:53 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:40 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:28 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:22 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-07-01 12:02:17 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-01 12:02:13 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:01:53 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:01:41 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 12:01:29 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-07-01 12:01:26 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-07-01 12:01:25 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |
| 2026-07-01 12:01:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:01:10 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-07-01 12:00:36 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-07-01 11:27:39 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 12:11:50 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-07-01 12:00:36 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-07-01 12:02:17 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-01 12:01:41 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 12:12:18 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-01 12:01:53 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:13 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:04:04 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:10:10 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:01:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:13:01 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:28 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 11:04:52 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:53 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:04:03 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:07:48 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:02:40 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:04:10 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:07:36 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:05:44 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-01 10:01:04 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:13:42 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:07:26 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:06:14 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-01 12:04:27 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-07-01 12:09:47 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-07-01 12:10:43 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-07-01 12:02:22 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-07-01 12:01:10 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-07-01 12:03:54 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-07-01 12:01:29 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-07-01 12:01:25 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |
| 2026-07-01 12:11:23 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-07-01 12:06:04 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.026 |  |
| 2026-07-01 12:03:21 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.031 |  |
| 2026-07-01 12:01:26 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-07-01 12:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.29 | 🟢 Normal | -0.053 |  |
| 2026-07-01 12:03:04 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)