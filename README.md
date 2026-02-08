# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_06:33:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,222 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 06:33:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.002 |  |
| 2026-02-08 06:18:07 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.175 |  |
| 2026-02-08 06:15:33 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.008 |  |
| 2026-02-08 06:11:45 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:10:37 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:10:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-08 06:09:22 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:08:52 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:07:43 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:07:33 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-08 06:07:27 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-08 06:06:13 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.117 |  |
| 2026-02-08 06:05:58 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-02-08 06:05:45 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:05:16 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:05:14 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-02-08 06:04:57 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:04:26 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.034 |  |
| 2026-02-08 06:04:23 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.048 |  |
| 2026-02-08 06:04:21 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-02-08 06:04:08 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:04:00 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:03:57 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:03:36 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.054 |  |
| 2026-02-08 06:03:13 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-02-08 06:02:43 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.041 |  |
| 2026-02-08 06:02:42 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:01:47 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | 0.002 |  |
| 2026-02-08 06:01:42 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-02-08 06:01:31 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-08 06:01:13 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.102 |  |
| 2026-02-08 06:01:09 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:00:55 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:00:53 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 06:00:49 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:00:40 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-08 06:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:00:13 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.194 |  |
| 2026-02-08 05:57:33 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.175 |  |
| 2026-02-08 05:53:07 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 06:07:33 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-08 06:07:27 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-08 06:10:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-08 06:01:31 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-08 06:00:53 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 06:01:47 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | 0.002 |  |
| 2026-02-08 06:33:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.002 |  |
| 2026-02-08 06:00:49 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:05:45 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 05:01:49 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:03:57 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:09:22 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:08:52 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:02:42 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:00:55 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:05:16 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:04:08 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:11:45 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:07:43 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:04:57 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:01:09 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:04:00 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-08 06:15:33 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.008 |  |
| 2026-02-08 06:01:42 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-02-08 06:05:14 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-02-08 06:05:58 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-02-08 06:00:40 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-08 06:04:21 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-02-08 06:03:13 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-02-08 06:04:26 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.034 |  |
| 2026-02-08 06:02:43 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.041 |  |
| 2026-02-08 06:04:23 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.048 |  |
| 2026-02-08 06:03:36 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.054 |  |
| 2026-02-08 06:01:13 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.102 |  |
| 2026-02-08 06:06:13 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.117 |  |
| 2026-02-08 06:18:07 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.175 |  |
| 2026-02-08 06:00:13 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)