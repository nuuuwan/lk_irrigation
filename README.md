# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_03:28:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 03:28:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:28:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:28:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:19:42 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.004 |  |
| 2026-02-25 03:19:28 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -4.500 |  |
| 2026-02-25 03:18:56 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -4.500 |  |
| 2026-02-25 03:17:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:17:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:17:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-02-25 03:09:09 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:09:08 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:08:42 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:08:41 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:08:40 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:08:39 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:08:39 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:08:38 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:08:34 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-02-25 03:08:27 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:07:31 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-25 03:05:36 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:04:52 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:04:16 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:03:51 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:03:45 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:03:38 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:03:19 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:03:16 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:02:12 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:02:02 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-25 03:01:46 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:01:24 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:01:21 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 02:58:24 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 02:44:17 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 03:17:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-02-25 01:00:35 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-25 01:01:49 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-25 03:02:02 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-25 03:07:31 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-25 02:04:53 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-25 03:17:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:01:46 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:04:16 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:01:24 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-25 02:03:56 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-25 02:00:30 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:20 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:03:45 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:28:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:03:19 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:09:09 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:05:36 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:02:12 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:08:27 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:03:38 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 01:07:21 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:04:52 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:03:16 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:08:42 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-25 03:19:42 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.004 |  |
| 2026-02-25 01:04:14 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.005 |  |
| 2026-02-25 03:08:34 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-02-25 01:01:16 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-25 01:01:42 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-25 01:02:17 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-02-25 01:05:46 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.011 |  |
| 2026-02-25 01:02:26 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | -0.015 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |
| 2026-02-25 01:11:49 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.138 |  |
| 2026-02-25 02:06:09 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -1.895 |  |
| 2026-02-25 03:19:28 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -4.500 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)