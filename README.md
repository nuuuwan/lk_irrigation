# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_13:20:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 13:20:51 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.008 |  |
| 2026-04-13 13:15:37 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.106 |  |
| 2026-04-13 13:10:17 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-13 13:09:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 13:07:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-13 13:07:01 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 13:06:59 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:06:52 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 13:06:34 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.028 |  |
| 2026-04-13 13:06:30 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:05:37 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 13:05:06 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:04:46 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.028 |  |
| 2026-04-13 13:04:34 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:04:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-13 13:03:58 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-13 13:03:54 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:03:43 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 13:03:33 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-13 13:03:23 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.031 |  |
| 2026-04-13 13:03:19 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-04-13 13:03:05 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | -0.093 |  |
| 2026-04-13 13:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.020 |  |
| 2026-04-13 13:03:01 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:02:53 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:02:47 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.012 |  |
| 2026-04-13 13:02:42 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-04-13 13:02:35 | Katharagama (Menik Ganga) | -0.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-13 13:02:33 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-04-13 13:01:55 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.185 |  |
| 2026-04-13 13:01:50 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-13 13:01:50 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-13 13:01:46 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-13 13:01:39 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -18.000 |  |
| 2026-04-13 13:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:01:37 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -18.000 |  |
| 2026-04-13 13:01:14 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-13 13:01:09 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.051 |  |
| 2026-04-13 13:00:57 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:00:51 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:00:38 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 13:02:35 | Katharagama (Menik Ganga) | -0.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-13 13:01:50 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-13 13:03:58 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-13 13:01:46 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-13 13:07:01 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 13:01:50 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-13 13:09:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 13:03:33 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-13 13:03:43 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 13:10:17 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-13 13:01:14 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-13 13:05:37 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 13:06:52 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 13:05:06 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:06:59 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:00:57 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:03:54 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:02:53 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:00:38 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:03:01 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:06:30 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:00:51 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:04:34 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:20:51 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.008 |  |
| 2026-04-13 13:04:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-13 13:07:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-13 13:02:47 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.012 |  |
| 2026-04-13 13:02:42 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-04-13 13:03:19 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-04-13 13:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.020 |  |
| 2026-04-13 13:06:34 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.028 |  |
| 2026-04-13 13:04:46 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.028 |  |
| 2026-04-13 13:03:23 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.031 |  |
| 2026-04-13 13:02:33 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-04-13 13:01:09 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.051 |  |
| 2026-04-13 13:03:05 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | -0.093 |  |
| 2026-04-13 13:15:37 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.106 |  |
| 2026-04-13 13:01:55 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.185 |  |
| 2026-04-13 13:01:39 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)