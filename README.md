# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_00:11:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,684 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 00:11:44 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | -0.019 |  |
| 2026-05-26 00:08:43 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-26 00:08:21 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-05-26 00:07:40 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:06:35 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:06:12 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:05:55 | Rathnapura (Kalu Ganga) | 4.18 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-26 00:05:53 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-26 00:05:53 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:05:52 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:05:47 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.029 |  |
| 2026-05-26 00:05:31 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:05:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 00:05:10 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-26 00:04:19 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:03:50 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:03:32 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:03:31 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:03:30 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-26 00:02:53 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 00:02:49 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.033 |  |
| 2026-05-26 00:02:37 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:02:30 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:02:16 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.022 |  |
| 2026-05-26 00:02:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:02:08 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:02:07 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:54 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.044 |  |
| 2026-05-26 00:01:46 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-05-26 00:01:32 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:30 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:21 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:15 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:13 | Dunamale (Aththanagalu Oya) | 2.39 | 🟢 Normal | 0.066 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 20:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.061 |  |
| 2026-05-26 00:05:55 | Rathnapura (Kalu Ganga) | 4.18 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-26 00:01:13 | Dunamale (Aththanagalu Oya) | 2.39 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-26 00:03:30 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-26 00:05:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 00:02:53 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 00:08:43 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-26 00:07:40 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:05:52 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:30 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:15 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:06:12 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:02:08 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:05:53 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:05:31 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:06:35 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:21 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:04:19 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:03:50 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:02:07 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:02:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:03:32 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:02:37 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:03:31 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:32 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:02:30 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:05:53 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-26 00:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-26 00:01:46 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-26 00:11:44 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | -0.019 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-26 00:02:16 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.022 |  |
| 2026-05-26 00:05:47 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.029 |  |
| 2026-05-26 00:02:49 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.033 |  |
| 2026-05-26 00:08:21 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-05-26 00:01:54 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.044 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)