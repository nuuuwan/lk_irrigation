# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_19:15:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,605 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 19:15:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:12:49 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:10:28 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-24 19:10:05 | Rathnapura (Kalu Ganga) | 4.44 | 🟢 Normal | 0.506 | 🔺 Rising |
| 2026-05-24 19:08:35 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-05-24 19:07:12 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-24 19:06:52 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:06:48 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-05-24 19:06:30 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:05:26 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-05-24 19:05:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:05:11 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:04:53 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:03:55 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | -0.040 |  |
| 2026-05-24 19:03:50 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:03:38 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-05-24 19:03:36 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-24 19:03:27 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:03:26 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-24 19:02:59 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-24 19:02:40 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 19:02:34 | Deraniyagala (Kelani Ganga) | 3.97 | 🟢 Normal | 1.244 | 🔺 Rising |
| 2026-05-24 19:02:29 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-24 19:02:28 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.080 |  |
| 2026-05-24 19:02:26 | Ellagawa (Kalu Ganga) | 9.59 | 🟢 Normal | -0.063 |  |
| 2026-05-24 19:02:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-24 19:02:09 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:02:00 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-05-24 19:01:55 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-05-24 19:01:46 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.013 |  |
| 2026-05-24 19:01:37 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | -0.022 |  |
| 2026-05-24 19:01:23 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.000 |  |
| 2026-05-24 19:01:04 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | -0.016 |  |
| 2026-05-24 19:00:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:00:46 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 19:01:23 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.000 |  |
| 2026-05-24 19:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | -0.022 |  |
| 2026-05-24 19:02:34 | Deraniyagala (Kelani Ganga) | 3.97 | 🟢 Normal | 1.244 | 🔺 Rising |
| 2026-05-24 19:10:05 | Rathnapura (Kalu Ganga) | 4.44 | 🟢 Normal | 0.506 | 🔺 Rising |
| 2026-05-24 19:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-05-24 19:07:12 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-24 19:03:36 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-24 19:10:28 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-24 19:02:40 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 19:02:29 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:00:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:01:37 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:04:53 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:06:30 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:12:49 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:15:33 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:03:50 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:05:11 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:06:52 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:05:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:03:27 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:02:09 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:08:35 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-05-24 19:06:48 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-05-24 19:03:26 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-24 19:02:59 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-24 19:00:46 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-24 19:02:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-24 19:05:26 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-05-24 19:01:46 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.013 |  |
| 2026-05-24 19:01:04 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | -0.016 |  |
| 2026-05-24 19:03:38 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-05-24 19:02:00 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-05-24 19:03:55 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | -0.040 |  |
| 2026-05-24 19:02:26 | Ellagawa (Kalu Ganga) | 9.59 | 🟢 Normal | -0.063 |  |
| 2026-05-24 19:02:28 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)