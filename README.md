# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_04:06:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,045 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 04:06:28 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | -0.010 |  |
| 2026-06-21 04:06:14 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:05:13 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:04:52 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-06-21 04:04:21 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-21 04:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 04:03:17 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:02:26 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:02:26 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-06-21 04:02:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:02:17 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:02:10 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:01:53 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 04:01:50 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:01:13 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 04:00:41 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.053 |  |
| 2026-06-21 03:54:20 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-06-21 03:41:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.031 |  |
| 2026-06-21 03:31:19 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.013 |  |
| 2026-06-21 03:28:35 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-21 03:22:00 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 03:05:46 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-21 03:28:35 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-21 03:02:20 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-21 04:01:53 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 04:01:13 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 04:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-21 04:02:10 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 03:11:25 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:02:26 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 03:05:11 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-21 03:16:32 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:02:17 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.000 |  |
| 2026-06-21 03:06:24 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-21 03:02:48 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:03:17 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:06:14 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-21 03:04:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:02:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:05:13 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:03:24 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 04:01:50 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 03:03:54 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-21 03:02:31 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-21 04:04:21 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-21 04:06:28 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | -0.010 |  |
| 2026-06-21 03:03:09 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-06-21 04:04:52 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-21 03:54:20 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-06-21 03:03:25 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-06-21 04:02:26 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-06-21 03:31:19 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.013 |  |
| 2026-06-21 03:22:00 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.018 |  |
| 2026-06-21 03:41:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.031 |  |
| 2026-06-21 04:00:41 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.053 |  |
| 2026-06-21 03:06:08 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -216.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)