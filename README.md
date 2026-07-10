# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_02:38:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,934 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 02:38:03 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.013 |  |
| 2026-07-11 02:21:26 | Thalgahagoda (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:17:40 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:13:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:12:55 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:11:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 6.857 | 🔺 Rising |
| 2026-07-11 02:10:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 6.857 | 🔺 Rising |
| 2026-07-11 02:10:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 6.857 | 🔺 Rising |
| 2026-07-11 02:10:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 6.857 | 🔺 Rising |
| 2026-07-11 02:09:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 6.857 | 🔺 Rising |
| 2026-07-11 02:08:26 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 02:07:49 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:06:39 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-07-11 02:06:06 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.648 |  |
| 2026-07-11 02:06:00 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-07-11 02:05:11 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:04:58 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-07-11 02:04:29 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-07-11 02:03:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:03:22 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 02:03:14 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:02:53 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-07-11 02:02:30 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-11 02:02:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:02:22 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:02:18 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-11 02:02:17 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:02:13 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:02:10 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:01:57 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:01:53 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:01:15 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 02:00:49 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:00:36 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-11 01:59:37 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.648 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 02:11:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 6.857 | 🔺 Rising |
| 2026-07-11 02:06:00 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-07-11 02:02:30 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-11 02:02:18 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-11 02:01:15 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 01:05:17 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 02:03:22 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 02:08:26 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 01:19:53 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-11 01:39:20 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-07-11 01:03:53 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.005 |  |
| 2026-07-10 18:05:00 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:02:10 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:02:17 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:00:49 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:03:14 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:02:13 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:09:34 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:17:40 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:07:49 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:02:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:05:11 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:00:36 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:01:53 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:12:55 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-11 01:03:59 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:13:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:03:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:21:26 | Thalgahagoda (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 01:13:52 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 01:01:20 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:38:03 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.013 |  |
| 2026-07-11 02:04:58 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-07-11 02:04:29 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-07-11 02:06:39 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-07-11 02:02:53 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-07-11 01:10:00 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.028 |  |
| 2026-07-11 02:06:06 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.648 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)