# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_09:14:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,654 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 09:14:30 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 09:08:46 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | -0.028 |  |
| 2026-06-08 09:08:34 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.031 |  |
| 2026-06-08 09:08:19 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-06-08 09:07:33 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-08 09:06:38 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-06-08 09:06:06 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.053 |  |
| 2026-06-08 09:05:34 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:05:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-08 09:05:06 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:05:04 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 09:05:00 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-08 09:04:56 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.051 |  |
| 2026-06-08 09:04:37 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:04:22 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 09:04:01 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 09:03:48 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-06-08 09:03:47 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-06-08 09:03:37 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | -0.041 |  |
| 2026-06-08 09:03:35 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-08 09:03:34 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.061 |  |
| 2026-06-08 09:03:33 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-08 09:03:26 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 09:03:11 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:03:08 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-08 09:03:03 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:02:56 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:02:39 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:02:24 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.05 | 🟡 Alert | -0.031 |  |
| 2026-06-08 09:02:14 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:01:52 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |
| 2026-06-08 09:01:40 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:01:17 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-08 09:01:12 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | -0.045 |  |
| 2026-06-08 09:01:07 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:01:03 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-06-08 09:00:23 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.015 |  |
| 2026-06-08 09:00:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.05 | 🟡 Alert | -0.031 |  |
| 2026-06-08 09:03:35 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-08 09:03:08 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-08 09:01:17 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-08 09:05:00 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-08 09:05:04 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 09:03:26 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 09:04:01 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 09:04:22 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 09:14:30 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 09:01:03 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:01:07 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:02:39 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:01:40 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:04:37 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:05:06 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:02:56 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:02:24 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:02:14 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:03:03 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:05:34 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:00:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:03:11 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 09:03:48 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-06-08 09:06:38 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-06-08 09:07:33 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-08 09:00:23 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.015 |  |
| 2026-06-08 09:03:47 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-06-08 09:05:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-08 09:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-06-08 09:08:46 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | -0.028 |  |
| 2026-06-08 09:08:19 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-06-08 09:08:34 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.031 |  |
| 2026-06-08 09:01:52 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |
| 2026-06-08 09:03:37 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | -0.041 |  |
| 2026-06-08 09:01:12 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | -0.045 |  |
| 2026-06-08 09:04:56 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.051 |  |
| 2026-06-08 09:06:06 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.053 |  |
| 2026-06-08 09:03:34 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)