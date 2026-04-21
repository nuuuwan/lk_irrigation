# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_14:22:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,132 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 14:22:05 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:15:49 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-04-21 14:12:42 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.035 |  |
| 2026-04-21 14:09:21 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-04-21 14:08:59 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.036 |  |
| 2026-04-21 14:08:39 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-04-21 14:07:53 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.029 |  |
| 2026-04-21 14:06:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-04-21 14:06:09 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-04-21 14:05:49 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:05:43 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:05:12 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.081 |  |
| 2026-04-21 14:04:44 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:04:43 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:04:42 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-04-21 14:04:35 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.031 |  |
| 2026-04-21 14:04:19 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:04:16 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:03:59 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.064 |  |
| 2026-04-21 14:03:20 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.070 |  |
| 2026-04-21 14:03:07 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-21 14:03:05 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.139 |  |
| 2026-04-21 14:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:02:43 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:02:39 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-21 14:02:37 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 14:02:30 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.040 |  |
| 2026-04-21 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-04-21 14:02:06 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:02:05 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.016 |  |
| 2026-04-21 14:01:23 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.011 |  |
| 2026-04-21 14:01:19 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:01:02 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 14:00:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.162 |  |
| 2026-04-21 14:00:55 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.045 |  |
| 2026-04-21 14:00:50 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.025 |  |
| 2026-04-21 14:00:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:00:11 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:58:07 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:57:31 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 14:03:07 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-21 14:06:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-04-21 14:02:39 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-21 14:02:37 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 14:01:02 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 13:57:31 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 14:00:11 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:22:05 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:01:19 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:04:16 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:05:43 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:00:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 14:04:44 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:21:22 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-04-21 14:08:39 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-04-21 14:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:02:43 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:05:49 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:02:06 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:04:43 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-21 14:01:23 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.011 |  |
| 2026-04-21 14:02:05 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.016 |  |
| 2026-04-21 14:15:49 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-04-21 14:06:09 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-04-21 14:00:50 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.025 |  |
| 2026-04-21 14:09:21 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-04-21 14:07:53 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.029 |  |
| 2026-04-21 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-04-21 14:04:42 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-04-21 14:04:35 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.031 |  |
| 2026-04-21 14:12:42 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.035 |  |
| 2026-04-21 14:08:59 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.036 |  |
| 2026-04-21 14:02:30 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.040 |  |
| 2026-04-21 14:00:55 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.045 |  |
| 2026-04-21 14:03:59 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.064 |  |
| 2026-04-21 14:03:20 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.070 |  |
| 2026-04-21 14:05:12 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.081 |  |
| 2026-04-21 14:03:05 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.139 |  |
| 2026-04-21 14:00:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)