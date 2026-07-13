# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_06:17:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,859 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 06:17:02 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:13:29 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.016 |  |
| 2026-07-13 06:09:57 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:09:43 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:09:24 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:08:31 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-07-13 06:08:30 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.016 |  |
| 2026-07-13 06:08:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:06:14 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-13 06:05:50 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.031 |  |
| 2026-07-13 06:05:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:05:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-13 06:05:02 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:04:59 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.143 |  |
| 2026-07-13 06:04:40 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:04:25 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-13 06:03:43 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.065 |  |
| 2026-07-13 06:03:24 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-13 06:03:21 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-13 06:03:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:03:14 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:03:14 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-07-13 06:02:51 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:02:51 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:02:37 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:02:32 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:02:29 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:02:19 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:02:01 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-13 06:01:51 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:01:42 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:01:35 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-13 06:01:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:01:31 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:00:44 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.155 |  |
| 2026-07-13 06:00:35 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 06:05:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-13 06:03:21 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-13 06:03:24 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-13 06:01:35 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-13 06:04:25 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-13 06:02:01 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-13 06:06:14 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-13 06:03:14 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:01:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:01:51 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:01:42 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:05:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:02:26 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:02:51 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:09:24 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:05:02 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:00:35 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:03:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:04:40 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:02:37 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:08:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:01:22 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:09:43 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:17:02 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:02:51 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:02:19 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 06:02:32 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:09:57 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:02:29 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:01:31 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-13 06:03:14 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-07-13 06:08:31 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-07-13 06:13:29 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.016 |  |
| 2026-07-13 06:08:30 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.016 |  |
| 2026-07-13 06:05:50 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.031 |  |
| 2026-07-13 06:03:43 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.065 |  |
| 2026-07-13 06:04:59 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.143 |  |
| 2026-07-13 06:00:44 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)