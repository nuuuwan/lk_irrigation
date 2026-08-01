# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_12:19:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,046 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 12:19:55 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:18:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:18:23 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.055 |  |
| 2026-08-01 12:12:38 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-01 12:08:19 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-01 12:08:15 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-08-01 12:06:07 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:06:05 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:05:49 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 12:05:42 | Ellagawa (Kalu Ganga) | 6.37 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-08-01 12:05:16 | Hanwella (Kelani Ganga) | 4.80 | 🟢 Normal | 0.449 | 🔺 Rising |
| 2026-08-01 12:05:09 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.442 |  |
| 2026-08-01 12:04:52 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-08-01 12:04:41 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.023 |  |
| 2026-08-01 12:04:38 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.049 |  |
| 2026-08-01 12:04:12 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.329 |  |
| 2026-08-01 12:03:49 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:03:42 | Glencourse (Kelani Ganga) | 14.95 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-01 12:03:25 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 12:03:14 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.158 |  |
| 2026-08-01 12:03:03 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.272 |  |
| 2026-08-01 12:02:46 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:02:43 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:02:39 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.298 |  |
| 2026-08-01 12:02:38 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:02:36 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 12:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 12:02:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:02:12 | Peradeniya (Mahaweli Ganga) | 5.65 | 🟡 Alert | -0.268 |  |
| 2026-08-01 12:01:56 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:01:43 | Giriulla (Maha Oya) | 3.28 | 🟢 Normal | 0.813 | 🔺 Rising |
| 2026-08-01 12:01:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-01 12:01:27 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-01 12:01:21 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:01:17 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 12:01:04 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-01 12:00:51 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:00:46 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:00:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 12:02:12 | Peradeniya (Mahaweli Ganga) | 5.65 | 🟡 Alert | -0.268 |  |
| 2026-08-01 12:01:43 | Giriulla (Maha Oya) | 3.28 | 🟢 Normal | 0.813 | 🔺 Rising |
| 2026-08-01 12:05:16 | Hanwella (Kelani Ganga) | 4.80 | 🟢 Normal | 0.449 | 🔺 Rising |
| 2026-08-01 12:05:42 | Ellagawa (Kalu Ganga) | 6.37 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-08-01 12:01:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-01 12:03:42 | Glencourse (Kelani Ganga) | 14.95 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-01 12:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 12:03:25 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 12:01:27 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-01 12:01:04 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-01 12:02:36 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 12:01:17 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 12:05:49 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 12:12:38 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-01 12:01:56 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:00:46 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:19:55 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:00:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:00:51 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:02:43 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:06:07 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:18:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:01:21 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:03:49 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:02:38 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:02:46 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:02:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:06:05 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 12:04:52 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-08-01 12:08:19 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-01 12:08:15 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-08-01 12:04:41 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.023 |  |
| 2026-08-01 12:04:38 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.049 |  |
| 2026-08-01 12:18:23 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.055 |  |
| 2026-08-01 12:03:14 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.158 |  |
| 2026-08-01 12:03:03 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.272 |  |
| 2026-08-01 12:02:39 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.298 |  |
| 2026-08-01 12:04:12 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.329 |  |
| 2026-08-01 12:05:09 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.442 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)