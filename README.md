# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_05:06:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,056 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 05:06:20 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-02-28 05:06:11 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-02-28 05:06:01 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-28 05:05:33 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.070 |  |
| 2026-02-28 05:05:11 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.012 |  |
| 2026-02-28 05:04:50 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-28 05:04:21 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 05:03:42 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.066 |  |
| 2026-02-28 05:03:42 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:03:41 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:03:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-02-28 05:03:20 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 05:02:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:02:50 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:02:40 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 05:02:40 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 05:02:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:02:09 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:02:01 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-28 05:01:32 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:01:31 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-02-28 05:01:01 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:00:59 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:00:38 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:00:18 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-28 04:54:38 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-28 04:25:52 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 04:18:14 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 04:14:31 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 04:13:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.070 |  |
| 2026-02-28 04:13:23 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.012 |  |
| 2026-02-28 04:11:44 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 05:02:01 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-28 05:00:18 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-28 05:03:20 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 04:03:23 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 05:04:21 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 05:02:40 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 05:02:40 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 04:05:25 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-28 05:00:38 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-28 04:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:01:21 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:05:33 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:02:50 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:13:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:03:42 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:01:01 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 04:01:26 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:01:32 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:00:59 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 04:25:52 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:02:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:02:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:03:41 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:03:42 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:03:05 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 05:02:09 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-28 04:04:29 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.005 |  |
| 2026-02-28 05:06:01 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-28 05:04:50 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-28 05:01:31 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-02-28 04:00:13 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-02-28 05:06:20 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-02-28 05:06:11 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-02-28 04:02:48 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-02-28 05:05:11 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.012 |  |
| 2026-02-27 18:05:48 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.028 |  |
| 2026-02-28 05:03:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-02-28 05:03:42 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.066 |  |
| 2026-02-28 05:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)