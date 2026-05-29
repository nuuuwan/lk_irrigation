# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_14:41:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,873 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 14:41:07 | Baddegama (Gin Ganga) | 3.31 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-05-29 14:39:15 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:24:22 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-29 14:20:15 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:16:10 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.026 |  |
| 2026-05-29 14:11:29 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.026 |  |
| 2026-05-29 14:10:32 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-29 14:10:01 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | -0.018 |  |
| 2026-05-29 14:09:10 | Rathnapura (Kalu Ganga) | 4.36 | 🟢 Normal | -0.120 |  |
| 2026-05-29 14:06:34 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.031 |  |
| 2026-05-29 14:06:33 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.070 |  |
| 2026-05-29 14:06:14 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 14:06:10 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:06:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:06:03 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 14:04:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-29 14:04:33 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | -0.029 |  |
| 2026-05-29 14:41:07 | Baddegama (Gin Ganga) | 3.31 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-05-29 14:02:09 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-29 14:03:28 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 14:06:14 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 14:00:39 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 14:10:32 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-29 14:24:22 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-29 14:00:24 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:02:45 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:02:53 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:05:14 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:39:15 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:00:21 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:01:15 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:06:10 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:20:15 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:06:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:06:03 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 14:03:11 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-29 14:02:20 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-29 14:02:16 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-05-29 14:01:11 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-29 14:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-29 14:10:01 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | -0.018 |  |
| 2026-05-29 14:02:55 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-05-29 14:02:25 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-05-29 14:02:35 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-05-29 14:16:10 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.026 |  |
| 2026-05-29 14:11:29 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.026 |  |
| 2026-05-29 14:04:04 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-05-29 14:03:42 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.030 |  |
| 2026-05-29 14:06:34 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.031 |  |
| 2026-05-29 14:01:10 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.034 |  |
| 2026-05-29 14:02:22 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-05-29 14:06:33 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.070 |  |
| 2026-05-29 14:04:54 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.072 |  |
| 2026-05-29 14:09:10 | Rathnapura (Kalu Ganga) | 4.36 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)