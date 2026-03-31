# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_15:07:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,426 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 15:07:51 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.009 |  |
| 2026-03-31 15:07:26 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-31 15:06:08 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:06:03 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:05:42 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 15:04:57 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.041 |  |
| 2026-03-31 15:04:55 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-03-31 15:04:51 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:04:51 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:04:23 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:04:17 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-31 15:04:00 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 15:03:39 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-31 15:03:29 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:03:24 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-31 15:02:40 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:02:18 | Giriulla (Maha Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-31 15:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:02:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-31 15:02:12 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:01:50 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:01:48 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-03-31 15:01:47 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2026-03-31 15:01:36 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 15:01:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:01:31 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:01:13 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-31 15:00:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:00:43 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:00:41 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.179 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 13:02:17 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-31 14:11:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-31 15:04:17 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-31 15:07:26 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-31 15:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-31 14:01:09 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-31 15:03:39 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-31 15:04:00 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 15:01:36 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 15:05:42 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 15:04:23 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 14:01:32 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:01:50 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:04:51 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:01:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:06:03 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:45 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:01:13 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:04:51 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:02:40 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-31 14:06:06 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-31 14:02:32 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:06:08 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:00:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 14:06:41 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:02:12 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:00:43 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:01:31 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:03:29 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:07:51 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.009 |  |
| 2026-03-31 15:01:48 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-03-31 15:02:18 | Giriulla (Maha Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-31 15:03:24 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-31 15:02:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-31 15:04:55 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-03-31 15:01:47 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2026-03-31 15:04:57 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.041 |  |
| 2026-03-31 15:00:41 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)