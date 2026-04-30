# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_22:08:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,458 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 22:08:26 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-04-30 22:08:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:07:49 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 22:07:34 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:07:18 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.060 |  |
| 2026-04-30 22:06:38 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-30 22:06:37 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.021 |  |
| 2026-04-30 22:06:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-30 22:06:31 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 22:05:29 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-30 22:05:10 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:05:04 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 22:05:02 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-30 22:04:55 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:04:21 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-30 22:04:02 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-04-30 22:03:46 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:03:36 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-04-30 22:03:36 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:03:29 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:03:27 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.779 | 🔺 Rising |
| 2026-04-30 22:02:49 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.551 |  |
| 2026-04-30 22:02:24 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-30 22:02:09 | Yaka Wewa (Ma Oya) | 1.76 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-04-30 22:01:57 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-04-30 22:01:39 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:01:32 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 22:01:28 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:01:11 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-30 22:01:09 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-30 22:00:50 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:00:29 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-30 22:00:07 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:51:27 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 22:03:27 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.779 | 🔺 Rising |
| 2026-04-30 22:02:09 | Yaka Wewa (Ma Oya) | 1.76 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-04-30 21:02:59 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-30 22:05:29 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-30 22:00:29 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-30 22:01:09 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-30 22:01:11 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-30 22:06:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-30 22:01:32 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 22:05:04 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 22:07:49 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 22:06:31 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 22:01:28 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:03:29 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:06:18 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:08:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:04:55 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:00:07 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:03:46 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:03:36 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:07:34 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:05:10 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:01:39 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:06:38 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-30 22:04:21 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-30 22:02:24 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-30 22:05:02 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-30 22:04:02 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:04:09 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-04-30 22:01:57 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-04-30 22:08:26 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-04-30 22:06:37 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.021 |  |
| 2026-04-30 22:03:36 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-04-30 22:07:18 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.060 |  |
| 2026-04-30 22:02:49 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.551 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)