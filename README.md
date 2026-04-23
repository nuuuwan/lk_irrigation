# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_16:25:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,013 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 16:25:31 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.030 |  |
| 2026-04-23 16:23:12 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.023 |  |
| 2026-04-23 16:12:36 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 16:09:20 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:08:29 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-23 16:08:11 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.057 |  |
| 2026-04-23 16:08:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 16:07:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.019 |  |
| 2026-04-23 16:07:27 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-04-23 16:07:23 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 16:07:08 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.042 |  |
| 2026-04-23 16:06:50 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.012 |  |
| 2026-04-23 16:06:31 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.019 |  |
| 2026-04-23 16:06:23 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:05:10 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:04:52 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-23 16:04:49 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-23 16:04:28 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:04:08 | Ellagawa (Kalu Ganga) | 5.27 | 🟢 Normal | -0.059 |  |
| 2026-04-23 16:04:05 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:03:57 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:03:50 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-23 16:03:47 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:03:40 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 16:03:10 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.606 | 🔺 Rising |
| 2026-04-23 16:02:59 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:02:57 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 16:02:53 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-04-23 16:02:39 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:02:34 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-23 16:02:26 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:02:15 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:01:54 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 16:01:37 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:01:26 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:01:13 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-04-23 16:00:53 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.021 |  |
| 2026-04-23 16:00:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-23 16:00:08 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.070 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 16:03:10 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.606 | 🔺 Rising |
| 2026-04-23 16:04:49 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-23 16:02:34 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-23 16:03:50 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-23 16:00:08 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-23 16:08:29 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-23 16:08:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 16:07:23 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 16:04:52 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-23 16:00:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-23 16:02:57 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 16:03:40 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 16:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 16:12:36 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 16:03:47 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:02:26 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:02:39 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:09:20 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:01:54 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:04:05 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:02:15 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-23 16:07:27 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-04-23 16:03:57 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:05:10 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:02:59 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:01:37 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:04:28 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:01:26 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.010 |  |
| 2026-04-23 16:02:53 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-04-23 16:01:13 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-04-23 16:06:50 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.012 |  |
| 2026-04-23 16:06:31 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.019 |  |
| 2026-04-23 16:07:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.019 |  |
| 2026-04-23 16:00:53 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.021 |  |
| 2026-04-23 16:23:12 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.023 |  |
| 2026-04-23 16:25:31 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.030 |  |
| 2026-04-23 16:07:08 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.042 |  |
| 2026-04-23 16:08:11 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.057 |  |
| 2026-04-23 16:04:08 | Ellagawa (Kalu Ganga) | 5.27 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)