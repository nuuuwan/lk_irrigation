# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_14:21:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,027 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 14:21:53 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:16:29 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.041 |  |
| 2026-04-22 14:15:07 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:13:10 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:11:10 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:10:45 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.059 |  |
| 2026-04-22 14:09:54 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:09:48 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:08:36 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:08:23 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-22 14:08:16 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:07:06 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:06:55 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-22 14:06:07 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:06:03 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.091 |  |
| 2026-04-22 14:05:10 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-04-22 14:04:29 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.039 |  |
| 2026-04-22 14:04:09 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-22 14:03:31 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-04-22 14:03:26 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:03:20 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 14:03:19 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-04-22 14:03:17 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.039 |  |
| 2026-04-22 14:02:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-04-22 14:02:53 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.031 |  |
| 2026-04-22 14:02:41 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-04-22 14:02:41 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:02:09 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-04-22 14:02:03 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:02:03 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.044 |  |
| 2026-04-22 14:02:00 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:01:53 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-04-22 14:01:51 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.041 |  |
| 2026-04-22 14:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:01:48 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-22 14:01:38 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:01:34 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | -0.040 |  |
| 2026-04-22 14:01:30 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-22 14:01:20 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 14:01:48 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-22 14:01:30 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-22 14:08:23 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-22 14:03:20 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 14:06:55 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-22 14:01:38 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:01:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:21:53 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:08:36 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:07:06 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:09:54 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:08:16 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:13:10 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-22 14:05:10 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-04-22 14:06:07 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:11:10 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:02:03 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:02:00 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:02:41 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:03:26 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:04:29 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-22 14:01:53 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-04-22 14:02:41 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-04-22 14:02:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-04-22 14:04:09 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-22 14:03:31 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-04-22 14:03:19 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-04-22 14:01:20 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-04-22 14:02:53 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.031 |  |
| 2026-04-22 14:03:17 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.039 |  |
| 2026-04-22 14:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.039 |  |
| 2026-04-22 14:02:09 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-04-22 14:01:34 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | -0.040 |  |
| 2026-04-22 14:01:51 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.041 |  |
| 2026-04-22 14:16:29 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.041 |  |
| 2026-04-22 14:02:03 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.044 |  |
| 2026-04-22 14:10:45 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.059 |  |
| 2026-04-22 14:06:03 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)