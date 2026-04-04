# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_20:17:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,223 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 20:17:52 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:14:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-04-04 20:13:51 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.407 |  |
| 2026-04-04 20:11:07 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-04-04 20:09:29 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-04-04 20:08:47 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:08:17 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-04-04 20:07:45 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 20:07:39 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:07:31 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-04 20:07:16 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:05:57 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -0.038 |  |
| 2026-04-04 20:05:20 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-04-04 20:04:58 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-04 20:04:17 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-04 20:04:15 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-04 20:04:12 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 20:04:09 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.090 |  |
| 2026-04-04 20:03:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:03:12 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:03:05 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-04-04 20:03:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 20:02:43 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-04-04 20:02:19 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.052 |  |
| 2026-04-04 20:02:18 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:02:07 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 20:02:04 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:01:54 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-04 20:01:54 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 20:01:40 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-04-04 20:01:23 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:01:16 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-04-04 20:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:00:48 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 20:00:33 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 20:00:10 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 20:01:40 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-04-04 20:01:16 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-04-04 20:04:58 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-04 20:01:54 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-04 20:07:31 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-04 20:01:54 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 20:00:33 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 20:07:45 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 20:00:48 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 20:02:07 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 20:03:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 20:04:12 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 20:00:10 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:02:18 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:03:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:01:23 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:17:52 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:08:47 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:07:39 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:03:12 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:07:16 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:02:04 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:09:29 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-04-04 20:08:17 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-04-04 20:04:15 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-04 20:04:17 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-04 20:05:20 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-04-04 20:14:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-04-04 20:11:07 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-04-04 20:02:43 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-04-04 20:03:05 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-04 20:05:57 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -0.038 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-04 20:02:19 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.052 |  |
| 2026-04-04 20:04:09 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.090 |  |
| 2026-04-04 20:13:51 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.407 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)