# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_01:29:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,355 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 01:29:04 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.008 |  |
| 2026-02-24 01:10:28 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-02-24 01:08:26 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.053 |  |
| 2026-02-24 01:07:19 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.009 |  |
| 2026-02-24 01:07:03 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.018 |  |
| 2026-02-24 01:06:53 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:05:23 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-24 01:05:10 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.057 |  |
| 2026-02-24 01:05:02 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 3.868 | 🔺 Rising |
| 2026-02-24 01:04:43 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:04:19 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:04:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-02-24 01:03:43 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:03:36 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:03:30 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:03:00 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.100 |  |
| 2026-02-24 01:02:43 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:02:23 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:02:21 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:02:20 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:02:13 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-02-24 01:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:02:03 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:01:52 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:01:42 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 01:01:40 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:01:39 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:01:17 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-24 01:01:02 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:01:00 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 3.868 | 🔺 Rising |
| 2026-02-24 01:00:48 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 01:05:02 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 3.868 | 🔺 Rising |
| 2026-02-24 01:04:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-02-24 01:05:23 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-24 01:01:17 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-24 01:00:48 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 01:01:42 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 01:02:43 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:01:52 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:03:36 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:01:40 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:03:30 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:02:23 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:04:19 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:01:02 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:04:43 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:06:53 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:01:40 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-24 01:29:04 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.008 |  |
| 2026-02-24 01:10:28 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-02-24 01:07:19 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.009 |  |
| 2026-02-24 01:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:04:12 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:03:43 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:01:44 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:02:20 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:01:39 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:02:21 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-24 01:07:03 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.018 |  |
| 2026-02-24 01:02:13 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-02-23 18:03:52 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.028 |  |
| 2026-02-24 00:02:12 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-02-24 00:11:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.037 |  |
| 2026-02-24 00:05:34 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.048 |  |
| 2026-02-24 01:08:26 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.053 |  |
| 2026-02-24 01:05:10 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.057 |  |
| 2026-02-24 01:03:00 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.100 |  |
| 2026-02-24 00:02:11 | Manampitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)