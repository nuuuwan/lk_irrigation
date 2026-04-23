# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_06:30:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,610 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 06:30:20 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.015 |  |
| 2026-04-23 06:20:15 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-23 06:13:23 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.008 |  |
| 2026-04-23 06:10:17 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-23 06:08:25 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-23 06:07:59 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.045 |  |
| 2026-04-23 06:07:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.109 |  |
| 2026-04-23 06:07:11 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-23 06:06:03 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-04-23 06:05:54 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-23 06:05:20 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.061 |  |
| 2026-04-23 06:05:06 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-23 06:04:59 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.078 |  |
| 2026-04-23 06:04:05 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-23 06:03:59 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-23 06:03:56 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-23 06:03:54 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-04-23 06:03:38 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 06:03:23 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.050 |  |
| 2026-04-23 06:03:11 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | -0.050 |  |
| 2026-04-23 06:03:08 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-23 06:02:59 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.266 |  |
| 2026-04-23 06:02:31 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-23 06:02:26 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-04-23 06:02:24 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.012 |  |
| 2026-04-23 06:02:24 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.050 |  |
| 2026-04-23 06:02:12 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-23 06:01:40 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-23 06:01:39 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.046 |  |
| 2026-04-23 06:01:34 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.651 |  |
| 2026-04-23 06:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | 1.863 | 🔺 Rising |
| 2026-04-23 06:01:26 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | -0.070 |  |
| 2026-04-23 06:01:12 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-04-23 06:01:12 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-23 06:00:41 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-23 06:00:23 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-04-23 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-23 05:51:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 1.863 | 🔺 Rising |
| 2026-04-23 05:50:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 1.863 | 🔺 Rising |
| 2026-04-23 05:43:32 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-23 05:37:48 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.148 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 06:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | 1.863 | 🔺 Rising |
| 2026-04-23 06:02:26 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-04-23 06:00:23 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-04-23 06:07:11 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-23 06:10:17 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-23 06:20:15 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-23 06:05:54 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-23 06:08:25 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-23 06:03:08 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-23 06:02:31 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-23 06:01:40 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-23 06:03:56 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-23 06:00:41 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-23 06:05:06 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-23 06:03:38 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 06:02:12 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-23 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-23 05:01:52 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 06:04:05 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-23 06:06:03 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-04-23 06:03:59 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-23 06:13:23 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.008 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-23 06:01:12 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-23 06:03:54 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-04-23 06:01:12 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-04-23 06:02:24 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.012 |  |
| 2026-04-23 06:30:20 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.015 |  |
| 2026-04-23 06:07:59 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.045 |  |
| 2026-04-23 06:01:39 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.046 |  |
| 2026-04-23 06:03:11 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | -0.050 |  |
| 2026-04-23 06:03:23 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.050 |  |
| 2026-04-23 06:02:24 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.050 |  |
| 2026-04-23 06:05:20 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.061 |  |
| 2026-04-23 06:01:26 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | -0.070 |  |
| 2026-04-23 06:04:59 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.078 |  |
| 2026-04-23 06:07:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.109 |  |
| 2026-04-23 06:02:59 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.266 |  |
| 2026-04-23 06:01:34 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.651 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)