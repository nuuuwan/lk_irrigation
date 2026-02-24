# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_04:39:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,349 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **49** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 04:39:38 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -36.000 |  |
| 2026-02-25 04:39:37 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -36.000 |  |
| 2026-02-25 04:36:17 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-25 04:28:14 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:21:43 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-02-25 04:15:42 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.027 |  |
| 2026-02-25 04:10:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-25 04:10:03 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:09:08 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-02-25 04:05:21 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:05:13 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-25 04:04:41 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:04:39 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-25 04:04:39 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:04:34 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-02-25 04:03:49 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-02-25 04:03:42 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:03:25 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.003 |  |
| 2026-02-25 04:03:19 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:03:06 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:53 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:50 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:49 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:23 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-02-25 04:02:22 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-02-25 04:02:20 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-02-25 04:02:19 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-02-25 04:02:10 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:09 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:08 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:05 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:04 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:03 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:01:49 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -36.000 |  |
| 2026-02-25 04:01:48 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -36.000 |  |
| 2026-02-25 04:01:47 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -36.000 |  |
| 2026-02-25 04:01:45 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -36.000 |  |
| 2026-02-25 04:01:44 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-02-25 04:01:41 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:01:37 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -396.000 |  |
| 2026-02-25 04:01:35 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -396.000 |  |
| 2026-02-25 04:01:33 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -396.000 |  |
| 2026-02-25 04:01:15 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:01:14 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:57:51 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:57:49 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:51:51 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:49:04 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 04:02:23 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-02-25 04:10:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-25 03:17:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-02-25 03:07:31 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-25 04:05:13 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-25 04:36:17 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-25 03:17:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:01:15 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:05 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:01:46 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:01:41 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-25 02:00:30 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:20 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:03:19 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:10:03 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:04:41 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:10 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:49 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:28:14 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:05:21 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:03:42 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:02:50 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 04:03:25 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.003 |  |
| 2026-02-25 04:09:08 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-02-25 04:04:39 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-25 04:01:44 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-02-25 01:05:46 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.011 |  |
| 2026-02-25 04:03:49 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-02-25 04:04:34 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-02-25 04:15:42 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.027 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-25 04:21:43 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |
| 2026-02-25 03:19:28 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -4.500 |  |
| 2026-02-25 04:39:38 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -36.000 |  |
| 2026-02-25 04:01:49 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -36.000 |  |
| 2026-02-25 04:01:37 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -396.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)