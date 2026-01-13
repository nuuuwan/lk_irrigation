# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_07:19:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,255 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 07:19:28 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:19:07 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:16:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:13:43 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:13:08 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 07:12:48 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:10:27 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-13 07:09:11 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 07:07:06 | Baddegama (Gin Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:06:57 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:06:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-01-13 07:06:12 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.019 |  |
| 2026-01-13 07:05:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.057 |  |
| 2026-01-13 07:05:15 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | -0.048 |  |
| 2026-01-13 07:05:07 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 07:04:50 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:03:42 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:03:28 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-01-13 07:03:12 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-13 07:03:02 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:03:00 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:02:56 | Horowpothana (Yan Oya) | 3.59 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-13 07:02:52 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-13 07:02:42 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:02:14 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 07:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.060 |  |
| 2026-01-13 07:01:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:01:42 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 07:01:37 | Weraganthota (Mahaweli Ganga) | -1.44 | 🟢 Normal | -0.100 |  |
| 2026-01-13 07:01:17 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:01:13 | Thanthirimale (Malwathu Oya) | 2.53 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-13 07:01:11 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.107 |  |
| 2026-01-13 07:01:08 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.032 |  |
| 2026-01-13 07:00:58 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:00:58 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 07:00:36 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-01-13 07:00:15 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-13 06:29:53 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:29:35 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-13 06:25:33 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | -0.100 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 07:06:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-01-13 07:02:52 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-13 07:01:13 | Thanthirimale (Malwathu Oya) | 2.53 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-13 07:02:56 | Horowpothana (Yan Oya) | 3.59 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-13 07:10:27 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-13 07:05:07 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 07:03:12 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-13 07:02:14 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 07:01:42 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 07:00:58 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 07:13:08 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 07:09:11 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 07:03:02 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:19:28 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:15 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:12:48 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:04:50 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:02:42 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:06:57 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:19:07 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:13:43 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:16:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:01:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:07:06 | Baddegama (Gin Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:03:42 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:03:00 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:01:17 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-13 07:03:28 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-01-13 07:06:12 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.019 |  |
| 2026-01-13 07:00:15 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-13 07:00:36 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-01-13 07:01:08 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.032 |  |
| 2026-01-13 07:05:15 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | -0.048 |  |
| 2026-01-13 07:05:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.057 |  |
| 2026-01-13 07:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.060 |  |
| 2026-01-13 07:01:37 | Weraganthota (Mahaweli Ganga) | -1.44 | 🟢 Normal | -0.100 |  |
| 2026-01-13 07:01:11 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)