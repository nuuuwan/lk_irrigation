# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_22:17:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,538 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 22:17:47 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-20 22:09:49 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:07:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-20 22:07:16 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.144 |  |
| 2026-04-20 22:06:29 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 22:06:17 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-20 22:05:39 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:05:36 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-20 22:05:21 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 22:05:13 | Thanamalwila (Kirindi Oya) | 3.92 | 🟢 Normal | 2.968 | 🔺 Rising |
| 2026-04-20 22:04:59 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-20 22:04:52 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:04:43 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:04:26 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-20 22:04:26 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | 0.531 | 🔺 Rising |
| 2026-04-20 22:04:20 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-04-20 22:04:12 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-20 22:04:04 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:03:51 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 22:03:47 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-04-20 22:03:08 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.110 |  |
| 2026-04-20 22:03:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-04-20 22:02:54 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-20 22:02:47 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.080 |  |
| 2026-04-20 22:02:28 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-04-20 22:02:13 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.296 |  |
| 2026-04-20 22:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 22:02:03 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:01:32 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:01:31 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.459 | 🔺 Rising |
| 2026-04-20 22:01:30 | Kuda Oya (Kirindi Oya) | 5.00 | 🟢 Normal | 0.753 | 🔺 Rising |
| 2026-04-20 22:01:00 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:00:12 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.141 |  |
| 2026-04-20 22:00:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 22:05:13 | Thanamalwila (Kirindi Oya) | 3.92 | 🟢 Normal | 2.968 | 🔺 Rising |
| 2026-04-20 22:01:30 | Kuda Oya (Kirindi Oya) | 5.00 | 🟢 Normal | 0.753 | 🔺 Rising |
| 2026-04-20 22:04:26 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | 0.531 | 🔺 Rising |
| 2026-04-20 22:01:31 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.459 | 🔺 Rising |
| 2026-04-20 22:03:47 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-04-20 22:02:28 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-04-20 22:07:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-20 22:04:26 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-20 22:05:36 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-20 22:06:17 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-20 22:04:12 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-20 22:02:54 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-20 22:04:59 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-20 22:03:51 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 22:17:47 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-20 22:05:21 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 22:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 22:06:29 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 22:01:00 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:01:32 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:04:43 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:04:52 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:00:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:02:03 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:04:04 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:05:39 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 22:09:49 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-20 21:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-20 22:04:20 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-04-20 22:03:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-04-20 21:19:28 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-04-20 22:02:47 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.080 |  |
| 2026-04-20 22:03:08 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.110 |  |
| 2026-04-20 22:00:12 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.141 |  |
| 2026-04-20 22:07:16 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.144 |  |
| 2026-04-20 22:02:13 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.296 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)