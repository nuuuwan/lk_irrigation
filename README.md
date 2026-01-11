# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_07:38:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,472 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 07:38:09 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:16:20 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-11 07:14:09 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.016 |  |
| 2026-01-11 07:13:30 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:12:19 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.039 |  |
| 2026-01-11 07:11:34 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:11:30 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-11 07:09:42 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:09:38 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:08:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.146 |  |
| 2026-01-11 07:07:45 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:07:43 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-11 07:06:31 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:06:17 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:06:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.196 |  |
| 2026-01-11 07:05:54 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:05:35 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 07:05:32 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-01-11 07:04:49 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.028 |  |
| 2026-01-11 07:04:42 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:04:41 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:04:12 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 07:03:59 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.012 |  |
| 2026-01-11 07:03:32 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.011 |  |
| 2026-01-11 07:03:27 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.068 |  |
| 2026-01-11 07:03:18 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-01-11 07:03:02 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-11 07:02:58 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:02:42 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 07:02:14 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:01:56 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:01:40 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:01:31 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-11 07:01:24 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-11 07:01:14 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-01-11 07:01:03 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-11 07:00:47 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:00:37 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:00:36 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-01-11 07:00:07 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 07:01:03 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-11 07:07:43 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-11 07:03:02 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-11 07:02:42 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 07:05:35 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 07:04:12 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 07:16:20 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-11 07:02:14 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:01:56 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:00:37 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:09:42 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:04:41 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:06:31 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-11 06:35:58 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:38:09 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:02:58 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:13:30 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:06:17 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:00:47 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:04:42 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:11:34 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:00:07 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:09:38 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:05:54 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 07:03:18 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-01-11 07:11:30 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-11 07:01:24 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-11 07:01:31 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-11 07:00:36 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-01-11 07:03:32 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.011 |  |
| 2026-01-11 07:03:59 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.012 |  |
| 2026-01-11 07:14:09 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.016 |  |
| 2026-01-11 07:01:14 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-01-11 07:04:49 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.028 |  |
| 2026-01-11 07:12:19 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.039 |  |
| 2026-01-11 07:05:32 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-01-11 07:03:27 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.068 |  |
| 2026-01-11 07:08:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.146 |  |
| 2026-01-11 07:06:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)