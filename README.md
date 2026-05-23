# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_04:31:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,198 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 04:31:34 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:19:32 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | 0.000 |  |
| 2026-05-24 04:19:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:18:48 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:15:25 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 04:13:55 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:13:34 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:13:19 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:08:33 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-24 04:08:25 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:07:49 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-24 04:06:51 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.046 |  |
| 2026-05-24 04:06:32 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:06:02 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:05:29 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.009 |  |
| 2026-05-24 04:04:41 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:04:28 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-05-24 04:04:04 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.034 |  |
| 2026-05-24 04:03:43 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -0.092 |  |
| 2026-05-24 04:03:25 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | -0.080 |  |
| 2026-05-24 04:02:50 | Putupaula (Kalu Ganga) | 3.28 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-05-24 04:02:40 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-24 04:02:39 | Dunamale (Aththanagalu Oya) | 4.20 | 🟡 Alert | -0.099 |  |
| 2026-05-24 04:02:22 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-05-24 04:02:08 | Hanwella (Kelani Ganga) | 5.11 | 🟢 Normal | -0.093 |  |
| 2026-05-24 04:01:58 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.142 |  |
| 2026-05-24 04:01:45 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.041 |  |
| 2026-05-24 04:01:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:01:41 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:01:37 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:01:26 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:00:26 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 02:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-24 04:02:50 | Putupaula (Kalu Ganga) | 3.28 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-05-24 04:19:32 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | 0.000 |  |
| 2026-05-24 04:02:39 | Dunamale (Aththanagalu Oya) | 4.20 | 🟡 Alert | -0.099 |  |
| 2026-05-24 03:06:23 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 5.976 | 🔺 Rising |
| 2026-05-24 04:07:49 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-24 04:08:33 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 04:15:25 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 04:01:26 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:19:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:06:32 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:18:48 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:01:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:02:22 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:06:02 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:13:34 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:00:26 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:08:25 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:01:37 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:13:55 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:01:41 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:04:41 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:22:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:31:34 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:05:29 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.009 |  |
| 2026-05-24 04:02:40 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-24 04:04:28 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-24 04:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-05-24 04:04:04 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.034 |  |
| 2026-05-24 04:01:45 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.041 |  |
| 2026-05-24 04:06:51 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.046 |  |
| 2026-05-24 04:03:25 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | -0.080 |  |
| 2026-05-24 04:03:43 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -0.092 |  |
| 2026-05-24 04:02:08 | Hanwella (Kelani Ganga) | 5.11 | 🟢 Normal | -0.093 |  |
| 2026-05-24 04:01:58 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)