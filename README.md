# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_13:18:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,749 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 13:18:52 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.034 |  |
| 2026-04-15 13:11:32 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-04-15 13:10:02 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-04-15 13:09:17 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-15 13:08:12 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:07:28 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-04-15 13:07:24 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-15 13:07:14 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-04-15 13:07:13 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 13:06:54 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-04-15 13:06:36 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-04-15 13:06:28 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-15 13:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-04-15 13:05:13 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:05:11 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:04:41 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:04:16 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.020 |  |
| 2026-04-15 13:03:42 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:03:38 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 7.322 | 🔺 Rising |
| 2026-04-15 13:03:35 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.022 |  |
| 2026-04-15 13:03:35 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-15 13:03:20 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:02:20 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:02:06 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.086 |  |
| 2026-04-15 13:02:04 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 13:01:57 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:01:40 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 7.322 | 🔺 Rising |
| 2026-04-15 13:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:01:23 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.049 |  |
| 2026-04-15 13:01:15 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:01:15 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.248 |  |
| 2026-04-15 13:01:08 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-15 13:01:06 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-04-15 13:01:03 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:00:58 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-04-15 13:00:53 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:00:44 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-15 13:00:34 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 13:03:38 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 7.322 | 🔺 Rising |
| 2026-04-15 13:06:28 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-15 13:07:24 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-15 13:07:13 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 13:01:08 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-15 13:02:04 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 13:09:17 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-15 13:01:03 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:01:15 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:03:20 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:03:42 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:08:12 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:00:48 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:02:20 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:00:53 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:01:57 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:05:11 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:05:13 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 13:10:02 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-04-15 13:07:28 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-04-15 13:07:14 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-04-15 13:06:54 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-04-15 13:03:35 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-15 13:00:44 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-15 13:00:34 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-15 13:04:16 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.020 |  |
| 2026-04-15 13:06:36 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-04-15 13:00:58 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-04-15 13:03:35 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.022 |  |
| 2026-04-15 12:00:38 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.030 |  |
| 2026-04-15 13:01:06 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-04-15 13:11:32 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-04-15 13:18:52 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.034 |  |
| 2026-04-15 13:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-04-15 13:01:23 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.049 |  |
| 2026-04-15 13:02:06 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.086 |  |
| 2026-04-15 12:00:16 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.152 |  |
| 2026-04-15 13:01:15 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.248 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)