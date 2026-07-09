# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_07:10:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **201,306 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 07:10:06 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:09:28 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-07-09 07:08:54 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:08:18 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-07-09 07:08:09 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.110 |  |
| 2026-07-09 07:07:55 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-09 07:07:37 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:07:36 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-07-09 07:07:36 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-07-09 07:06:42 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.009 |  |
| 2026-07-09 07:06:16 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-09 07:06:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-09 07:06:05 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.072 |  |
| 2026-07-09 07:05:52 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.038 |  |
| 2026-07-09 07:05:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 07:05:05 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-07-09 07:04:07 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-09 07:04:04 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:03:48 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:03:43 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:03:35 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 07:03:33 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-07-09 07:03:21 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:03:13 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:02:54 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-07-09 07:02:50 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:02:23 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.096 |  |
| 2026-07-09 07:02:18 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-09 07:01:55 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-07-09 07:01:43 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:01:35 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:01:16 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.071 |  |
| 2026-07-09 07:01:15 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:01:00 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.004 |  |
| 2026-07-09 06:33:06 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 07:06:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-09 07:02:18 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-09 07:04:07 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-09 07:06:16 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-09 07:07:55 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-09 07:05:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 07:03:35 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 07:01:00 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.004 |  |
| 2026-07-09 07:03:43 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:01:35 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:07:37 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:03:21 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:01:15 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:03:13 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-09 06:00:59 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:02:23 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-09 06:05:59 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:10:06 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:04:04 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:03:48 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:08:54 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:02:50 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 06:04:18 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:01:43 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:09:28 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-07-09 07:08:18 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-07-09 07:06:42 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.009 |  |
| 2026-07-09 07:05:05 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-07-09 07:07:36 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-07-09 07:03:33 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-07-09 07:07:36 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-07-09 06:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-07-09 07:01:55 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-07-09 07:02:54 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-07-09 07:05:52 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.038 |  |
| 2026-07-09 07:01:16 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.071 |  |
| 2026-07-09 07:06:05 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.072 |  |
| 2026-07-09 07:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.096 |  |
| 2026-07-09 07:08:09 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)