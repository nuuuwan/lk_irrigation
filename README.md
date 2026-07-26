# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_14:18:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **216,800 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 14:18:53 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:15:54 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:13:49 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:11:53 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 14:11:42 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:11:39 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:10:41 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.097 |  |
| 2026-07-26 14:10:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-07-26 14:10:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-26 14:08:51 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-26 14:08:23 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:07:43 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:07:38 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:07:06 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:06:10 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:05:34 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:05:19 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-26 14:04:57 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.010 |  |
| 2026-07-26 14:04:22 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:03:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-07-26 14:03:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-07-26 14:03:10 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:03:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:02:55 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:02:30 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-07-26 14:02:28 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:02:27 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-07-26 14:02:21 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 14:02:17 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:02:08 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-26 14:01:40 | Yaka Wewa (Ma Oya) | 6.65 | 🔴 Major Flood | 6.223 | 🔺 Rising |
| 2026-07-26 14:01:40 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:33 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:13 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:07 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 14:01:07 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:06 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:00:33 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 14:01:40 | Yaka Wewa (Ma Oya) | 6.65 | 🔴 Major Flood | 6.223 | 🔺 Rising |
| 2026-07-26 14:02:27 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-07-26 14:08:51 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-26 14:05:19 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-26 14:02:21 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 14:01:07 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 14:11:53 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 14:10:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-26 14:02:55 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:33 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:13 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:40 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:13:49 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:06 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:05:34 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:03:10 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:02:28 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:07:43 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:11:42 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:03:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:06:10 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:15:54 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:02:17 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:04:22 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:02:08 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:00:33 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:08:23 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:01:07 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:07:38 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:11:39 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:18:53 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 14:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-26 14:02:30 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-07-26 14:04:57 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.010 |  |
| 2026-07-26 14:03:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-07-26 14:10:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-07-26 14:03:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-07-26 14:10:41 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)