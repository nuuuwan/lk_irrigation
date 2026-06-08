# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_02:23:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,279 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 02:23:32 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-06-09 02:09:47 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:09:42 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | -0.018 |  |
| 2026-06-09 02:09:23 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:08:23 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:07:49 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-09 02:07:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-06-09 02:07:04 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.043 |  |
| 2026-06-09 02:06:14 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.034 |  |
| 2026-06-09 02:06:00 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:05:40 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-06-09 02:05:22 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.031 |  |
| 2026-06-09 02:05:02 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 02:04:33 | Hanwella (Kelani Ganga) | 3.59 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-09 02:04:21 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-09 02:03:54 | Putupaula (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-09 02:03:15 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-09 02:03:06 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-09 02:03:04 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:02:59 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 02:02:30 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.014 |  |
| 2026-06-09 02:02:26 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.153 |  |
| 2026-06-09 02:02:26 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:02:19 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-06-09 02:02:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-09 02:02:11 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:02:10 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -0.100 |  |
| 2026-06-09 02:01:40 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 02:03:06 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-09 02:02:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-09 02:04:33 | Hanwella (Kelani Ganga) | 3.59 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-08 18:00:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-09 02:05:02 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 02:02:59 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 01:06:05 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:00:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:03:04 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:02:26 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:28:45 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 18:07:32 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:06:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:09:47 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:06:00 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:08:23 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:09:23 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-09 01:01:58 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:01:40 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 02:00:49 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.005 |  |
| 2026-06-09 02:07:49 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-09 02:03:15 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-09 02:04:21 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-09 02:03:54 | Putupaula (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-09 02:02:30 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.014 |  |
| 2026-06-09 02:09:42 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | -0.018 |  |
| 2026-06-08 23:14:23 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-06-09 02:05:40 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-06-09 02:02:19 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-06-09 02:23:32 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-06-09 01:22:26 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.027 |  |
| 2026-06-09 02:05:22 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.031 |  |
| 2026-06-09 02:07:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-06-09 02:06:14 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.034 |  |
| 2026-06-08 18:02:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.040 |  |
| 2026-06-09 02:07:04 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.043 |  |
| 2026-06-09 00:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.084 |  |
| 2026-06-09 02:02:10 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -0.100 |  |
| 2026-06-09 02:02:26 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)