# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_21:15:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,197 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 21:15:36 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:12:25 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-06-26 21:10:42 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.025 |  |
| 2026-06-26 21:09:22 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-26 21:09:13 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-26 21:06:55 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-26 21:06:15 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:05:41 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:05:40 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-06-26 21:05:39 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 21:05:11 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:04:57 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-26 21:04:25 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 21:04:17 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:04:12 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-26 21:04:00 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:03:48 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:03:34 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:03:23 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:03:19 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-06-26 21:02:51 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.167 |  |
| 2026-06-26 21:02:28 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:02:25 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 21:02:25 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:02:25 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:02:09 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-26 21:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:01:38 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:01:31 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:01:10 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:01:10 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:01:08 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-06-26 21:01:01 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:00:51 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:00:34 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 21:01:08 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-06-26 21:04:57 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-26 21:09:13 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-26 21:02:09 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-26 21:09:22 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-26 21:05:39 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 21:02:25 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 21:04:25 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 21:04:12 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-26 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:03:48 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:01:10 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:01:01 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:01:38 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:06:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:01:10 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:02:25 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:02:28 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:00:34 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:00:51 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:15:36 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:03:34 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:05:11 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:03:23 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:04:00 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:06:15 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-26 20:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-06-26 21:06:55 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-26 21:04:17 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:02:25 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:01:31 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:05:41 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-06-26 21:03:19 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-06-26 21:05:40 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-06-26 21:12:25 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-06-26 21:10:42 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.025 |  |
| 2026-06-26 21:02:51 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)