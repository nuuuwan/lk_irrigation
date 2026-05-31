# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_03:25:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 03:25:45 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:13:44 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.009 |  |
| 2026-06-01 03:13:22 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:09:40 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:09:08 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-01 03:08:44 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-06-01 03:07:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-01 03:06:57 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-01 03:06:17 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:05:47 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:05:46 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:05:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 03:04:58 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:04:53 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-06-01 03:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.077 |  |
| 2026-06-01 03:03:58 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:39 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-01 03:03:39 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-01 03:03:33 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-01 03:03:14 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:04 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-01 03:03:03 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.043 |  |
| 2026-06-01 03:03:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:02:28 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:02:21 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-06-01 03:02:01 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:01:35 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:01:33 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 03:01:23 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:01:01 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.828 |  |
| 2026-06-01 02:59:34 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.828 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 03:03:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-01 03:03:39 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-01 03:03:39 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-01 03:06:57 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-01 03:09:08 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-01 03:07:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-01 03:05:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 03:01:33 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:05:47 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:04 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:01:23 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 02:41:43 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:06:10 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:04:58 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:01:35 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:06:17 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:13:22 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:05:46 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:06:35 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:14 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:37:18 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:58 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:09:40 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:25:45 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:02:28 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:02:01 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:13:44 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.009 |  |
| 2026-06-01 03:08:44 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-06-01 02:00:48 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-06-01 03:03:33 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-01 03:04:53 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-06-01 03:02:21 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-06-01 03:03:03 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.043 |  |
| 2026-06-01 03:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.077 |  |
| 2026-06-01 03:01:01 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.828 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)