# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_17:13:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 17:13:33 | Kuda Oya (Kirindi Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:13:21 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-23 17:12:14 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-23 17:09:41 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.774 | 🔺 Rising |
| 2026-04-23 17:08:10 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.047 |  |
| 2026-04-23 17:08:06 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:07:49 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:07:03 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:07:03 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-23 17:06:55 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:06:51 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:06:16 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.042 |  |
| 2026-04-23 17:05:36 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-23 17:05:35 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-23 17:05:01 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-23 17:04:41 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-23 17:04:40 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:04:22 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:04:11 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:04:06 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:04:01 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-04-23 17:03:47 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-23 17:03:35 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.021 |  |
| 2026-04-23 17:03:33 | Norwood (Kelani Ganga) | 1.82 | 🟡 Alert | 0.527 | 🔺 Rising |
| 2026-04-23 17:03:28 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:03:28 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:03:24 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:03:23 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:03:09 | Kuda Oya (Kirindi Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:03:07 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-23 17:02:49 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.022 |  |
| 2026-04-23 17:02:14 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 17:01:45 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:01:41 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:01:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-23 17:01:14 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:01:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:00:30 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 17:03:33 | Norwood (Kelani Ganga) | 1.82 | 🟡 Alert | 0.527 | 🔺 Rising |
| 2026-04-23 17:09:41 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.774 | 🔺 Rising |
| 2026-04-23 17:04:01 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-04-23 17:05:35 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-23 17:03:07 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-23 17:03:47 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-23 17:05:01 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-23 17:13:21 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-23 17:01:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-23 17:12:14 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-23 17:00:30 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-23 17:05:36 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-23 17:07:03 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-23 17:04:41 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-23 17:02:14 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 17:01:14 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:01:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:07:03 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:03:28 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:07:49 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:04:11 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:06:55 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:04:22 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:04:06 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:13:33 | Kuda Oya (Kirindi Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:04:40 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-23 17:03:28 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:08:06 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:03:23 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:02:49 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:06:51 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:01:45 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:01:41 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:03:24 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-23 17:03:35 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.021 |  |
| 2026-04-23 17:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.022 |  |
| 2026-04-23 17:06:16 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.042 |  |
| 2026-04-23 17:08:10 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.047 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)