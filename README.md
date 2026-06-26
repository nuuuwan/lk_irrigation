# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_20:22:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 20:22:34 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.023 |  |
| 2026-06-26 20:19:00 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:14:29 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.018 |  |
| 2026-06-26 20:14:09 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-26 20:11:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:08:48 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:08:37 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-06-26 20:08:01 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.013 |  |
| 2026-06-26 20:07:41 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:07:37 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.038 |  |
| 2026-06-26 20:07:34 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-26 20:06:39 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-06-26 20:06:32 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-26 20:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:05:27 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:05:22 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:04:35 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:04:34 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:04:21 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-06-26 20:03:39 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:03:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-06-26 20:02:59 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.021 |  |
| 2026-06-26 20:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:48 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:32 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:24 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:22 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-06-26 20:02:15 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-26 20:02:13 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:11 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:08 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 20:01:47 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:01:42 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-06-26 20:01:35 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 19:59:05 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 20:01:42 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-06-26 20:06:39 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-06-26 20:02:15 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-26 20:06:32 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-26 20:14:09 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-26 20:07:34 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-26 19:59:05 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-26 20:02:08 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 20:05:27 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:11 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:13 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:11:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:08:48 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:01:47 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:06:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:01:35 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:24 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:32 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:19:00 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:02:48 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:07:41 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:04:35 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:03:39 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:04:34 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:05:22 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:08:37 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-06-26 20:04:21 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-06-26 20:08:01 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.013 |  |
| 2026-06-26 20:14:29 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.018 |  |
| 2026-06-26 20:02:59 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.021 |  |
| 2026-06-26 20:02:22 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-06-26 20:22:34 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.023 |  |
| 2026-06-26 20:03:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-06-26 20:07:37 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.038 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)