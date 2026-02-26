# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_09:04:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,424 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 09:04:35 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:04:35 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:04:25 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:04:21 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:04:10 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:04:06 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:04:01 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:03:52 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.020 |  |
| 2026-02-26 09:03:52 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-02-26 09:03:47 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:03:38 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:03:28 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:03:25 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 09:03:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:03:22 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 09:03:21 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-26 09:03:04 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-26 09:03:04 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:03:02 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 09:03:01 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:02:55 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:02:41 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:02:30 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:02:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.060 |  |
| 2026-02-26 09:02:24 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:02:13 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-26 09:02:13 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:02:12 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.135 |  |
| 2026-02-26 09:02:05 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-26 09:01:49 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.014 |  |
| 2026-02-26 09:01:33 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:01:31 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:01:15 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.015 |  |
| 2026-02-26 09:00:28 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:38:40 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.029 |  |
| 2026-02-26 08:23:00 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:18:05 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.014 |  |
| 2026-02-26 08:14:19 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:13:12 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:11:05 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 09:03:04 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-26 09:03:21 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-26 09:03:02 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 09:02:13 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-26 09:03:25 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 09:03:22 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 09:02:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:02:41 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:04:21 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:03:04 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:01:33 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:02:55 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:01:31 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:03:47 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:03:01 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:04:35 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:02:30 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:04:35 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:00:28 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:03:28 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:05:04 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:03:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:04:10 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:36 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 09:04:01 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:04:25 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:04:06 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:02:13 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:02:24 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:03:38 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-26 09:03:52 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-02-26 09:01:49 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.014 |  |
| 2026-02-26 09:01:15 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.015 |  |
| 2026-02-26 09:02:05 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-26 09:03:52 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.020 |  |
| 2026-02-26 08:06:11 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.022 |  |
| 2026-02-26 08:38:40 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.029 |  |
| 2026-02-26 09:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.060 |  |
| 2026-02-26 09:02:12 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)