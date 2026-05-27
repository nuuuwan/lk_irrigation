# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_16:13:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,168 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 16:13:44 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.033 |  |
| 2026-05-27 16:12:20 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-27 16:07:56 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 16:07:31 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-27 16:06:53 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-27 16:06:51 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-05-27 16:06:15 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:06:12 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-27 16:06:09 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-05-27 16:05:58 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:05:50 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:05:41 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:05:05 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 16:04:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.082 |  |
| 2026-05-27 16:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-27 16:04:12 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.043 |  |
| 2026-05-27 16:04:09 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-27 16:04:04 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:04:02 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-27 16:03:58 | Deraniyagala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-05-27 16:03:27 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:03:06 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-27 16:02:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-27 16:02:38 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-27 16:02:21 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 16:02:15 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:02:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:02:09 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:01:51 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.021 |  |
| 2026-05-27 16:01:46 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 16:01:36 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:01:20 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:00:57 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:00:48 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:00:47 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 15:59:51 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 16:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-27 16:06:51 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-05-27 16:03:58 | Deraniyagala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-05-27 16:06:12 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-27 16:04:09 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-27 16:12:20 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-27 16:07:31 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-27 16:06:53 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-27 16:03:06 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-27 16:04:02 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-27 16:02:21 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 16:07:56 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 16:01:46 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 16:05:05 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 16:00:48 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 15:25:52 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:01:36 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:05:58 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:02:09 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:00:57 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:06:15 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:03:27 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:01:20 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:02:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:04:04 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:05:50 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:05:41 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:00:47 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:02:15 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 16:02:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-27 16:02:38 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-27 16:06:09 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-05-27 15:59:51 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.021 |  |
| 2026-05-27 16:01:51 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.021 |  |
| 2026-05-27 16:13:44 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.033 |  |
| 2026-05-27 16:04:12 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.043 |  |
| 2026-05-27 16:04:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.082 |  |
| 2026-05-27 15:01:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.434 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)