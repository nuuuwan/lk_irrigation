# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_03:21:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,529 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 03:21:36 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.007 |  |
| 2026-06-07 03:19:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:14:33 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -18.000 |  |
| 2026-06-07 03:14:31 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -18.000 |  |
| 2026-06-07 03:12:55 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-07 03:12:03 | Rathnapura (Kalu Ganga) | 2.64 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 03:10:21 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:09:13 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.045 |  |
| 2026-06-07 03:07:42 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-07 03:07:15 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.994 | 🔺 Rising |
| 2026-06-07 03:07:09 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:06:43 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:06:19 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 03:05:36 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-07 03:05:05 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 03:05:01 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.031 |  |
| 2026-06-07 03:04:54 | Ellagawa (Kalu Ganga) | 7.04 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:04:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-07 03:04:50 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-06-07 03:04:35 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 03:04:19 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | -0.021 |  |
| 2026-06-07 03:03:42 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-07 03:03:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:03:15 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:03:10 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -1.565 |  |
| 2026-06-07 03:03:07 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 03:03:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:02:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 03:02:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-07 03:02:47 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -1.565 |  |
| 2026-06-07 03:01:39 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:01:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 03:07:15 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.994 | 🔺 Rising |
| 2026-06-07 03:02:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-07 03:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-07 03:07:42 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-07 03:03:07 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 03:05:36 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-07 03:02:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 03:12:03 | Rathnapura (Kalu Ganga) | 2.64 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 03:04:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-07 03:12:55 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-07 03:05:05 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 03:06:19 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 03:04:35 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:03:15 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:01:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:07:58 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:10:21 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:01:39 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:03:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:19:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 02:10:09 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:06:43 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:07:09 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:04:50 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-06-07 03:21:36 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.007 |  |
| 2026-06-07 03:04:54 | Ellagawa (Kalu Ganga) | 7.04 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:03:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-07 03:03:42 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:08:42 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-06-07 03:04:19 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | -0.021 |  |
| 2026-06-07 00:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.023 |  |
| 2026-06-07 03:05:01 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.031 |  |
| 2026-06-07 03:09:13 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.045 |  |
| 2026-06-07 03:03:10 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -1.565 |  |
| 2026-06-07 03:14:33 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)