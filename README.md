# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_07:10:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 07:10:45 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | 0.742 | 🔺 Rising |
| 2026-08-01 07:10:11 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:10:06 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:09:26 | Glencourse (Kelani Ganga) | 13.04 | 🟢 Normal | 1.245 | 🔺 Rising |
| 2026-08-01 07:07:08 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:07:00 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-08-01 07:06:50 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:06:35 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:06:00 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2026-08-01 07:05:34 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-08-01 07:05:26 | Peradeniya (Mahaweli Ganga) | 4.72 | 🟢 Normal | 0.564 | 🔺 Rising |
| 2026-08-01 07:05:22 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-01 07:05:13 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-01 07:05:02 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 07:04:26 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-08-01 07:03:55 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:03:46 | Nawalapitiya (Mahaweli Ganga) | 4.69 | 🟡 Alert | -0.562 |  |
| 2026-08-01 07:03:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.100 |  |
| 2026-08-01 07:03:10 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-08-01 07:03:08 | Deraniyagala (Kelani Ganga) | 5.22 | 🟡 Alert | -0.532 |  |
| 2026-08-01 07:03:03 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-08-01 07:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-08-01 07:02:27 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 07:02:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:02:15 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-08-01 07:02:13 | Holombuwa (Kelani Ganga) | 3.89 | 🟠 Minor Flood | -0.143 |  |
| 2026-08-01 07:01:51 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:01:43 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:01:27 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:01:15 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:01:13 | Kithulgala (Kelani Ganga) | 3.53 | 🟡 Alert | -0.783 |  |
| 2026-08-01 07:01:11 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-01 07:00:46 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-01 07:00:40 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:54:02 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-08-01 06:35:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:31:18 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 07:02:13 | Holombuwa (Kelani Ganga) | 3.89 | 🟠 Minor Flood | -0.143 |  |
| 2026-08-01 07:03:08 | Deraniyagala (Kelani Ganga) | 5.22 | 🟡 Alert | -0.532 |  |
| 2026-08-01 07:03:46 | Nawalapitiya (Mahaweli Ganga) | 4.69 | 🟡 Alert | -0.562 |  |
| 2026-08-01 07:01:13 | Kithulgala (Kelani Ganga) | 3.53 | 🟡 Alert | -0.783 |  |
| 2026-08-01 07:09:26 | Glencourse (Kelani Ganga) | 13.04 | 🟢 Normal | 1.245 | 🔺 Rising |
| 2026-08-01 07:10:45 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | 0.742 | 🔺 Rising |
| 2026-08-01 07:05:26 | Peradeniya (Mahaweli Ganga) | 4.72 | 🟢 Normal | 0.564 | 🔺 Rising |
| 2026-08-01 07:06:00 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2026-08-01 07:04:26 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-08-01 07:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-08-01 07:03:03 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-08-01 07:03:10 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-08-01 06:05:46 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-01 07:01:11 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-01 06:03:01 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-01 07:02:27 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 07:05:02 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 07:02:15 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-08-01 07:03:55 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:02:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:00:40 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:01:51 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:01:27 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:06:35 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:10:11 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:07:02 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:04:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:06:50 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:01:15 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:10:06 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:07:08 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:01:43 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:05:22 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-01 07:05:13 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-01 07:00:46 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-01 07:05:34 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-08-01 07:07:00 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-08-01 06:02:15 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.033 |  |
| 2026-08-01 07:03:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)