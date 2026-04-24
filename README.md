# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_09:11:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,625 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 09:11:34 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-04-24 09:09:30 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:07:11 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-24 09:06:49 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-04-24 09:06:30 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:06:27 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.290 |  |
| 2026-04-24 09:05:12 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.022 |  |
| 2026-04-24 09:05:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-04-24 09:04:41 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.054 |  |
| 2026-04-24 09:04:40 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.032 |  |
| 2026-04-24 09:04:33 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.021 |  |
| 2026-04-24 09:04:23 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:04:06 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.097 |  |
| 2026-04-24 09:04:05 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.057 |  |
| 2026-04-24 09:04:00 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-04-24 09:03:49 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:03:46 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:03:19 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:03:08 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:03:03 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-24 09:03:02 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-24 09:02:44 | Katharagama (Menik Ganga) | 2.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 09:02:39 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:02:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:02:36 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.029 |  |
| 2026-04-24 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.050 |  |
| 2026-04-24 09:02:15 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.011 |  |
| 2026-04-24 09:02:14 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 09:01:36 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 09:01:34 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-04-24 09:01:14 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:01:10 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.030 |  |
| 2026-04-24 09:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:00:52 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-04-24 09:00:52 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:00:35 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:00:19 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:00:17 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:00:16 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 09:03:03 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-24 09:03:02 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-24 09:01:36 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 09:02:44 | Katharagama (Menik Ganga) | 2.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 09:02:14 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 09:02:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:03:08 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:04:23 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:03:19 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:09:30 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:03:46 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:00:35 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:06:30 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 09:03:49 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:00:17 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:00:19 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:00:52 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:02:39 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-24 09:02:15 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.011 |  |
| 2026-04-24 09:06:49 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-04-24 09:11:34 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-04-24 09:00:52 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-04-24 09:07:11 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-24 09:04:33 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.021 |  |
| 2026-04-24 09:05:12 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.022 |  |
| 2026-04-24 09:05:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-04-24 09:02:36 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.029 |  |
| 2026-04-24 09:01:10 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.030 |  |
| 2026-04-24 09:01:34 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-04-24 09:04:40 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.032 |  |
| 2026-04-24 09:04:00 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-04-24 09:00:16 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.042 |  |
| 2026-04-24 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.050 |  |
| 2026-04-24 09:04:41 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.054 |  |
| 2026-04-24 09:04:05 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.057 |  |
| 2026-04-24 08:12:26 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | -0.064 |  |
| 2026-04-24 09:04:06 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.097 |  |
| 2026-04-24 09:06:27 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.290 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)