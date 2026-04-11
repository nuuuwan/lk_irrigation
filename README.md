# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_05:43:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 05:43:43 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-04-11 05:16:24 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-11 05:13:08 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:11:43 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-11 05:11:29 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:10:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-04-11 05:09:09 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-11 05:08:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-04-11 05:08:55 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 05:08:00 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.055 |  |
| 2026-04-11 05:06:47 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 05:06:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-04-11 05:05:50 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:05:08 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.250 |  |
| 2026-04-11 05:04:45 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:04:25 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-11 05:04:10 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:04:06 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:04:00 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 05:03:46 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 05:03:34 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-11 05:03:15 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:02:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:02:43 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 05:02:37 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:59 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:59 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:35 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:08 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:04 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-11 05:00:57 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-11 05:00:51 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-11 05:00:35 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:00:13 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.110 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 18:06:03 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-11 05:08:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-04-11 05:09:09 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-11 05:02:43 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 05:08:55 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 05:00:57 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-11 05:03:34 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-11 05:06:47 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 05:11:43 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-11 05:04:00 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 05:03:46 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 05:05:50 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:04 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:00:35 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:59 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:08 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:02:37 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:13:08 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:03:15 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:04:10 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:59 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:04:06 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:04:45 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:02:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:35 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:11:29 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-11 04:19:20 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:16:24 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-11 05:04:25 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-11 05:00:51 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-11 05:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-11 05:43:43 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-04-11 05:10:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-04-11 05:08:00 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.055 |  |
| 2026-04-11 05:06:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-04-11 05:00:13 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.110 |  |
| 2026-04-11 05:05:08 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.250 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)