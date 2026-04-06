# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_12:16:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,707 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 12:16:18 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.027 |  |
| 2026-04-06 12:14:24 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:12:29 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:10:53 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:08:07 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:07:25 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:07:06 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:07:04 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:06:57 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.039 |  |
| 2026-04-06 12:06:21 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:05:47 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 12:05:41 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-04-06 12:05:31 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.060 |  |
| 2026-04-06 12:05:16 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:05:01 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-04-06 12:04:43 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-04-06 12:04:16 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.386 |  |
| 2026-04-06 12:04:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:03:50 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-06 12:03:48 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-06 12:03:33 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.012 |  |
| 2026-04-06 12:03:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-04-06 12:03:29 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:03:03 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 12:02:58 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:52 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:45 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:22 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:02:20 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:15 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 12:01:26 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-04-06 12:01:13 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-04-06 12:01:12 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:01:08 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:00:46 | Thanthirimale (Malwathu Oya) | 1.81 | 🟢 Normal | -0.030 |  |
| 2026-04-06 12:00:38 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:00:30 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:00:07 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 12:03:50 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-06 12:03:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-04-06 12:03:48 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-06 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 12:03:03 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 12:05:47 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 12:02:52 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:00:38 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:01:12 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:20 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:45 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:14:24 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:08:07 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:15 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:07:06 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:07:04 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:10:53 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:02:58 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:06:21 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:04:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:07:25 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 12:12:29 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:03:29 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:01:08 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:05:16 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:02:22 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-06 12:05:41 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-04-06 12:05:01 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-04-06 12:04:43 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-04-06 12:03:33 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.012 |  |
| 2026-04-06 12:01:13 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-04-06 12:16:18 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.027 |  |
| 2026-04-06 12:00:46 | Thanthirimale (Malwathu Oya) | 1.81 | 🟢 Normal | -0.030 |  |
| 2026-04-06 12:06:57 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.039 |  |
| 2026-04-06 12:01:26 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-04-06 12:05:31 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.060 |  |
| 2026-04-06 12:04:16 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.386 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)