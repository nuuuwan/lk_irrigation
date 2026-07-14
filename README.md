# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_11:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,932 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 11:13:45 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-07-14 11:10:37 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:09:04 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-07-14 11:08:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-07-14 11:08:27 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.018 |  |
| 2026-07-14 11:07:53 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.009 |  |
| 2026-07-14 11:07:48 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:07:38 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-07-14 11:07:12 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-07-14 11:06:42 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:06:32 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.009 |  |
| 2026-07-14 11:06:01 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:05:28 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:05:23 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-07-14 11:05:21 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:04:56 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:04:16 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:03:40 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:03:34 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-14 11:03:19 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.032 |  |
| 2026-07-14 11:03:15 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-14 11:03:13 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:03:00 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:02:28 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:02:20 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-14 11:02:11 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:01:52 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.041 |  |
| 2026-07-14 11:01:47 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:01:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:01:29 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:01:16 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:00:49 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:00:46 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:00:43 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:00:19 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:58:29 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:35:29 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 11:05:23 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-07-14 11:08:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-07-14 11:03:34 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-14 11:02:20 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-14 10:12:50 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-14 11:01:16 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:00:49 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:00:19 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:00:43 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:01:47 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:01:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:03:40 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:10:37 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:06:01 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:01:29 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:04:16 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:07:48 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:03:00 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:03:13 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:00:46 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:04:56 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:05:21 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:05:28 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:02:28 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:06:42 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:58:29 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:02:11 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 11:07:53 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.009 |  |
| 2026-07-14 11:06:32 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.009 |  |
| 2026-07-14 11:09:04 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-07-14 11:07:12 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-07-14 11:07:38 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-07-14 11:03:15 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-14 11:13:45 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-07-14 11:08:27 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.018 |  |
| 2026-07-14 10:24:14 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.022 |  |
| 2026-07-14 11:03:19 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.032 |  |
| 2026-07-14 11:01:52 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)