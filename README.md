# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_04:25:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,602 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 04:25:11 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | -0.014 |  |
| 2026-05-28 04:17:53 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:15:34 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-05-28 04:12:51 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | -0.119 |  |
| 2026-05-28 04:11:50 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.026 |  |
| 2026-05-28 04:11:49 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | -0.040 |  |
| 2026-05-28 04:10:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.067 |  |
| 2026-05-28 04:08:59 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 04:08:39 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-28 04:08:27 | Rathnapura (Kalu Ganga) | 4.67 | 🟢 Normal | -0.096 |  |
| 2026-05-28 04:06:55 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:06:31 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:06:29 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-28 04:05:19 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-28 04:04:31 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-28 04:04:13 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 04:03:53 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.098 |  |
| 2026-05-28 04:03:51 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:03:26 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 04:03:21 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-28 04:03:15 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 04:03:14 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.058 |  |
| 2026-05-28 04:02:53 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -8.195 |  |
| 2026-05-28 04:02:50 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.038 |  |
| 2026-05-28 04:02:47 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:02:39 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.057 |  |
| 2026-05-28 04:02:19 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.062 |  |
| 2026-05-28 04:02:07 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-05-28 04:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:01:25 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:01:23 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-05-28 04:01:12 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:00:27 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 03:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.57 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-05-28 04:11:49 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | -0.040 |  |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-28 04:08:39 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-28 04:05:19 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-28 04:04:13 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 04:03:26 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 04:08:59 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 04:03:15 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 04:06:31 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:01:12 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:02:39 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:06:55 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:01:25 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:03:51 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:17:53 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:02:47 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:00:27 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:07:24 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:15:34 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-05-27 18:05:39 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-28 04:06:29 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-28 04:04:31 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-28 04:03:21 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-28 04:02:07 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-05-28 04:01:23 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-05-28 04:25:11 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | -0.014 |  |
| 2026-05-28 04:11:50 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.026 |  |
| 2026-05-28 04:02:50 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.038 |  |
| 2026-05-28 04:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.057 |  |
| 2026-05-28 04:03:14 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.058 |  |
| 2026-05-28 04:02:19 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.062 |  |
| 2026-05-28 04:10:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.067 |  |
| 2026-05-28 04:08:27 | Rathnapura (Kalu Ganga) | 4.67 | 🟢 Normal | -0.096 |  |
| 2026-05-28 04:03:53 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.098 |  |
| 2026-05-28 04:12:51 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | -0.119 |  |
| 2026-05-28 04:02:53 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -8.195 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)