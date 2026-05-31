# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_06:25:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,350 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 06:25:01 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:13:21 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.035 |  |
| 2026-05-31 06:10:48 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:09:07 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:09:00 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.044 |  |
| 2026-05-31 06:08:53 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.044 |  |
| 2026-05-31 06:08:41 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -4.235 |  |
| 2026-05-31 06:08:24 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | -4.235 |  |
| 2026-05-31 06:07:20 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | -0.031 |  |
| 2026-05-31 06:06:27 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.112 |  |
| 2026-05-31 06:06:23 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:05:59 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.151 |  |
| 2026-05-31 06:05:37 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-05-31 06:05:14 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:05:08 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:04:58 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.019 |  |
| 2026-05-31 06:04:50 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:04:16 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:04:13 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:04:05 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:03:57 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:03:16 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -21.600 |  |
| 2026-05-31 06:03:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:03:11 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -21.600 |  |
| 2026-05-31 06:03:05 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-05-31 06:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | -0.137 |  |
| 2026-05-31 06:02:59 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-05-31 06:02:56 | Putupaula (Kalu Ganga) | 2.09 | 🟢 Normal | -0.055 |  |
| 2026-05-31 06:02:50 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:02:45 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:02:11 | Hanwella (Kelani Ganga) | 2.41 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-31 06:02:00 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-05-31 06:01:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:01:41 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:01:39 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:01:38 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:01:23 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.050 |  |
| 2026-05-31 06:00:59 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-31 06:00:31 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:00:28 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 06:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | -0.137 |  |
| 2026-05-31 06:02:11 | Hanwella (Kelani Ganga) | 2.41 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-31 06:00:59 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-31 06:00:28 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-31 06:05:08 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:00:31 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:01:23 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:02:45 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:01:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:02:50 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:04:05 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:25:01 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:01:41 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:04:50 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:03:57 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:10:48 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:03:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:04:13 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:04:51 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:09:07 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:05:14 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:04:16 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:06:23 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:05:37 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-05-31 06:02:00 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-05-31 06:03:05 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-05-31 06:04:58 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.019 |  |
| 2026-05-31 06:07:20 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | -0.031 |  |
| 2026-05-31 06:02:59 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-05-31 06:13:21 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.035 |  |
| 2026-05-31 06:09:00 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.044 |  |
| 2026-05-31 06:08:53 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.044 |  |
| 2026-05-31 06:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.050 |  |
| 2026-05-31 06:02:56 | Putupaula (Kalu Ganga) | 2.09 | 🟢 Normal | -0.055 |  |
| 2026-05-31 06:06:27 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.112 |  |
| 2026-05-31 06:05:59 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.151 |  |
| 2026-05-31 06:08:41 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -4.235 |  |
| 2026-05-31 06:03:16 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -21.600 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)