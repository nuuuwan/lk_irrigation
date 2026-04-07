# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_06:14:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,355 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 06:14:51 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:13:51 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.006 |  |
| 2026-04-07 06:08:28 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-07 06:07:36 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-07 06:07:19 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-07 06:07:18 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-07 06:06:44 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.125 |  |
| 2026-04-07 06:06:42 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.126 |  |
| 2026-04-07 06:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.075 |  |
| 2026-04-07 06:06:13 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:05:44 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:05:39 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:05:29 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-07 06:04:40 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.060 |  |
| 2026-04-07 06:04:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.062 |  |
| 2026-04-07 06:04:08 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 06:04:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:03:59 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-07 06:03:54 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-07 06:02:54 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:02:50 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:02:50 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.083 |  |
| 2026-04-07 06:02:30 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:02:26 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-07 06:02:23 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.043 |  |
| 2026-04-07 06:02:23 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 06:02:22 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.037 |  |
| 2026-04-07 06:02:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:02:06 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.042 |  |
| 2026-04-07 06:01:58 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-07 06:01:55 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-04-07 06:01:53 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.093 |  |
| 2026-04-07 06:01:38 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:01:29 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:01:10 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:01:03 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-04-07 06:00:09 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-07 05:50:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.075 |  |
| 2026-04-07 05:46:21 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.037 |  |
| 2026-04-07 05:43:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.075 |  |
| 2026-04-07 05:43:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:43:09 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:38:11 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.126 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 06:07:36 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-07 06:02:26 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-07 06:03:54 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-07 06:07:18 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-07 06:07:19 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-07 06:04:08 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 06:01:58 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-07 06:02:23 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 06:08:28 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-07 06:02:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:01:03 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:01:38 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:01:29 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:04:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:02:50 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:02:30 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:02:54 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:05:39 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:14:51 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:06:13 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:01:10 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:13:51 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.006 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-07 06:03:59 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-07 06:05:29 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-07 06:00:09 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-07 06:01:55 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-04-07 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-04-07 06:02:22 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.037 |  |
| 2026-04-07 06:02:06 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.042 |  |
| 2026-04-07 06:02:23 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.043 |  |
| 2026-04-07 06:04:40 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.060 |  |
| 2026-04-07 06:04:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.062 |  |
| 2026-04-07 06:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.075 |  |
| 2026-04-07 06:02:50 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.083 |  |
| 2026-04-07 06:01:53 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.093 |  |
| 2026-04-07 06:06:44 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.125 |  |
| 2026-04-07 06:06:42 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)