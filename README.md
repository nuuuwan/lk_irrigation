# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_06:15:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,808 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 06:15:56 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:15:48 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-01 06:14:40 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:10:08 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.588 | 🔺 Rising |
| 2026-08-01 06:08:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-08-01 06:07:39 | Holombuwa (Kelani Ganga) | 4.02 | 🟠 Minor Flood | 0.341 | 🔺 Rising |
| 2026-08-01 06:07:39 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | 0.634 | 🔺 Rising |
| 2026-08-01 06:07:16 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 1.104 | 🔺 Rising |
| 2026-08-01 06:07:08 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:07:02 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:06:44 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:05:59 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:05:54 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.063 |  |
| 2026-08-01 06:05:52 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 06:05:46 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-01 06:05:34 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-08-01 06:05:29 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-08-01 06:05:28 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.005 |  |
| 2026-08-01 06:04:41 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:04:22 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-01 06:04:19 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 06:03:57 | Nawalapitiya (Mahaweli Ganga) | 5.25 | 🟠 Minor Flood | -0.226 |  |
| 2026-08-01 06:03:26 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 06:03:22 | Deraniyagala (Kelani Ganga) | 5.75 | 🟡 Alert | 0.612 | 🔺 Rising |
| 2026-08-01 06:03:01 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-01 06:02:36 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-08-01 06:02:15 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.033 |  |
| 2026-08-01 06:02:14 | Kithulgala (Kelani Ganga) | 4.30 | 🟠 Minor Flood | 0.505 | 🔺 Rising |
| 2026-08-01 06:02:07 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:01:39 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.152 |  |
| 2026-08-01 06:01:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:01:17 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:00:40 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.164 |  |
| 2026-08-01 06:00:38 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 05:52:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-08-01 05:49:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.431 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 06:02:14 | Kithulgala (Kelani Ganga) | 4.30 | 🟠 Minor Flood | 0.505 | 🔺 Rising |
| 2026-08-01 06:07:39 | Holombuwa (Kelani Ganga) | 4.02 | 🟠 Minor Flood | 0.341 | 🔺 Rising |
| 2026-08-01 06:03:57 | Nawalapitiya (Mahaweli Ganga) | 5.25 | 🟠 Minor Flood | -0.226 |  |
| 2026-08-01 06:03:22 | Deraniyagala (Kelani Ganga) | 5.75 | 🟡 Alert | 0.612 | 🔺 Rising |
| 2026-08-01 06:07:16 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 1.104 | 🔺 Rising |
| 2026-08-01 06:07:39 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | 0.634 | 🔺 Rising |
| 2026-08-01 06:10:08 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.588 | 🔺 Rising |
| 2026-08-01 06:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-08-01 06:05:29 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-08-01 06:05:34 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-08-01 06:05:46 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-01 06:04:22 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-01 06:03:26 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 06:15:48 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-01 06:03:01 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-01 06:00:38 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 06:04:19 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 06:05:52 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 18:04:08 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:01:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:02:36 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:02:07 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:14:40 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:04:41 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:07:02 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:04:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:06:44 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:05:59 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:01:17 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:07:08 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:05 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:15:56 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 06:05:28 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.005 |  |
| 2026-08-01 06:02:15 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.033 |  |
| 2026-08-01 06:08:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-08-01 06:05:54 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.063 |  |
| 2026-08-01 06:01:39 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.152 |  |
| 2026-08-01 06:00:40 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)