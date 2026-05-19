# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_13:26:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,099 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 13:26:01 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.015 |  |
| 2026-05-19 13:20:06 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:14:10 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:08:11 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-05-19 13:07:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.066 |  |
| 2026-05-19 13:07:31 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.009 |  |
| 2026-05-19 13:06:44 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-05-19 13:06:16 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:05:52 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:05:31 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:04:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-19 13:04:37 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-05-19 13:04:26 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:04:24 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 13:03:55 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:03:55 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-05-19 13:03:49 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:03:40 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:03:29 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:03:15 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:03:14 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-19 13:02:22 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:02:19 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:02:08 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:02:04 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:02:02 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:01:55 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:01:55 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:01:40 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 13:01:36 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 13:01:36 | Thanthirimale (Malwathu Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-19 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 13:01:19 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:01:19 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:01:11 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-05-19 13:01:09 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-05-19 13:00:59 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.022 |  |
| 2026-05-19 13:00:32 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:00:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 13:04:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-19 13:03:14 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-19 13:04:24 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 13:01:40 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 13:01:36 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 13:00:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 13:01:55 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:02:22 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:02:04 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:00:32 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:01:19 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:03:15 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:14:10 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:02:19 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:05:31 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:03:55 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:03:49 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:20:06 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-19 13:07:31 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.009 |  |
| 2026-05-19 13:04:37 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-05-19 13:05:52 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:01:55 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:01:19 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:03:29 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:03:40 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-19 11:00:40 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:06:16 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:04:26 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:02:08 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-05-19 13:01:11 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-05-19 13:26:01 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.015 |  |
| 2026-05-19 13:08:11 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-05-19 13:03:55 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-05-19 13:01:36 | Thanthirimale (Malwathu Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-19 13:00:59 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.022 |  |
| 2026-05-19 13:06:44 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-05-19 13:01:09 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-05-19 13:07:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)