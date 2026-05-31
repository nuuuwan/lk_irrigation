# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_15:13:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,712 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 15:13:07 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:11:05 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:09:59 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:09:54 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.009 |  |
| 2026-05-31 15:09:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.65 | 🟢 Normal | -0.125 |  |
| 2026-05-31 15:08:38 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:08:38 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-31 15:08:03 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-31 15:07:02 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.028 |  |
| 2026-05-31 15:06:13 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:05:41 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:05:13 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:04:37 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:04:29 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:04:18 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:03:47 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-05-31 15:03:42 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:03:38 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-31 15:03:26 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:03:23 | Ellagawa (Kalu Ganga) | 5.91 | 🟢 Normal | -0.031 |  |
| 2026-05-31 15:03:11 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.152 |  |
| 2026-05-31 15:03:02 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.107 |  |
| 2026-05-31 15:03:00 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:58 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:52 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:02:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:42 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:02:41 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:31 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:17 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:16 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:15 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:06 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-05-31 15:01:56 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:01:49 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:01:44 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-05-31 15:00:37 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:00:31 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 15:00:17 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:00:12 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-31 15:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:00:08 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 15:02:06 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-05-31 15:08:38 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-31 15:03:38 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-31 15:00:12 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-31 15:08:03 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-31 15:00:31 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 15:02:15 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:09:59 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:01:49 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:41 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:58 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:00:17 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:05:13 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:03:00 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:11:05 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:05:41 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:04:29 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:04:37 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:31 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:13:07 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:03:42 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:06:13 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:09:54 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.009 |  |
| 2026-05-31 15:02:42 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:04:18 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:00:37 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:02:52 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:03:26 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:01:44 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-05-31 15:03:47 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-05-31 15:00:08 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.028 |  |
| 2026-05-31 15:07:02 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.028 |  |
| 2026-05-31 15:03:23 | Ellagawa (Kalu Ganga) | 5.91 | 🟢 Normal | -0.031 |  |
| 2026-05-31 15:03:02 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.107 |  |
| 2026-05-31 15:09:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.65 | 🟢 Normal | -0.125 |  |
| 2026-05-31 15:03:11 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)