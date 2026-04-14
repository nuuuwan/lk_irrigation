# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_19:17:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,093 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 19:17:12 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.016 |  |
| 2026-04-14 19:13:28 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:08:30 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-04-14 19:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.041 |  |
| 2026-04-14 19:07:45 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.019 |  |
| 2026-04-14 19:07:39 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.028 |  |
| 2026-04-14 19:07:23 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.045 |  |
| 2026-04-14 19:06:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.063 |  |
| 2026-04-14 19:06:48 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-04-14 19:06:17 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-14 19:05:55 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:05:37 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-14 19:05:34 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-04-14 19:04:58 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-14 19:04:44 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:04:14 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:03:12 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:02:50 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:02:36 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-14 19:02:35 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 19:02:33 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:02:30 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-04-14 19:02:27 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 19:02:26 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-14 19:02:17 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-14 19:02:13 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:02:10 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -18.000 |  |
| 2026-04-14 19:02:08 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -18.000 |  |
| 2026-04-14 19:01:49 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:01:47 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:01:13 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:00:44 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:00:44 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 19:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:00:11 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 19:05:37 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-14 19:04:58 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-14 19:00:44 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 19:02:35 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 19:02:27 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 19:02:36 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-14 19:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:05:55 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:00:44 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:01:13 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:03:12 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:01:47 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:02:33 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-14 18:06:57 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:13:28 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-14 19:02:50 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:04:14 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:00:11 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:02:13 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:04:44 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:01:49 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:06:17 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-14 19:02:17 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-14 19:17:12 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.016 |  |
| 2026-04-14 19:07:45 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.019 |  |
| 2026-04-14 19:08:30 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-04-14 19:02:26 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:02:56 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-14 19:07:39 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.028 |  |
| 2026-04-14 19:02:30 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-04-14 19:06:48 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-04-14 19:05:34 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-04-14 19:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.041 |  |
| 2026-04-14 19:07:23 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.045 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-14 19:06:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.063 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-14 19:02:10 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)