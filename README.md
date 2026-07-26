# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_03:20:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **217,258 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 03:20:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:13:33 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:09:10 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-07-27 03:09:06 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-07-27 03:08:24 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-27 03:07:00 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:06:25 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:05:33 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:48 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:37 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.199 |  |
| 2026-07-27 03:04:33 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:32 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:31 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:16 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:03 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:03:27 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-27 03:03:25 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-07-27 03:03:20 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:03:12 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:02:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:02:36 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.044 |  |
| 2026-07-27 03:02:21 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-27 03:02:10 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:02:03 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:01:55 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:01:52 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-07-27 03:01:27 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:01:26 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.020 |  |
| 2026-07-27 03:01:07 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-27 03:01:07 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-27 03:00:54 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:00:06 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 02:47:10 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 03:03:27 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-27 03:02:21 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-26 21:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-27 03:01:07 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-27 03:08:24 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-27 03:13:33 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:01:27 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:00:54 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:01:55 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:03:20 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:20:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 18:03:43 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:05:33 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:07:00 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:03:12 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:32 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-27 00:08:10 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:02:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:00:06 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:02:10 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:33 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:03 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:31 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-26 18:00:36 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:02:03 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:16 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:48 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:06:25 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:03:25 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-07-27 03:01:07 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-27 03:09:06 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-07-26 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.020 |  |
| 2026-07-27 03:01:26 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.020 |  |
| 2026-07-27 03:09:10 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-07-27 02:39:55 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.032 |  |
| 2026-07-27 03:01:52 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-07-27 03:02:36 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.044 |  |
| 2026-07-27 03:04:37 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)