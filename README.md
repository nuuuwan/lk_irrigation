# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_20:26:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,054 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 20:26:42 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-24 20:16:39 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:16:34 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.034 |  |
| 2026-04-24 20:12:17 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-24 20:09:48 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:09:05 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.028 |  |
| 2026-04-24 20:08:36 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:08:32 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-04-24 20:08:15 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.039 |  |
| 2026-04-24 20:08:03 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-24 20:07:57 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:06:31 | Katharagama (Menik Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:06:29 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:06:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.090 |  |
| 2026-04-24 20:05:12 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-04-24 20:05:01 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 20:05:01 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.029 |  |
| 2026-04-24 20:04:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-04-24 20:04:04 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:03:53 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.040 |  |
| 2026-04-24 20:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.071 |  |
| 2026-04-24 20:03:51 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-04-24 20:03:40 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:03:38 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-04-24 20:03:23 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-04-24 20:02:47 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-04-24 20:02:41 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:02:23 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:02:23 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:02:14 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:02:13 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:01:46 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:01:18 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:01:12 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-24 20:01:08 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-24 20:00:48 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-24 20:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:00:27 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 20:00:48 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-24 20:12:17 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-24 20:01:12 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-24 20:08:03 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-24 20:26:42 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-24 20:05:01 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 20:03:40 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:16:39 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:02:23 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:07:57 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:02:14 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:04:04 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:02:13 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:06:31 | Katharagama (Menik Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:06:29 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:01:46 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:09:48 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:02:41 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:01:18 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-24 20:08:32 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-04-24 20:01:08 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-24 20:03:38 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-04-24 20:03:23 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-04-24 20:04:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-04-24 20:03:51 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-04-24 20:09:05 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.028 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-24 20:05:01 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.029 |  |
| 2026-04-24 20:02:47 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-04-24 20:05:12 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-04-24 20:16:34 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.034 |  |
| 2026-04-24 20:08:15 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.039 |  |
| 2026-04-24 20:03:53 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.040 |  |
| 2026-04-24 20:00:27 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.042 |  |
| 2026-04-24 20:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.071 |  |
| 2026-04-24 20:06:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)