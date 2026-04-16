# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_10:37:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,528 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 10:37:42 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.013 |  |
| 2026-04-16 10:09:01 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:08:50 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:07:55 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-04-16 10:07:51 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:07:38 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-04-16 10:06:30 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:06:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 10:06:00 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.028 |  |
| 2026-04-16 10:05:35 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-16 10:05:28 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:05:07 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-16 10:04:46 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.033 |  |
| 2026-04-16 10:04:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:04:37 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:04:37 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-16 10:04:31 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-04-16 10:04:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-16 10:04:16 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:04:09 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-16 10:03:48 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | -0.068 |  |
| 2026-04-16 10:03:36 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:03:16 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:03:01 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:03:01 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:02:54 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-16 10:02:38 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 10:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.090 |  |
| 2026-04-16 10:02:09 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-04-16 10:01:57 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.091 |  |
| 2026-04-16 10:01:45 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-04-16 10:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.051 |  |
| 2026-04-16 10:01:24 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.023 |  |
| 2026-04-16 10:01:15 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.103 |  |
| 2026-04-16 10:01:14 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-04-16 10:01:10 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.024 |  |
| 2026-04-16 10:01:08 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-04-16 10:00:20 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 10:04:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-16 10:04:37 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-16 10:02:54 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-16 10:05:07 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-16 10:05:35 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-16 10:06:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 10:02:38 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 10:03:16 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:04:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:04:37 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:08:50 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:02:50 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:06:30 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:03:36 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:09:01 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:07:51 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:03:01 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:03:01 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:04:16 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:05:28 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-16 10:02:09 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-04-16 10:07:38 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-04-16 10:04:09 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-16 10:00:20 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-16 10:01:14 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-04-16 10:37:42 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.013 |  |
| 2026-04-16 10:07:55 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-04-16 10:01:45 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-04-16 10:01:24 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.023 |  |
| 2026-04-16 10:01:10 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.024 |  |
| 2026-04-16 10:06:00 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.028 |  |
| 2026-04-16 10:04:31 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-04-16 10:01:08 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-04-16 10:04:46 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.033 |  |
| 2026-04-16 10:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.051 |  |
| 2026-04-16 10:03:48 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | -0.068 |  |
| 2026-04-16 10:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.090 |  |
| 2026-04-16 10:01:57 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.091 |  |
| 2026-04-16 10:01:15 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)