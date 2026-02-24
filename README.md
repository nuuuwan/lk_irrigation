# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_05:24:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,384 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 05:24:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-25 05:13:55 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:10:54 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-25 05:10:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-25 05:08:07 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:07:36 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:07:32 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:07:26 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:07:03 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.003 |  |
| 2026-02-25 05:06:37 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:06:05 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:05:54 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.009 |  |
| 2026-02-25 05:05:51 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.005 |  |
| 2026-02-25 05:04:39 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.056 |  |
| 2026-02-25 05:04:35 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:04:31 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:04:12 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -3.000 |  |
| 2026-02-25 05:03:58 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.102 |  |
| 2026-02-25 05:03:48 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -3.000 |  |
| 2026-02-25 05:03:33 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -22.500 |  |
| 2026-02-25 05:03:17 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -22.500 |  |
| 2026-02-25 05:02:54 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 05:02:44 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:02:23 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-02-25 05:02:20 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-02-25 05:02:11 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.027 |  |
| 2026-02-25 05:02:07 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:01:52 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-25 05:01:32 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:01:29 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:01:09 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-25 05:00:59 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-02-25 05:00:46 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:00:45 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.051 |  |
| 2026-02-25 04:39:38 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -0.027 |  |
| 2026-02-25 04:39:37 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.027 |  |
| 2026-02-25 04:36:17 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 05:02:23 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-02-25 05:10:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-25 05:10:54 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-25 05:24:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-25 05:02:54 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 05:05:51 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.005 |  |
| 2026-02-25 05:07:32 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:01:52 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:01:29 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:20 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:02:44 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:07:36 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:01:32 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:06:37 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:00:46 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:06:05 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:07:26 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:04:35 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:13:55 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:04:31 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:08:07 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:02:07 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:07:03 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.003 |  |
| 2026-02-25 05:05:54 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.009 |  |
| 2026-02-25 05:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-25 04:01:44 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-02-25 05:01:09 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-25 01:05:46 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.011 |  |
| 2026-02-25 05:02:11 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.027 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-25 05:02:20 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-02-25 05:00:59 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |
| 2026-02-25 05:00:45 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.051 |  |
| 2026-02-25 05:04:39 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.056 |  |
| 2026-02-25 05:03:58 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.102 |  |
| 2026-02-25 05:04:12 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -3.000 |  |
| 2026-02-25 05:03:33 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -22.500 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)