# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_15:12:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,600 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 15:12:42 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:11:38 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:10:09 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:10:03 | Magura (Kalu Ganga) | 4.50 | 🟡 Alert | -0.035 |  |
| 2026-05-15 15:09:57 | Glencourse (Kelani Ganga) | 12.07 | 🟢 Normal | -0.144 |  |
| 2026-05-15 15:08:16 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.043 |  |
| 2026-05-15 15:07:11 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-05-15 15:06:49 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:06:26 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.030 |  |
| 2026-05-15 15:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 15:05:18 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:05:03 | Badalgama (Maha Oya) | 4.24 | 🟢 Normal | -0.073 |  |
| 2026-05-15 15:04:37 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-15 15:04:34 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:04:30 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 15:04:04 | Galgamuwa (Mee Oya) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:04:04 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.033 |  |
| 2026-05-15 15:03:35 | Moragaswewa (Deduru Oya) | 3.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-15 15:03:30 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 15:03:00 | Hanwella (Kelani Ganga) | 5.49 | 🟢 Normal | -0.132 |  |
| 2026-05-15 15:02:56 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-05-15 15:02:52 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:02:50 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 15:02:38 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 15:02:33 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:02:23 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.053 |  |
| 2026-05-15 15:02:17 | Ellagawa (Kalu Ganga) | 8.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 15:02:13 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-05-15 15:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-15 15:02:04 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | -0.091 |  |
| 2026-05-15 15:01:56 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-15 15:01:53 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-15 15:01:48 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.131 |  |
| 2026-05-15 15:01:44 | Giriulla (Maha Oya) | 3.09 | 🟢 Normal | -0.065 |  |
| 2026-05-15 15:01:28 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 15:01:12 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.055 |  |
| 2026-05-15 15:01:09 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:00:59 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:00:29 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:00:15 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 15:04:30 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 15:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 15:10:03 | Magura (Kalu Ganga) | 4.50 | 🟡 Alert | -0.035 |  |
| 2026-05-15 15:01:53 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-15 15:03:35 | Moragaswewa (Deduru Oya) | 3.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-15 15:02:38 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 15:04:37 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-15 15:02:17 | Ellagawa (Kalu Ganga) | 8.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 15:03:30 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 15:01:28 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 15:02:50 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 15:00:15 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:02:33 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:12:42 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:00:59 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:04:04 | Galgamuwa (Mee Oya) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:05:18 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:06:49 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:11:38 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:02:52 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:10:09 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:01:09 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:04:34 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-15 15:01:56 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-15 15:07:11 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-05-15 15:02:13 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-05-15 15:02:56 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-05-15 15:06:26 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.030 |  |
| 2026-05-15 15:04:04 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.033 |  |
| 2026-05-15 15:08:16 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.043 |  |
| 2026-05-15 15:02:23 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.053 |  |
| 2026-05-15 15:01:12 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.055 |  |
| 2026-05-15 15:01:44 | Giriulla (Maha Oya) | 3.09 | 🟢 Normal | -0.065 |  |
| 2026-05-15 15:05:03 | Badalgama (Maha Oya) | 4.24 | 🟢 Normal | -0.073 |  |
| 2026-05-15 15:02:04 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | -0.091 |  |
| 2026-05-15 15:01:48 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.131 |  |
| 2026-05-15 15:03:00 | Hanwella (Kelani Ganga) | 5.49 | 🟢 Normal | -0.132 |  |
| 2026-05-15 15:09:57 | Glencourse (Kelani Ganga) | 12.07 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)