# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_17:15:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,588 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 17:15:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:14:50 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | -0.017 |  |
| 2026-05-16 17:09:33 | Moragaswewa (Deduru Oya) | 2.95 | 🟢 Normal | -0.026 |  |
| 2026-05-16 17:08:20 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:08:17 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | -0.020 |  |
| 2026-05-16 17:08:14 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:07:22 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.052 |  |
| 2026-05-16 17:06:23 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.028 |  |
| 2026-05-16 17:05:55 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-16 17:05:26 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-16 17:04:45 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 17:04:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:04:39 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-16 17:04:02 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-16 17:04:00 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 17:03:49 | Hanwella (Kelani Ganga) | 3.47 | 🟢 Normal | -0.031 |  |
| 2026-05-16 17:03:44 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:35 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:32 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-16 17:03:23 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-05-16 17:03:15 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-16 17:03:11 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:08 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-16 17:03:01 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-16 17:02:58 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:02:51 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-16 17:02:44 | Thanthirimale (Malwathu Oya) | 3.83 | 🟢 Normal | -0.054 |  |
| 2026-05-16 17:02:35 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:02:33 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 17:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:02:25 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-05-16 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.96 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 17:01:53 | Galgamuwa (Mee Oya) | 2.95 | 🟢 Normal | -0.103 |  |
| 2026-05-16 17:01:18 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:01:10 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | -0.042 |  |
| 2026-05-16 17:01:10 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.109 |  |
| 2026-05-16 17:01:08 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.030 |  |
| 2026-05-16 17:01:07 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.96 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 17:01:10 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.109 |  |
| 2026-05-16 17:02:51 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-16 17:05:55 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-16 17:04:39 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-16 17:03:32 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-16 17:03:01 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-16 17:03:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-16 17:04:02 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-16 17:05:26 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-16 17:02:33 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 17:04:00 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 17:04:45 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 17:01:18 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:44 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:35 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:11 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:01:07 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:02:35 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:08 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:04:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:08:20 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:02:58 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:15:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:08:14 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:14:50 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | -0.017 |  |
| 2026-05-16 17:02:25 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-05-16 17:03:15 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-16 17:08:17 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | -0.020 |  |
| 2026-05-16 17:09:33 | Moragaswewa (Deduru Oya) | 2.95 | 🟢 Normal | -0.026 |  |
| 2026-05-16 17:06:23 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.028 |  |
| 2026-05-16 17:01:08 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.030 |  |
| 2026-05-16 17:03:23 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-05-16 17:03:49 | Hanwella (Kelani Ganga) | 3.47 | 🟢 Normal | -0.031 |  |
| 2026-05-16 17:01:10 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | -0.042 |  |
| 2026-05-16 17:07:22 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.052 |  |
| 2026-05-16 17:02:44 | Thanthirimale (Malwathu Oya) | 3.83 | 🟢 Normal | -0.054 |  |
| 2026-05-16 17:01:53 | Galgamuwa (Mee Oya) | 2.95 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)