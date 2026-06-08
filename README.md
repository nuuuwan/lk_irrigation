# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_22:05:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,141 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 22:05:45 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-08 22:05:33 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:05:31 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:05:10 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.020 |  |
| 2026-06-08 22:04:25 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.101 |  |
| 2026-06-08 22:04:19 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:04:14 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.032 |  |
| 2026-06-08 22:03:47 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:03:28 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:03:25 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-08 22:03:01 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-06-08 22:02:43 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:02:37 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:02:35 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 22:02:18 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.070 |  |
| 2026-06-08 22:02:15 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-06-08 22:02:09 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 22:01:29 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:01:06 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:00:58 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 21:22:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.053 |  |
| 2026-06-08 21:15:54 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-08 21:15:44 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 22:05:45 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-08 21:06:57 | Peradeniya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-08 21:03:45 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-08 18:00:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-08 21:05:33 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 22:02:09 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 22:02:35 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 22:03:47 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-08 21:02:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:04:19 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:00:58 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 18:07:32 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 21:15:54 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:05:33 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:05:31 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:03:28 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 21:03:34 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:02:43 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:01:06 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:01:29 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 21:06:21 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-08 22:03:25 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-08 22:02:15 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-06-08 22:03:01 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-06-08 21:07:59 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.011 |  |
| 2026-06-08 21:09:39 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-06-08 21:05:28 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.012 |  |
| 2026-06-08 21:15:44 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.018 |  |
| 2026-06-08 22:05:10 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.020 |  |
| 2026-06-08 21:02:42 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.021 |  |
| 2026-06-08 21:04:22 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | -0.030 |  |
| 2026-06-08 22:04:14 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.032 |  |
| 2026-06-08 18:02:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.040 |  |
| 2026-06-08 21:04:43 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.051 |  |
| 2026-06-08 21:22:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.053 |  |
| 2026-06-08 21:05:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-06-08 22:02:18 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.070 |  |
| 2026-06-08 22:04:25 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.101 |  |
| 2026-06-08 21:04:01 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)