# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_13:30:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,834 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 13:30:21 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-05-29 13:23:45 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | -0.016 |  |
| 2026-05-29 13:19:24 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.222 |  |
| 2026-05-29 13:08:44 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.019 |  |
| 2026-05-29 13:07:38 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:07:23 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:06:53 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.037 |  |
| 2026-05-29 13:06:25 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.041 |  |
| 2026-05-29 13:05:23 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:04:40 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:04:27 | Hanwella (Kelani Ganga) | 3.80 | 🟢 Normal | -0.049 |  |
| 2026-05-29 13:04:18 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.021 |  |
| 2026-05-29 13:04:14 | Rathnapura (Kalu Ganga) | 4.49 | 🟢 Normal | -0.085 |  |
| 2026-05-29 13:03:54 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:03:47 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 13:03:25 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:03:22 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.042 |  |
| 2026-05-29 13:03:20 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-29 13:03:12 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.059 |  |
| 2026-05-29 13:03:11 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:03:02 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:59 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-05-29 13:02:51 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:45 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:02:31 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 13:02:26 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:20 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:01:51 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:01:16 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:01:12 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:00:42 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.022 |  |
| 2026-05-29 13:00:37 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:00:34 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:00:24 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:00:20 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 13:23:45 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | -0.016 |  |
| 2026-05-29 13:03:47 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 13:03:20 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-29 13:05:23 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:03:25 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:02:31 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:02:45 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:07:23 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:03:11 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 13:00:34 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:03:02 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:01:16 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:20 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:59 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:00:24 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:07:38 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:51 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:02:26 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 13:03:54 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:01:12 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:04:40 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:00:37 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:00:20 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:01:51 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-29 13:08:44 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.019 |  |
| 2026-05-29 13:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-05-29 13:30:21 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-05-29 13:04:18 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.021 |  |
| 2026-05-29 13:00:42 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.022 |  |
| 2026-05-29 13:06:53 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.037 |  |
| 2026-05-29 13:06:25 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.041 |  |
| 2026-05-29 13:03:22 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.042 |  |
| 2026-05-29 13:04:27 | Hanwella (Kelani Ganga) | 3.80 | 🟢 Normal | -0.049 |  |
| 2026-05-29 13:03:12 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.059 |  |
| 2026-05-29 13:04:14 | Rathnapura (Kalu Ganga) | 4.49 | 🟢 Normal | -0.085 |  |
| 2026-05-29 13:19:24 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.222 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)